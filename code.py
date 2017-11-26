from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import * 
import sys
import subprocess

class Application(QtGui.QMainWindow):
	def __init__(self, *args):
		#Creates the main window with the menu bar and buttons``
		QtGui.QMainWindow.__init__(self, *args)
		self.UI()

	def UI(self):
		self.setWindowTitle("Volatility 2.3.1 GUI")		
		self.resize(640,480)
		#self.menuBar_()
		self.Buttons()
		self.text_output = QtGui.QTextEdit(self)
		#self.text_output.move(300,200)
		#self.setCentralWidget(self.text_output)
		self.text_output.setGeometry(10,100,500,370)
		#self.setCentralWidget(self.text_output)

		#Creates the menubar
		self.File = self.menuBar().addMenu("File")
		self.openFile = QtGui.QAction("Open File", self, triggered=self.chooseFile)
		self.File.addAction(self.openFile)

		#This is where the a person can input a command and where the command will appear from all the options that the user selected
		self.linetext = QtGui.QLineEdit(self)
		self.linetext.setGeometry(10,60,500,30)
		

	def chooseFile(self):
		chooseFile = QtGui.QFileDialog.getOpenFileName(self, "Choose the image")		
		#test = subprocess.call(["echo", chooseFile])
		self.linetext.insert(" -f ")
		file_Selected = self.linetext.insert(chooseFile)
		

	def Buttons(self):
		button1 = QtGui.QPushButton('Run', self)
		button1.move(510,60)
		button1.clicked.connect(self.runCommand)
		
		profilesPush = QtGui.QPushButton('Profiles', self)
		profilesPush.setText("Profiles")
		profilesPush.clicked.connect(self.findProfiles)
		profilesPush.move(200,25)

		msgBox = QtGui.QMessageBox()
		msgBox.setText("Select the plugin")

		pluginsbutton = QtGui.QPushButton('Plugins', self)
		pluginsbutton.move(50,25)
		pluginsbutton.clicked.connect(self.findPlugins)

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
		checkbox_4 = QtGui.QCheckBox("psscan", pluginPop)
		checkbox_5 = QtGui.QCheckBox("psxview", pluginPop)
		checkbox_6 = QtGui.QCheckBox("pstree", pluginPop)
		
		checkbox_7 = QtGui.QCheckBox("cmdline", pluginPop)
		checkbox_8 = QtGui.QCheckBox("vadinfo",pluginPop)
		checkbox_9 = QtGui.QCheckBox("vaddump",pluginPop)
		checkbox_10 = QtGui.QCheckBox("handles",pluginPop)
		checkbox_11 = QtGui.QCheckBox("privs",pluginPop)
		checkbox_12 = QtGui.QCheckBox("getsids",pluginPop)
		
		checkbox_13 = QtGui.QCheckBox("moddump",pluginPop)
		checkbox_14 = QtGui.QCheckBox("procdump",pluginPop)
		checkbox_15 = QtGui.QCheckBox("dlldump",pluginPop)
		
		checkbox_16 = QtGui.QCheckBox("malfind",pluginPop)
		checkbox_17 = QtGui.QCheckBox("ldrmodules",pluginPop)
		checkbox_18 = QtGui.QCheckBox("impscan",pluginPop)

		checkbox_19 = QtGui.QCheckBox("sessions",pluginPop)
		checkbox_20 = QtGui.QCheckBox("consoles",pluginPop)		

		label3.move(0,0)
		label3.setFont(QtGui.QFont("Times",weight = QtGui.QFont.Bold))
		label3.show()
		

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

		checkbox_4.move(0,100)
		pluginList.addButton(checkbox_4)
		checkbox_4.show()

		checkbox_5.move(0,120)
		pluginList.addButton(checkbox_5)
		checkbox_5.show()
		
		checkbox_6.move(0,140)
		pluginList.addButton(checkbox_6)
		checkbox_6.show()

		label5.move(0,160)
		label5.setFont(QtGui.QFont("Times",weight = QtGui.QFont.Bold))
		label5.show()

		checkbox_7.move(0,180)
		pluginList.addButton(checkbox_7)
		checkbox_7.show()

		checkbox_8.move(0,200)
		pluginList.addButton(checkbox_8)
		checkbox_8.show()

		checkbox_9.move(0,220)
		pluginList.addButton(checkbox_9)
		checkbox_9.show()
		
		checkbox_10.move(0,240)
		pluginList.addButton(checkbox_10)
		checkbox_10.show()
		
		checkbox_11.move(0,260)
		pluginList.addButton(checkbox_11)
		checkbox_11.show()

		checkbox_12.move(0,280)
		pluginList.addButton(checkbox_12)
		checkbox_12.show()
				
		label6.move(0,300)
		label6.setFont(QtGui.QFont("Times",weight = QtGui.QFont.Bold))
		label6.show()		

		checkbox_13.move(0,320)
		pluginList.addButton(checkbox_13)
		checkbox_13.show()

		checkbox_14.move(0,340)
		pluginList.addButton(checkbox_14)
		checkbox_14.show()

		checkbox_15.move(0,360)
		pluginList.addButton(checkbox_15)
		checkbox_15.show()
	
		label7.move(0,380)
		label7.setFont(QtGui.QFont("Times",weight = QtGui.QFont.Bold))
		label7.show()			
		
		checkbox_16.move(0,400)
		pluginList.addButton(checkbox_16)
		checkbox_16.show()
		
		checkbox_17.move(0,420)
		pluginList.addButton(checkbox_17)
		checkbox_17.show()

		checkbox_18.move(0,440)
		pluginList.addButton(checkbox_18)
		checkbox_18.show()
		
		checkbox_19.move(0,460)
		pluginList.addButton(checkbox_19)
		checkbox_19.show()
		
		checkbox_20.move(0,480)
		pluginList.addButton(checkbox_20)
		checkbox_20.show()
		


		pluginList.buttonClicked.connect(self.pluginsInfo)
		self.checked = pluginList.checkedButton()

		pluginPop.exec_()

	def pluginsInfo(self, button):
		text = self.linetext.text()
		length_initial = text.length()
		self.linetext.insert(" ")
		self.linetext.insert(button.text())
		
		#length_initial = text.length()
		#Get length of the string and get length of the both inserts. Remove them and input the new insert.
	
	
	def findProfiles(self):
		#Creates the popup for the plugins
		popUp = QtGui.QDialog()
		buttonList = QtGui.QButtonGroup() 
		popUp.setWindowTitle("Profiles Selection")
		label1 = QtGui.QLabel("Windows operating Systems", popUp)
		label2 = QtGui.QLabel("Linux Operating Systems",popUp)
		checkbox1 = QtGui.QCheckBox("VistaSP0x64", popUp)
		checkbox2 = QtGui.QCheckBox("VistaSP0x86", popUp)
		checkbox3 = QtGui.QCheckBox("VistaSP1x64", popUp)
		checkbox4 = QtGui.QCheckBox("VistaSP1x86", popUp)
		checkbox5 = QtGui.QCheckBox("VistaSP2x64", popUp)
		checkbox6 = QtGui.QCheckBox("Win07x86", popUp)
		checkbox7 = QtGui.QCheckBox("Win07x64", popUp)
		checkbox8 = QtGui.QCheckBox("Win10x86", popUp)
		checkbox9 = QtGui.QCheckBox("Win10x64", popUp)
		checkbox10 = QtGui.QCheckBox("CentOSx64", popUp)
		checkbox11 = QtGui.QCheckBox("CentOSx86", popUp)
		checkbox12 = QtGui.QCheckBox("Debianx64", popUp)
		checkbox13 = QtGui.QCheckBox("Debianx86", popUp)
		checkbox14 = QtGui.QCheckBox("Fedorax64", popUp)
		checkbox15 = QtGui.QCheckBox("Fedorax86", popUp)
		checkbox16 = QtGui.QCheckBox("Ubuntux64", popUp)
		checkbox17 = QtGui.QCheckBox("Ubuntux86", popUp)

		label1.move(0,0)
		label1.setFont(QtGui.QFont("Times",weight = QtGui.QFont.Bold))
		label1.show()
		
		checkbox1.move(0,20)
		buttonList.addButton(checkbox1)
		checkbox1.show()

		checkbox2.move(0,40)
		buttonList.addButton(checkbox2)
		checkbox2.show()

		checkbox3.move(0,60)
		buttonList.addButton(checkbox3)
		checkbox3.show()

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
		
		checkbox11.move(0,240)
		buttonList.addButton(checkbox11)
		checkbox11.show()

		checkbox12.move(0,260)
		buttonList.addButton(checkbox12)
		checkbox12.show()

		checkbox13.move(0,280)
		buttonList.addButton(checkbox13)
		checkbox13.show()

		checkbox14.move(0,300)
		buttonList.addButton(checkbox14)
		checkbox14.show()

		checkbox15.move(0,320)
		buttonList.addButton(checkbox15)
		checkbox15.show()

		checkbox16.move(0,340)
		buttonList.addButton(checkbox16)
		checkbox16.show()

		checkbox17.move(0,360)
		buttonList.addButton(checkbox17)
		checkbox17.show()



		
		buttonList.buttonClicked.connect(self.profileInfo)
		self.clickedBox = buttonList.checkedButton()

		popUp.exec_()

		#popUp.setText("Select a Plugin")
		#popUp.addbutton(QtGui.QPushButton('Accept'), QtGui.QMessageBox.Yes)	

	def profileInfo(self, button):
		text = self.linetext.text()
		length_initial = text.length()
		self.linetext.insert(" --profile=") 
		self.linetext.insert(button.text())
		thing = " --profile="
		
		#length_initial = text.length()
		counter = 0
		#Get length of the string and get length of the both inserts. Remove them and input the new insert.
		if thing in text:
			hi = text.count(thing)
			if hi >= 1:
				length_e = self.linetext.text()
				length_entire = length_e.length()
				length_cut = length_entire - length_initial
				#print("length_entire: ", length_entire)	
				#print("length_initial: ", length_initial)			
				#print("length_cut: ",length_cut)
				real = length_cut * 2
				#self.linetext.cursorBackward(real, length_cut)
				while( counter < real):
					self.linetext.backspace()
					counter = counter + 1		
		

	
	def runCommand(self, button):
		thing1 = str(self.linetext.text())
		print thing1
		#print("volatility"," -f ", thing1)
		Kappa = subprocess.check_output(["volatility " + thing1], shell=True)
		self.text_output.setText(Kappa)
		return Kappa

def main():
	app = QtGui.QApplication(sys.argv)
	win = Application()
	win.show()
	app.exec_()	


if __name__ == "__main__":
	main()
