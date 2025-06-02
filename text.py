#Import Library
#from PyQt4 import QtCore, QtGui
from PyQt5 import QtCore, QtWidgets,QtGui
#from PyQt4.QtCore import QTimer
#from PyQt4.QtGui import QApplication
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer
import numpy as np
import cv2
import time
import random
import pyttsx3
import pyttsx3 as pyttsx
import autocomplete
import winsound
import os.path
import sendSMS
import subprocess
import sys

#colourLoop constants
letRowNorm=["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Emergency</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Food</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Water</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Restroom</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Fan</span></p></body></html>"]

letRowBold=["<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b>Emergency</b></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Food</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Water</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Restroom</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Fan</span></p></body></html>","<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Emergency</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b>Food</b></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Water</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Restroom</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Fan</span></p></body></html>","<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Emergency</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Food</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b>Water</b></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Restroom</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Fan</span></p></body></html>","<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Emergency</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Food</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Water</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b>Restroom</b></span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Fan</span></p></body></html>","<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Emergency</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Food</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Water</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Restroom</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\"><b>Fan</b></span></p></body></html>"]


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

#Face Cascades
face_cascade = cv2.CascadeClassifier('haarCascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarCascades/haarcascade_eye_tree_eyeglasses.xml')
#pupil_cascade = cv2.CascadeClassifier('haarcascade_eye2.xml')

#Number signifies camera
cap = cv2.VideoCapture(0)

#Eye constants
bothEyesClosedStart=False
bothEyesClosedStartTime=0
bothFirst=0
leftEyeClosedStart=False
leftEyeClosedStartTime=0
leftFirst=0
rightEyeClosedStart=False
rightEyeClosedStartTime=0
rightFirst=0

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
autocomplete.load()

NUM_ROWS_OF_LETTERS=5
letRowCount=-1
stopRow=False
currentSentence=""
wholeText=""
vidOpen=False
letters=["Emergency","Food","Water","Restroom","Fan"]

def tick():
    #Eye constants
    global bothEyesClosedStart
    global bothEyesClosedStartTime
    global bothFirst
    global leftEyeClosedStart
    global leftEyeClosedStartTime
    global leftFirst
    global rightEyeClosedStart
    global rightEyeClosedStartTime
    global rightFirst
    global timerColour
    global stopRow
    global letRowCount
    global letColCount
    global letters
    global currentSentence
    global wholeText
    global ui
    global row5
    global row6
    global vidOpen
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces)==1:
        #Draw Face
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_grayLeft = gray[y:y+h, x:x+w//2]
            roi_grayRight = gray[y:y+h, x+w//2:x+w]
            roi_color = img[y:y+h, x:x+w]
            leftEye = eye_cascade.detectMultiScale(roi_grayLeft)
            rightEye = eye_cascade.detectMultiScale(roi_grayRight)
            ##Blink
            if len(leftEye)==0 and len(rightEye)==0:
                if bothEyesClosedStart==False:
                    timerColour.stop()
                    bothEyesClosedStartTime=time.time()
                    bothEyesClosedStart=True
                elif time.time()-bothEyesClosedStartTime>.75  and bothFirst==0:
                    winsound.Beep(500, 250)
                    bothFirst=1
                    if stopRow==False:
                        stopRow=True
                    else:
                        stopRow=False
                        if letRowCount<5:
                            currentSentence += str(letters[letRowCount])
                            print(currentSentence)
                            text_to_speech(currentSentence)
                            sendSMS.send(currentSentence)
                            currentSentence = ""
                            
            ##Left Wink
            elif len(leftEye)==1 and len(rightEye)==0:
                if rightEyeClosedStart==False:
                    timerColour.stop()
                    rightEyeClosedStartTime=time.time()
                    rightEyeClosedStart=True
                elif time.time()-rightEyeClosedStartTime>1.5 and rightFirst==0:
                    rightFirst=1
            ##Right Wink
            elif len(leftEye)==0 and len(rightEye)==1:
                if leftEyeClosedStart==False:
                    timerColour.stop()
                    leftEyeClosedStartTime=time.time()
                    leftEyeClosedStart=True
                elif time.time()-leftEyeClosedStartTime>1.5 and leftFirst==0:
                    leftFirst=1
            ##Eyes Open
            elif len(leftEye)==1 and len(rightEye)==1:
                bothFirst=0
                bothEyesClosedStart=False
                bothEyesClosedStartTime=time.time()
                rightFirst=0
                rightEyeClosedStart=False
                leftEyeClosedStartTime=time.time()
                leftFirst=0
                leftEyeClosedStart=False
                rightEyeClosedStartTime=time.time()
                if timerColour.isActive()==False:
                    timerColour.start(1000)
            #Draw Eyes
            for (ex,ey,ew,eh) in rightEye:
                cv2.rectangle(roi_color,(ex+w//2,ey),(ex+ew+w//2,ey+eh),(255,255,0),2)
            for (ex,ey,ew,eh) in leftEye:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    cv2.imshow('BlinkToText Video Feed',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        cap.release()
        cv2.destroyAllWindows()
        server.quit()
        return 0

def close():
    cap.release()
    cv2.destroyAllWindows()
    return 0
    
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.addLnOnly=True
        MainWindow.setObjectName(_fromUtf8("EyeToText Translator"))
        MainWindow.resize(632, 482)
        self.go=True
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(0, 150, 632, 482))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.pauseBut)
       
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 632, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        self.menuStart_Stop_Sel = QtWidgets.QMenu(self.menuSettings)
        self.menuStart_Stop_Sel.setObjectName(_fromUtf8("menuStart_Stop_Sel"))
        self.menuFinger = QtWidgets.QMenu(self.menuSettings)
        self.menuFinger.setObjectName(_fromUtf8("menuFinger"))
        self.menuLetter_Sel = QtWidgets.QMenu(self.menuSettings)
        self.menuLetter_Sel.setObjectName(_fromUtf8("menuLetter_Sel"))
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionWord_Sel = QtWidgets.QAction(MainWindow)
        self.actionWord_Sel.setObjectName(_fromUtf8("actionWord_Sel"))
        self.actionBlink = QtWidgets.QAction(MainWindow)
        self.actionBlink.setObjectName(_fromUtf8("actionBlink"))
        self.actionLeft_Wink = QtWidgets.QAction(MainWindow)
        self.actionLeft_Wink.setObjectName(_fromUtf8("actionLeft_Wink"))
        self.actionRight_Wink = QtWidgets.QAction(MainWindow)
        self.actionRight_Wink.setObjectName(_fromUtf8("actionRight_Wink"))
        self.actionBlink_2 = QtWidgets.QAction(MainWindow)
        self.actionBlink_2.setObjectName(_fromUtf8("actionBlink_2"))
        self.actionLeft_Wink_2 = QtWidgets.QAction(MainWindow)
        self.actionLeft_Wink_2.setObjectName(_fromUtf8("actionLeft_Wink_2"))
        self.actionRight_Wink_2 = QtWidgets.QAction(MainWindow)
        self.actionRight_Wink_2.setObjectName(_fromUtf8("actionRight_Wink_2"))
        self.actionAbout_EyeTotText = QtWidgets.QAction(MainWindow)
        self.actionAbout_EyeTotText.setObjectName(_fromUtf8("actionAbout_EyeTotText"))
        self.actionContact_Developer = QtWidgets.QAction(MainWindow)
        self.actionContact_Developer.setObjectName(_fromUtf8("actionContact_Developer"))
        self.menuStart_Stop_Sel.addAction(self.actionBlink)
        self.menuStart_Stop_Sel.addAction(self.actionLeft_Wink)
        self.menuStart_Stop_Sel.addAction(self.actionRight_Wink)
        self.menuFinger.addAction(self.actionBlink)
        self.menuFinger.addAction(self.actionLeft_Wink)
        self.menuFinger.addAction(self.actionRight_Wink)
        self.menuLetter_Sel.addAction(self.actionBlink_2)
        self.menuLetter_Sel.addAction(self.actionLeft_Wink_2)
        self.menuLetter_Sel.addAction(self.actionRight_Wink_2)
        self.menuSettings.addAction(self.menuStart_Stop_Sel.menuAction())
        self.menuSettings.addAction(self.menuLetter_Sel.menuAction())
        self.menuSettings.addAction(self.menuFinger.menuAction())
        self.menuSettings.addSeparator()
        self.menuHelp.addAction(self.actionAbout_EyeTotText)
        self.menuHelp.addAction(self.actionContact_Developer)
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.buts=[[self.pushButton], [self.textBrowser, self.pushButton]]
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\" bgcolor=\"#f0f0f0\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Emergency</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Food</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Water</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Restroom</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:24pt;\">Fan</span></p></body></html>", None))
        
        
    def changeColour(self):
        global letRowBold
        global letColCount
        global letRowCount
        global stopRow
        if self.go:
            if(stopRow==False):
                letRowCount+=1
                if letRowCount==(len(letRowBold)):
                    letRowCount=0
                if letRowCount<5:
                    self.textBrowser.setHtml(_translate("MainWindow",letRowBold[letRowCount], None))
                    for row in self.buts:
                        for but in row:
                            but.setStyleSheet('QPushButton {font-weight:normal; QTextBrowser {font-weight:normal;}}')
                
            
    def pushSentenceToBody(self):
        global currentSentence
        global wholeText
        if currentSentence!="":
            print(currentSentence)
        self.textBrowser_2.setText(wholeText)
        self.textBrowser_4.setText(currentSentence)
        self.predictNextWord()
    def delLet(self):
        global currentSentence
        currentSentence=currentSentence[0:-1]
        self.textBrowser_4.setText(currentSentence)
        self.predictNextWord()
    def addSpace(self):
        global currentSentence
        currentSentence+=" "
        self.textBrowser_4.setText(currentSentence)
        self.predictNextWord()
    def reciteBut(self):
        self.pushSentenceToBody()
        global wholeText
        reciteLine=wholeText.replace("<br>", "")
        engine.say(reciteLine)
        engine.runAndWait()
    def nurseBut(self):
        global wholeText
        reciteLine=wholeText.replace("<br>", "")
        sendSMS.send(reciteLine)
        print("Nurse")
    def pauseBut(self):
        global letRowCount
        global letColCount
        self.go=not(self.go)
        if letRowCount==6:
            letRowCount=-1
            letColCount=-1
    def predictNextWord(self):
        global currentSentence
        words=currentSentence.lower().split(" ")
        if words:
            if words[0]=="":
                self.textBrowser_3.setText(_translate("MainWindow", "", None))
            elif words[-1]=="":
                predWord=autocomplete.predict('', words[-2])
                if predWord:
                    predWord=predWord[0][0]
                    self.textBrowser_3.setText(_translate("MainWindow", predWord, None))
                    self.textBrowser_3.setAlignment(QtCore.Qt.AlignCenter)
                else:
                    self.textBrowser_3.setText(_translate("MainWindow", "", None))
                    self.textBrowser_3.setAlignment(QtCore.Qt.AlignCenter)
            else:
                predWord=autocomplete.predict(words[-1], '')
                if predWord:
                    predWord=predWord[0][0]
                    self.textBrowser_3.setText(_translate("MainWindow", predWord, None))
                    self.textBrowser_3.setAlignment(QtCore.Qt.AlignCenter)
                else:
                    self.textBrowser_3.setText(_translate("MainWindow", "", None))
                    self.textBrowser_3.setAlignment(QtCore.Qt.AlignCenter)
    def getPredWord(self):
        global currentSentence
        predWord=self.textBrowser_3.toPlainText()
        predWord=str(predWord)
        if currentSentence and predWord:
            words=currentSentence.split(" ")
            if len(words)==1:
                words[0]=predWord.title()
            else:
                words[-1]=predWord
            currentSentence=" ".join(words)+" "
            self.textBrowser_4.setText(currentSentence)
    def openCam(self):
        print("hi")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.aboutToQuit.connect(close)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    row5={0:ui.pauseBut, 1:ui.addSpace, 2:ui.delLet}
    row6={0:ui.getPredWord, 1:ui.nurseBut}
    MainWindow.show()
    timer = QTimer()
    timer.timeout.connect(tick)
    timer.start(100)
    timerColour = QTimer()
    timerColour.timeout.connect(ui.changeColour)
    timerColour.start(1000)
    sys.exit(app.exec_())
