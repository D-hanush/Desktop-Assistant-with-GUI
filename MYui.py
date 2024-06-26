# from PyQt5 import QtCore, QtGui, QtWidgets
# import os

# class Ui_Myui(object):
#     def setupUi(self, Myui):
#         Myui.setObjectName("Myui")
#         Myui.resize(1008, 790)
#         self.centralwidget = QtWidgets.QWidget(Myui)
#         self.centralwidget.setObjectName("centralwidget")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         self.label.setGeometry(QtCore.QRect(10, 0, 991, 781))
#         self.label.setText("")
        
#         # Use raw strings to handle backslashes
#         loading_gif_path = r"C:\Users\HP\Music\DellaGUI\Loading.gif"
#         if os.path.exists(loading_gif_path):
#             self.movie = QtGui.QMovie(loading_gif_path)
#             self.label.setMovie(self.movie)
#             self.movie.start()
#         else:
#             print(f"Image not found: {loading_gif_path}")

#         self.label.setScaledContents(True)
#         self.label.setObjectName("label")
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(760, 680, 91, 31))
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.pushButton.setFont(font)
#         self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
#         self.pushButton.setObjectName("pushButton")
#         self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton_2.setGeometry(QtCore.QRect(860, 680, 91, 31))
#         font = QtGui.QFont()
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.pushButton_2.setFont(font)
#         self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
#         self.pushButton_2.setObjectName("pushButton_2")
#         self.label_2 = QtWidgets.QLabel(self.centralwidget)
#         self.label_2.setGeometry(QtCore.QRect(20, 690, 721, 71))
#         self.label_2.setText("")

#         # Use raw strings to handle backslashes
#         newwave_gif_path = r"C:\Users\HP\Music\DellaGUI\ios.gif"
#         if os.path.exists(newwave_gif_path):
#             self.movie2 = QtGui.QMovie(newwave_gif_path)
#             self.label_2.setMovie(self.movie2)
#             self.movie2.start()
#         else:
#             print(f"Image not found: {newwave_gif_path}")

#         self.label_2.setObjectName("label_2")
#         Myui.setCentralWidget(self.centralwidget)

#         self.retranslateUi(Myui)
#         QtCore.QMetaObject.connectSlotsByName(Myui)

#     def retranslateUi(self, Myui):
#         _translate = QtCore.QCoreApplication.translate
#         Myui.setWindowTitle(_translate("Myui", "MainWindow"))
#         self.pushButton.setText(_translate("Myui", "RUN"))
#         self.pushButton_2.setText(_translate("Myui", "EXIT"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     Myui = QtWidgets.QMainWindow()
#     ui = Ui_Myui()
#     ui.setupUi(Myui)
#     Myui.show()
#     sys.exit(app.exec_())

from PyQt5 import QtCore, QtGui, QtWidgets
import os

class Ui_Myui(object):
    def setupUi(self, Myui):
        Myui.setObjectName("Myui")
        Myui.resize(1008, 790)
        self.centralwidget = QtWidgets.QWidget(Myui)
        self.centralwidget.setObjectName("centralwidget")
        
        # Setup main loading gif
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 991, 781))
        self.label.setText("")
        
        # Use raw strings to handle backslashes
        loading_gif_path = r"C:\Users\HP\Music\DellaGUI\Loading.gif"
        if os.path.exists(loading_gif_path):
            self.movie = QtGui.QMovie(loading_gif_path)
            self.label.setMovie(self.movie)
            self.movie.start()
        else:
            print(f"Image not found: {loading_gif_path}")

        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        # Setup buttons
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(760, 680, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.pushButton.setObjectName("pushButton")
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 680, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        
        # Setup hidden gif for ios
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 690, 721, 71))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.setVisible(False)  # Hide initially
        
        newwave_gif_path = r"C:\Users\HP\Music\DellaGUI\ios.gif"
        if os.path.exists(newwave_gif_path):
            self.movie2 = QtGui.QMovie(newwave_gif_path)
            self.label_2.setMovie(self.movie2)
        else:
            print(f"Image not found: {newwave_gif_path}")

        Myui.setCentralWidget(self.centralwidget)

        self.retranslateUi(Myui)
        QtCore.QMetaObject.connectSlotsByName(Myui)
        
        # Connect buttons to functions
        self.pushButton.clicked.connect(self.run_button_clicked)
        self.pushButton_2.clicked.connect(Myui.close)

    def retranslateUi(self, Myui):
        _translate = QtCore.QCoreApplication.translate
        Myui.setWindowTitle(_translate("Myui", "MainWindow"))
        self.pushButton.setText(_translate("Myui", "RUN"))
        self.pushButton_2.setText(_translate("Myui", "EXIT"))
        
    def run_button_clicked(self):
        self.label_2.setVisible(True)  # Show the gif
        self.movie2.start()  # Start the gif animation


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Myui = QtWidgets.QMainWindow()
    ui = Ui_Myui()
    ui.setupUi(Myui)
    Myui.show()
    sys.exit(app.exec_())
