# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(680, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMaximumSize(QtCore.QSize(1677215, 16777215))
        self.tabWidget.setAutoFillBackground(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.seqSpin = QtWidgets.QSpinBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.seqSpin.sizePolicy().hasHeightForWidth())
        self.seqSpin.setSizePolicy(sizePolicy)
        self.seqSpin.setObjectName("seqSpin")
        self.gridLayout_3.addWidget(self.seqSpin, 2, 5, 1, 1)
        self.newTrackButton = QtWidgets.QPushButton(self.tab)
        self.newTrackButton.setObjectName("newTrackButton")
        self.gridLayout_3.addWidget(self.newTrackButton, 0, 7, 1, 1)
        self.sizeCombo = QtWidgets.QComboBox(self.tab)
        self.sizeCombo.setObjectName("sizeCombo")
        self.gridLayout_3.addWidget(self.sizeCombo, 1, 7, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 1, 6, 1, 1)
        self.disciplineCombo = QtWidgets.QComboBox(self.tab)
        self.disciplineCombo.setObjectName("disciplineCombo")
        self.gridLayout_3.addWidget(self.disciplineCombo, 1, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 8, 7, 1, 1)
        self.statusCombo = QtWidgets.QComboBox(self.tab)
        self.statusCombo.setObjectName("statusCombo")
        self.gridLayout_3.addWidget(self.statusCombo, 6, 7, 1, 1)
        self.author = QtWidgets.QLineEdit(self.tab)
        self.author.setObjectName("author")
        self.gridLayout_3.addWidget(self.author, 5, 7, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 5, 6, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 6, 6, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 4, 1, 1)
        self.revSpin = QtWidgets.QSpinBox(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.revSpin.sizePolicy().hasHeightForWidth())
        self.revSpin.setSizePolicy(sizePolicy)
        self.revSpin.setObjectName("revSpin")
        self.gridLayout_3.addWidget(self.revSpin, 2, 7, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 2, 6, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 2, 4, 1, 1)
        self.trackListCombo = QtWidgets.QComboBox(self.tab)
        self.trackListCombo.setObjectName("trackListCombo")
        self.gridLayout_3.addWidget(self.trackListCombo, 0, 0, 1, 4)
        self.label_5 = QtWidgets.QLabel(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 3, 4, 1, 1)
        self.description = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.description.sizePolicy().hasHeightForWidth())
        self.description.setSizePolicy(sizePolicy)
        self.description.setObjectName("description")
        self.gridLayout_3.addWidget(self.description, 4, 5, 1, 2)
        self.fileTree = QtWidgets.QTreeView(self.tab)
        self.fileTree.setMinimumSize(QtCore.QSize(300, 0))
        self.fileTree.setObjectName("fileTree")
        self.gridLayout_3.addWidget(self.fileTree, 1, 0, 10, 3)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 1)
        self.FileName = QtWidgets.QLabel(self.tab_2)
        self.FileName.setObjectName("FileName")
        self.gridLayout_2.addWidget(self.FileName, 0, 1, 1, 1)
        self.listView = QtWidgets.QListView(self.tab_2)
        self.listView.setObjectName("listView")
        self.gridLayout_2.addWidget(self.listView, 1, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 680, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.trackListCombo.currentIndexChanged['int'].connect(MainWindow.projectChanged)
        self.newTrackButton.clicked.connect(MainWindow.addProject)
        self.pushButton.clicked.connect(MainWindow.updateFile)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.newTrackButton.setText(_translate("MainWindow", "Add"))
        self.label_2.setText(_translate("MainWindow", "Size"))
        self.pushButton.setText(_translate("MainWindow", "Update Details"))
        self.label_6.setText(_translate("MainWindow", "Author"))
        self.label_7.setText(_translate("MainWindow", "Status"))
        self.label.setText(_translate("MainWindow", "Discipline"))
        self.label_4.setText(_translate("MainWindow", "Rev"))
        self.label_3.setText(_translate("MainWindow", "Document number"))
        self.label_5.setText(_translate("MainWindow", "Description"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.label_8.setText(_translate("MainWindow", "File History"))
        self.FileName.setText(_translate("MainWindow", "File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))

