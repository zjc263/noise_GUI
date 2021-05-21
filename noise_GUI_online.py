# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 00:06:36 2021

@author: Administrator
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as figureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import h5py
import noise_cache
import numpy as np
import sys,os
from Tonecfg import Ui_tonecfg
from noise_mainwindow import Ui_Noise_mainwindow


try:
    import pyUSRP as u
except ImportError:
    try:
        sys.path.append('..')
        import pyUSRP as u
    except ImportError:
        print ("Cannot find the pyUSRP package")


if not u.Connect():
    u.print_error("Cannot find the GPU server!")
    exit()

class MyStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)
    def write(self, text):
        # Add text to a QTextEdit...
        self.textWritten.emit(str(text))
                

class Main(QMainWindow,Ui_Noise_mainwindow):
    def __init__(self):
       super(Main, self).__init__()
       self.setupUi(self)
       sys.stdout = MyStream(textWritten=self.normalOutputWritten)
       root_dir = os.path.dirname(os.path.abspath('.'))
       runfile=root_dir+"/runnum.txt"
       f = open(runfile, "r")
       noise_cache.runnum=int(f.read())
       f.close()


  
    
    def __del__(self):
    # Restore sys.stdout
       sys.stdout = sys.__stdout__

        
    
    def normalOutputWritten(self, text):   
    
      cursor = self.textEdit.textCursor()
      cursor.movePosition(QtGui.QTextCursor.End)
      cursor.insertText(text)
      self.textEdit.setTextCursor(cursor)
      self.textEdit.ensureCursorVisible()        
    def run(self):
        print("start noise acquisition")
        root_dir = os.path.dirname(os.path.abspath('.'))
        runfile=root_dir+"/runnum.txt"
        f = open(runfile, "r")
        runnum=int(f.read())
        f.close()

        noise_cache.runnum+=1
        self.lcdNumber.display(int(noise_cache.runnum))
        self.get_paramaters()
        
        
        
        
        f=open(runfile,"w")
        f.write(str(noise_cache.runnum))
        f.close()
        
                  
        
    def tone_cfg(self):
        tcfg.OPEN()
    def get_paramaters(self):
        noise_cache.lo=self.Lo_freq.value()
        noise_cache.time=self.time_duration.value()
        noise_cache.rx=self.tx_gain.value()
        noise_cache.tx=self.rx_gain.value()
        noise_cache.sampling_rate=self.sampling_rate.value()
        noise_cache.decimation=self.decimation.value()
        noise_cache.trigger_mode=self.trigger_mode.currentText()
        noise_cache.threshold_mode=self.threshold_mode.currentText()
        noise_cache.slice_len=self.slice_length.value()
        noise_cache.noise_space=self.noise_space.value()
        
        realrate=int(noise_cache.sampling_rate/noise_cache.decimation)
        threshold=noise_cache.threshold
        noise_space=noise_cache.noise_space
        triggermode=noise_cache.trigger_mode
        slice_len=noise_cache.slice_len
        decimation=noise_cache.decimation
        thresholdmode=noise_cache.threshold_mode
        alpha=noise_cache.alpha
        trigger =u.infn(realrate,threshold,slice_len,noise_space,triggermode,decimation,thresholdmode,alpha=alpha)
        
        
        
        
        noise_filename= u.Get_noise(noise_cache.tones, measure_t = noise_cache.time, rate =noise_cache.sampling_rate, decimation = noise_cache.decimation, amplitudes =noise_cache.power,RF =noise_cache.lo, output_filename = noise_cache.runnum, Front_end = "A",Device = None, delay = None,pf_average = 4, tx_gain = noise_cache.tx, rx_gain=noise_cache.rx,mode = "DIRECT", trigger = trigger)
        
        
class tonecfg(QMainWindow,Ui_tonecfg):
    def __init__(self):
      super(tonecfg, self).__init__()
      self.setupUi(self)
      self.pushButton.clicked.connect(self.buildup)
      self.add_row.clicked.connect(self.addrow)
      self.del_row.clicked.connect(self.delrow)
      self.save.clicked.connect(self.savecol)
      self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)  
      self.tableWidget.customContextMenuRequested.connect(self.generateMenu)  
   
    def OPEN(self):
      self.show()
    # def load(self):
    #    try:
    #        noise_cache.tone_num=len(noise_cache.freq_array)
    #        print(noise_cache.tone_num)
    #        self.tableWidget.setRowCount(noise_cache.tone_num)
    #        for r in range(noise_cache.tone_num):           
    #            self.tableWidget.setItem(r,1,noise_cache.freq[r])
    #            self.tableWidget.setItem(r,2,noise_cache.threshold[r])
    #            self.tableWidget.setItem(r,3,noise_cache.alpha[r])
    #            self.tableWidget.setItem(r,4,noise_cache.power[r])
    #    except AttributeError:
    #        self.tableWidget.setRowCount(0)


    def buildup(self):                   
       noise_cache.tone_num=self.spinBox.value()
       print("tone number is "+str(noise_cache.tone_num)) 
       # for t in range (noise_cache.tone_num):     
       self.tableWidget.setRowCount(noise_cache.tone_num)
       for r in range(noise_cache.tone_num):
           threshold = QTableWidgetItem("4")
           alpha = QTableWidgetItem("0")
           power = QTableWidgetItem("1")             
           self.tableWidget.setItem(r,2,threshold)
           self.tableWidget.setItem(r,3,alpha)
           self.tableWidget.setItem(r,4,power)       
    def addrow(self):
       count = self.tableWidget.currentRow() 
       self.tableWidget.insertRow(count+1)
    def delrow(self):
       count = self.tableWidget.currentRow() 
       self.tableWidget.removeRow(count)
    def generateMenu(self,pos):
        menu = QMenu()
        item1 = menu.addAction(u"add row")
        item2 = menu.addAction(u"delete row")
        action = menu.exec_(self.tableWidget.mapToGlobal(pos))
        if action == item1:           
            count = self.tableWidget.currentRow() 
            self.tableWidget.insertRow(count+1)
        elif action == item2:
            count = self.tableWidget.currentRow() 
            self.tableWidget.removeRow(count)
        else:
            return
    def savecol(self): 
        row_num=self.tableWidget.rowCount()
        tones_array=np.zeros(0)
        threshold_array=np.zeros(0)
        alpha_array=np.zeros(0)
        power_array=np.zeros(0)
        for r in range(row_num):
            
           try:
               freq=float(self.tableWidget.item(r,1).text())
               threshold=float(self.tableWidget.item(r,2).text())
               alpha=float(self.tableWidget.item(r,3).text())
               power=float(self.tableWidget.item(r,4).text())
               tones_array=np.append(tones_array,freq)
               threshold_array=np.append(threshold_array,threshold)
               alpha_array=np.append(alpha_array,alpha)
               power_array=np.append(power_array,power)  
               noise_cache.tones=tones_array
               noise_cache.threshold=threshold_array        
               noise_cache.alpha=alpha_array           
               noise_cache.power=power_array                   
           except AttributeError:
               pass

       
           
     
         
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)   
    ui = Main()                         
    tcfg=tonecfg()              
    ui.show()
    ui.run_button.clicked.connect(ui.lcdNumber.setDecMode)
    ui.run_button.clicked.connect(lambda:ui.run())
    ui.pushButton.clicked.connect(lambda:ui.tone_cfg())
    ui.lcdNumber.display(int(noise_cache.runnum))                           
    app.exit(app.exec_())             
