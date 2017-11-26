import sys
import subprocess
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import * 


class Application(QtGui.QMainWindow):
	def __init__(self, *args):
		#Creates the main window with the menu bar and buttons``
		QtGui.QMainWindow.__init__(self, *args)
		self.UI()

	def UI(self):
		self.setWindowTitle("Volatility GUI")		
		self.resize(640,500)
		self.Buttons()
		self.text_output = QtGui.QTextEdit(self)
		self.text_output.setGeometry(10,100,500,370)

		#Creates the menubar
		self.File = self.menuBar().addMenu("File")
		self.openFile = QtGui.QAction("Open File", self, triggered=self.selectFile)
		self.File.addAction(self.openFile)

		#Can input a command 
		self.linetext = QtGui.QLineEdit(self)
		self.linetext.setGeometry(15,65,495,25)

	def selectFile(self):
		selectFile = QtGui.QFileDialog.getOpenFileName(self, "Please select the image")		
		self.linetext.insert("-f")
		file_Selected = self.linetext.insert(selectFile)
		

	def Buttons(self):
		button1 = QtGui.QPushButton('Run', self)
		buttonone.move(510,60)
		button1.clicked.connect(self.runCommand)
		
		pushProfile = QtGui.QPushButton('Profiles', self)
		pushProfile.setText("Profiles")
		pushProfile.clicked.connect(self.findProfiles)
		pushProfile.move(205,30)

		msgBox = QtGui.QMessageBox()
		msgBox.setText("Please select the plugin you wish to choose")

		pluginClikcer = QtGui.QPushButton('Plugins', self)
		pluginClikcer.move(55,30)
		pluginClikcer.clicked.connect(self.findPlugins)

	def findPlugins(self):
		#Creates the popup for the plugins
		pluginPop = QtGui.QDialog()
		pluginList = QtGui.QButtonGroup() 
		pluginPop.setWindowTitle("Plugin Selection")
		label3 = QtGui.QLabel("Image Identification", pluginPop)
		label4 = QtGui.QLabel("Process Listings",pluginPop)
		label5 = QtGui.QLabel("Process Information",pluginPop)
		label6 = QtGui.QLabel ("PE File Extraction",pluginPop)
		label7 = QtGui.QLabel("Injected Code",pluginPop)		
		checkbox_1 = QtGui.QCheckBox("imageinfo", pluginPop)
		checkbox_2 = QtGui.QCheckBox("kdbgscan", pluginPop)
		checkbox_3 = QtGui.QCheckBox("pslist", pluginPop)
		checkbox4 = QtGui.QCheckBox("VistaSP1x86", popUp)
		checkbox5 = QtGui.QCheckBox("VistaSP2x64", popUp)
		checkbox6 = QtGui.QCheckBox("Win07x86", popUp)
		checkbox7 = QtGui.QCheckBox("Win07x64", popUp)
		checkbox8 = QtGui.QCheckBox("Win10x86", popUp)
		checkbox9 = QtGui.QCheckBox("Win10x64", popUp)
		checkbox10 = QtGui.QCheckBox("CentOSx64", popUp)
		checkbox_1.move(0,20)
		pluginList.addButton(checkbox_1)
		checkbox_1.show()
		checkbox_2.move(0,40)
		pluginList.addButton(checkbox_2)
		checkbox_2.show()
		label4.move(0,60)
		label4.setFont(QtGui.QFont("Times",weight = QtGui.QFont.Bold))
		label4.show()
		checkbox_3.move(0,80)
		pluginList.addButton(checkbox_3)
		checkbox_3.show()
		checkbox4.move(0,80)
		buttonList.addButton(checkbox4)
		checkbox4.show()
		checkbox5.move(0,100)
		buttonList.addButton(checkbox5)
		checkbox5.show()
		checkbox6.move(0,120)
		buttonList.addButton(checkbox6)
		checkbox6.show()
		checkbox7.move(0,140)
		buttonList.addButton(checkbox7)
		checkbox7.show()
		checkbox8.move(0,160)
		buttonList.addButton(checkbox8)
		checkbox8.show()
		checkbox9.move(0,180)
		buttonList.addButton(checkbox9)
		checkbox9.show()
		label2.move(0,200)
		label2.setFont(QtGui.QFont("Times",weight = QtGui.QFont.Bold))
		label2.show()
		checkbox10.move(0,220)
		buttonList.addButton(checkbox10)
		checkbox10.show()
		

	def pInfo(self, button):
		text = self.linetext.text()
		length_initial = text.length()
		self.linetext.insert(" --profile=") 
		self.linetext.insert(button.text())
		object = " --profile="

		counter = 0
		#Get length of the string and get length of the both inserts. Remove them and input the new insert.
		if object in text:
			hi = text.count(object)
			if hi >= 1:
				length_e = self.linetext.text()
				length_entire = length_e.length()
				length_cut = length_entire - length_initial
				lengthi = length_cut * 2
				while( counter < lengthi):
					self.linetext.backspace()
					counter = counter + 1		
		
	


	
	def runCommand(self, button):
		object1 = str(self.linetext.text())
		print object1
		Kappa = subprocess.check_output(["volatility " + object1], shell=True)
		self.text_output.setText(Kappa)
		return Kappa

def main():
	app = QtGui.QApplication(sys.argv)
	win = Application()
	win.show()
	app.exec_()	


if __name__ == "__main__":
	main()
