# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\pjjoyce\Dropbox\00_My_Software\futura\futura_ui\app\ui\ui_files\actions.ui',
# licensing of 'C:\Users\pjjoyce\Dropbox\00_My_Software\futura\futura_ui\app\ui\ui_files\actions.ui' applies.
#
# Created: Fri Dec 13 12:59:03 2019
#      by: pyside2-uic  running on PySide2 5.13.1
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_ActionsWidget(object):
    def setupUi(self, ActionsWidget):
        ActionsWidget.setObjectName("ActionsWidget")
        ActionsWidget.resize(1341, 737)
        self.gridLayout_7 = QtWidgets.QGridLayout(ActionsWidget)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.fileFrame = QtWidgets.QFrame(ActionsWidget)
        self.fileFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fileFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fileFrame.setObjectName("fileFrame")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.fileFrame)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.fileFrame)
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.newButton = QtWidgets.QPushButton(self.fileFrame)
        self.newButton.setMinimumSize(QtCore.QSize(100, 100))
        self.newButton.setMaximumSize(QtCore.QSize(100, 100))
        self.newButton.setBaseSize(QtCore.QSize(50, 50))
        self.newButton.setObjectName("newButton")
        self.horizontalLayout_6.addWidget(self.newButton)
        self.loadButton = QtWidgets.QPushButton(self.fileFrame)
        self.loadButton.setMinimumSize(QtCore.QSize(100, 100))
        self.loadButton.setMaximumSize(QtCore.QSize(100, 100))
        self.loadButton.setBaseSize(QtCore.QSize(50, 50))
        self.loadButton.setObjectName("loadButton")
        self.horizontalLayout_6.addWidget(self.loadButton)
        self.line = QtWidgets.QFrame(self.fileFrame)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout_6.addWidget(self.line)
        self.loaderButton = QtWidgets.QPushButton(self.fileFrame)
        self.loaderButton.setMinimumSize(QtCore.QSize(100, 100))
        self.loaderButton.setMaximumSize(QtCore.QSize(100, 100))
        self.loaderButton.setBaseSize(QtCore.QSize(50, 50))
        self.loaderButton.setObjectName("loaderButton")
        self.horizontalLayout_6.addWidget(self.loaderButton)
        self.saveLoaderButton = QtWidgets.QPushButton(self.fileFrame)
        self.saveLoaderButton.setMinimumSize(QtCore.QSize(100, 100))
        self.saveLoaderButton.setMaximumSize(QtCore.QSize(100, 100))
        self.saveLoaderButton.setObjectName("saveLoaderButton")
        self.horizontalLayout_6.addWidget(self.saveLoaderButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.gridLayout_6.addLayout(self.verticalLayout_6, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.fileFrame, 0, 0, 1, 1)
        self.databaseFrame = QtWidgets.QFrame(ActionsWidget)
        self.databaseFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.databaseFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.databaseFrame.setObjectName("databaseFrame")
        self.gridLayout = QtWidgets.QGridLayout(self.databaseFrame)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.databaseFrame)
        self.label.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.baseDatabaseButton = QtWidgets.QPushButton(self.databaseFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baseDatabaseButton.sizePolicy().hasHeightForWidth())
        self.baseDatabaseButton.setSizePolicy(sizePolicy)
        self.baseDatabaseButton.setMinimumSize(QtCore.QSize(100, 100))
        self.baseDatabaseButton.setMaximumSize(QtCore.QSize(100, 100))
        self.baseDatabaseButton.setBaseSize(QtCore.QSize(50, 50))
        self.baseDatabaseButton.setObjectName("baseDatabaseButton")
        self.horizontalLayout.addWidget(self.baseDatabaseButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.databaseFrame, 0, 1, 1, 1)
        self.technologyFrame = QtWidgets.QFrame(ActionsWidget)
        self.technologyFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.technologyFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.technologyFrame.setObjectName("technologyFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.technologyFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.technologyFrame)
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.technologyFileButton = QtWidgets.QPushButton(self.technologyFrame)
        self.technologyFileButton.setMinimumSize(QtCore.QSize(100, 100))
        self.technologyFileButton.setMaximumSize(QtCore.QSize(100, 100))
        self.technologyFileButton.setBaseSize(QtCore.QSize(50, 50))
        self.technologyFileButton.setObjectName("technologyFileButton")
        self.horizontalLayout_2.addWidget(self.technologyFileButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.technologyFrame, 1, 0, 1, 1)
        self.marketsFrame = QtWidgets.QFrame(ActionsWidget)
        self.marketsFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.marketsFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.marketsFrame.setObjectName("marketsFrame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.marketsFrame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.marketsFrame)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.marketsButton = QtWidgets.QPushButton(self.marketsFrame)
        self.marketsButton.setMinimumSize(QtCore.QSize(100, 100))
        self.marketsButton.setMaximumSize(QtCore.QSize(100, 100))
        self.marketsButton.setBaseSize(QtCore.QSize(50, 50))
        self.marketsButton.setObjectName("marketsButton")
        self.horizontalLayout_4.addWidget(self.marketsButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.gridLayout_4.addLayout(self.verticalLayout_4, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.marketsFrame, 1, 1, 1, 1)
        self.regionalisationFrame = QtWidgets.QFrame(ActionsWidget)
        self.regionalisationFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.regionalisationFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.regionalisationFrame.setObjectName("regionalisationFrame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.regionalisationFrame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.regionalisationFrame)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.regionaliseButton = QtWidgets.QPushButton(self.regionalisationFrame)
        self.regionaliseButton.setMinimumSize(QtCore.QSize(100, 100))
        self.regionaliseButton.setMaximumSize(QtCore.QSize(100, 100))
        self.regionaliseButton.setBaseSize(QtCore.QSize(50, 50))
        self.regionaliseButton.setObjectName("regionaliseButton")
        self.horizontalLayout_3.addWidget(self.regionaliseButton)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.regionalisationFrame, 2, 0, 1, 1)
        self.exportFrame = QtWidgets.QFrame(ActionsWidget)
        self.exportFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.exportFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.exportFrame.setObjectName("exportFrame")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.exportFrame)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.exportFrame)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 25))
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.exportButton = QtWidgets.QPushButton(self.exportFrame)
        self.exportButton.setMinimumSize(QtCore.QSize(100, 100))
        self.exportButton.setMaximumSize(QtCore.QSize(100, 100))
        self.exportButton.setBaseSize(QtCore.QSize(50, 50))
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout_5.addWidget(self.exportButton)
        self.exportBrightwayButton = QtWidgets.QPushButton(self.exportFrame)
        self.exportBrightwayButton.setMinimumSize(QtCore.QSize(100, 100))
        self.exportBrightwayButton.setMaximumSize(QtCore.QSize(100, 100))
        self.exportBrightwayButton.setObjectName("exportBrightwayButton")
        self.horizontalLayout_5.addWidget(self.exportBrightwayButton)
        self.testButton = QtWidgets.QPushButton(self.exportFrame)
        self.testButton.setMinimumSize(QtCore.QSize(100, 100))
        self.testButton.setMaximumSize(QtCore.QSize(100, 100))
        self.testButton.setObjectName("testButton")
        self.horizontalLayout_5.addWidget(self.testButton)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.gridLayout_5.addLayout(self.verticalLayout_5, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.exportFrame, 2, 1, 1, 1)

        self.retranslateUi(ActionsWidget)
        QtCore.QMetaObject.connectSlotsByName(ActionsWidget)

    def retranslateUi(self, ActionsWidget):
        ActionsWidget.setWindowTitle(QtWidgets.QApplication.translate("ActionsWidget", "Form", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("ActionsWidget", "File", None, -1))
        self.newButton.setText(QtWidgets.QApplication.translate("ActionsWidget", "New Recipe", None, -1))
        self.loadButton.setText(QtWidgets.QApplication.translate("ActionsWidget", "Open Recipe", None, -1))
        self.loaderButton.setText(QtWidgets.QApplication.translate("ActionsWidget", "Open saved\n"
"workspace", None, -1))
        self.saveLoaderButton.setText(QtWidgets.QApplication.translate("ActionsWidget", "Save\n"
"workspace", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("ActionsWidget", "Databases", None, -1))
        self.baseDatabaseButton.setText(QtWidgets.QApplication.translate("ActionsWidget", "Add base\n"
"database", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("ActionsWidget", "Technology", None, -1))
        self.technologyFileButton.setText(QtWidgets.QApplication.translate("ActionsWidget", "Add technology", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("ActionsWidget", "Markets", None, -1))
        self.marketsButton.setText(QtWidgets.QApplication.translate("ActionsWidget", "Alter markets", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("ActionsWidget", "Regionalisation", None, -1))
        self.regionaliseButton.setText(QtWidgets.QApplication.translate("ActionsWidget", "Regionalise", None, -1))
        self.label_5.setText(QtWidgets.QApplication.translate("ActionsWidget", "Export", None, -1))
        self.exportButton.setText(QtWidgets.QApplication.translate("ActionsWidget", "Export current\n"
"recipe", None, -1))
        self.exportBrightwayButton.setText(QtWidgets.QApplication.translate("ActionsWidget", "Export database\n"
"to Brightway2", None, -1))
        self.testButton.setText(QtWidgets.QApplication.translate("ActionsWidget", "Test Button", None, -1))

