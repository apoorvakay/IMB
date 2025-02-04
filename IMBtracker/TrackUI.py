# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrackMain.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1165, 830)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMaximumSize(QtCore.QSize(362, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.trackStartBtn = QtWidgets.QPushButton(self.groupBox)
        self.trackStartBtn.setObjectName("trackStartBtn")
        self.gridLayout_2.addWidget(self.trackStartBtn, 2, 0, 1, 1)
        self.trackProgressBar = QtWidgets.QProgressBar(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.trackProgressBar.sizePolicy().hasHeightForWidth())
        self.trackProgressBar.setSizePolicy(sizePolicy)
        self.trackProgressBar.setMinimumSize(QtCore.QSize(0, 0))
        self.trackProgressBar.setProperty("value", 0)
        self.trackProgressBar.setTextVisible(True)
        self.trackProgressBar.setObjectName("trackProgressBar")
        self.gridLayout_2.addWidget(self.trackProgressBar, 4, 0, 1, 1)
        self.experimentInfoGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.experimentInfoGroupBox.setObjectName("experimentInfoGroupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.experimentInfoGroupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.locationGroupBox = QtWidgets.QGroupBox(self.experimentInfoGroupBox)
        self.locationGroupBox.setObjectName("locationGroupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.locationGroupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.locationVLayout = QtWidgets.QVBoxLayout()
        self.locationVLayout.setObjectName("locationVLayout")
        self.locationHLayout = QtWidgets.QHBoxLayout()
        self.locationHLayout.setObjectName("locationHLayout")
        self.pathLineEdit = QtWidgets.QLineEdit(self.locationGroupBox)
        self.pathLineEdit.setReadOnly(True)
        self.pathLineEdit.setObjectName("pathLineEdit")
        self.locationHLayout.addWidget(self.pathLineEdit)
        self.folderBrowseBtn = QtWidgets.QToolButton(self.locationGroupBox)
        self.folderBrowseBtn.setObjectName("folderBrowseBtn")
        self.locationHLayout.addWidget(self.folderBrowseBtn)
        self.locationVLayout.addLayout(self.locationHLayout)
        self.verticalLayout_2.addLayout(self.locationVLayout)
        self.verticalLayout.addWidget(self.locationGroupBox)
        self.dishSizeGroupBox = QtWidgets.QGroupBox(self.experimentInfoGroupBox)
        self.dishSizeGroupBox.setMinimumSize(QtCore.QSize(300, 80))
        self.dishSizeGroupBox.setObjectName("dishSizeGroupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dishSizeGroupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.bigDishRadioBtn = QtWidgets.QRadioButton(self.dishSizeGroupBox)
        self.bigDishRadioBtn.setChecked(True)
        self.bigDishRadioBtn.setObjectName("bigDishRadioBtn")
        self.verticalLayout_3.addWidget(self.bigDishRadioBtn)
        self.smallDishRadioBtn = QtWidgets.QRadioButton(self.dishSizeGroupBox)
        self.smallDishRadioBtn.setObjectName("smallDishRadioBtn")
        self.verticalLayout_3.addWidget(self.smallDishRadioBtn)
        self.verticalLayout.addWidget(self.dishSizeGroupBox)
        self.gridLayout_2.addWidget(self.experimentInfoGroupBox, 0, 0, 1, 1)
        self.trackingParamsGroupBox = QtWidgets.QGroupBox(self.groupBox)
        self.trackingParamsGroupBox.setObjectName("trackingParamsGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.trackingParamsGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.collisionResGroupBox = QtWidgets.QGroupBox(self.trackingParamsGroupBox)
        self.collisionResGroupBox.setObjectName("collisionResGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.collisionResGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.woColResRadioBtn = QtWidgets.QRadioButton(self.collisionResGroupBox)
        self.woColResRadioBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.woColResRadioBtn.setMaximumSize(QtCore.QSize(320, 16777215))
        self.woColResRadioBtn.setChecked(True)
        self.woColResRadioBtn.setObjectName("woColResRadioBtn")
        self.verticalLayout_4.addWidget(self.woColResRadioBtn)
        self.withColResRadioBtn = QtWidgets.QRadioButton(self.collisionResGroupBox)
        self.withColResRadioBtn.setObjectName("withColResRadioBtn")
        self.verticalLayout_4.addWidget(self.withColResRadioBtn)
        self.verticalLayout_5.addWidget(self.collisionResGroupBox)
        self.frame = QtWidgets.QFrame(self.trackingParamsGroupBox)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.imageProcGroupBox = QtWidgets.QGroupBox(self.frame)
        self.imageProcGroupBox.setObjectName("imageProcGroupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.imageProcGroupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.contrastCheckbox = QtWidgets.QCheckBox(self.imageProcGroupBox)
        self.contrastCheckbox.setObjectName("contrastCheckbox")
        self.gridLayout.addWidget(self.contrastCheckbox, 3, 2, 1, 1)
        self.brightnessCheckbox = QtWidgets.QCheckBox(self.imageProcGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.brightnessCheckbox.sizePolicy().hasHeightForWidth())
        self.brightnessCheckbox.setSizePolicy(sizePolicy)
        self.brightnessCheckbox.setMinimumSize(QtCore.QSize(0, 0))
        self.brightnessCheckbox.setObjectName("brightnessCheckbox")
        self.gridLayout.addWidget(self.brightnessCheckbox, 0, 2, 1, 1)
        self.gammaCheckbox = QtWidgets.QCheckBox(self.imageProcGroupBox)
        self.gammaCheckbox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gammaCheckbox.setObjectName("gammaCheckbox")
        self.gridLayout.addWidget(self.gammaCheckbox, 5, 2, 1, 1)
        self.contrastVal = QtWidgets.QDoubleSpinBox(self.imageProcGroupBox)
        self.contrastVal.setMinimum(0.1)
        self.contrastVal.setMaximum(4.0)
        self.contrastVal.setSingleStep(0.1)
        self.contrastVal.setProperty("value", 1.0)
        self.contrastVal.setObjectName("contrastVal")
        self.gridLayout.addWidget(self.contrastVal, 4, 2, 1, 1)
        self.brightnessVal = QtWidgets.QDoubleSpinBox(self.imageProcGroupBox)
        self.brightnessVal.setDecimals(1)
        self.brightnessVal.setMinimum(-256.0)
        self.brightnessVal.setMaximum(256.0)
        self.brightnessVal.setSingleStep(1.0)
        self.brightnessVal.setObjectName("brightnessVal")
        self.gridLayout.addWidget(self.brightnessVal, 1, 2, 1, 1)
        self.gammaVal = QtWidgets.QDoubleSpinBox(self.imageProcGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gammaVal.sizePolicy().hasHeightForWidth())
        self.gammaVal.setSizePolicy(sizePolicy)
        self.gammaVal.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.gammaVal.setMaximum(4.0)
        self.gammaVal.setSingleStep(0.01)
        self.gammaVal.setProperty("value", 1.0)
        self.gammaVal.setObjectName("gammaVal")
        self.gridLayout.addWidget(self.gammaVal, 6, 2, 1, 1)
        self.horizontalLayout_4.addWidget(self.imageProcGroupBox)
        self.ROIGroupBox = QtWidgets.QGroupBox(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROIGroupBox.sizePolicy().hasHeightForWidth())
        self.ROIGroupBox.setSizePolicy(sizePolicy)
        self.ROIGroupBox.setObjectName("ROIGroupBox")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.ROIGroupBox)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.ROIYspinbox = QtWidgets.QSpinBox(self.ROIGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROIYspinbox.sizePolicy().hasHeightForWidth())
        self.ROIYspinbox.setSizePolicy(sizePolicy)
        self.ROIYspinbox.setMaximum(9999)
        self.ROIYspinbox.setObjectName("ROIYspinbox")
        self.gridLayout_7.addWidget(self.ROIYspinbox, 2, 1, 1, 1)
        self.ROIRspinbox = QtWidgets.QSpinBox(self.ROIGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROIRspinbox.sizePolicy().hasHeightForWidth())
        self.ROIRspinbox.setSizePolicy(sizePolicy)
        self.ROIRspinbox.setMaximum(9999)
        self.ROIRspinbox.setObjectName("ROIRspinbox")
        self.gridLayout_7.addWidget(self.ROIRspinbox, 3, 1, 1, 1)
        self.ROIXspinbox = QtWidgets.QSpinBox(self.ROIGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROIXspinbox.sizePolicy().hasHeightForWidth())
        self.ROIXspinbox.setSizePolicy(sizePolicy)
        self.ROIXspinbox.setMinimumSize(QtCore.QSize(60, 0))
        self.ROIXspinbox.setMaximum(9999)
        self.ROIXspinbox.setObjectName("ROIXspinbox")
        self.gridLayout_7.addWidget(self.ROIXspinbox, 1, 1, 1, 1)
        self.ROIxlbl = QtWidgets.QLabel(self.ROIGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROIxlbl.sizePolicy().hasHeightForWidth())
        self.ROIxlbl.setSizePolicy(sizePolicy)
        self.ROIxlbl.setMinimumSize(QtCore.QSize(0, 0))
        self.ROIxlbl.setObjectName("ROIxlbl")
        self.gridLayout_7.addWidget(self.ROIxlbl, 1, 0, 1, 1)
        self.ROIylbl = QtWidgets.QLabel(self.ROIGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROIylbl.sizePolicy().hasHeightForWidth())
        self.ROIylbl.setSizePolicy(sizePolicy)
        self.ROIylbl.setObjectName("ROIylbl")
        self.gridLayout_7.addWidget(self.ROIylbl, 2, 0, 1, 1)
        self.ROIcheckbox = QtWidgets.QCheckBox(self.ROIGroupBox)
        self.ROIcheckbox.setObjectName("ROIcheckbox")
        self.gridLayout_7.addWidget(self.ROIcheckbox, 0, 0, 1, 2)
        self.ROIrlbl = QtWidgets.QLabel(self.ROIGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ROIrlbl.sizePolicy().hasHeightForWidth())
        self.ROIrlbl.setSizePolicy(sizePolicy)
        self.ROIrlbl.setObjectName("ROIrlbl")
        self.gridLayout_7.addWidget(self.ROIrlbl, 3, 0, 1, 1)
        self.horizontalLayout_4.addWidget(self.ROIGroupBox)
        self.verticalLayout_5.addWidget(self.frame)
        self.outputGroupBox = QtWidgets.QGroupBox(self.trackingParamsGroupBox)
        self.outputGroupBox.setObjectName("outputGroupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.outputGroupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.outputPathLineEdit = QtWidgets.QLineEdit(self.outputGroupBox)
        self.outputPathLineEdit.setReadOnly(True)
        self.outputPathLineEdit.setObjectName("outputPathLineEdit")
        self.gridLayout_5.addWidget(self.outputPathLineEdit, 0, 0, 1, 1)
        self.outputFolderBrowseBtn = QtWidgets.QToolButton(self.outputGroupBox)
        self.outputFolderBrowseBtn.setObjectName("outputFolderBrowseBtn")
        self.gridLayout_5.addWidget(self.outputFolderBrowseBtn, 0, 1, 1, 1)
        self.outputAppendCheckBox = QtWidgets.QCheckBox(self.outputGroupBox)
        self.outputAppendCheckBox.setObjectName("outputAppendCheckBox")
        self.gridLayout_5.addWidget(self.outputAppendCheckBox, 1, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.outputGroupBox)
        self.gridLayout_2.addWidget(self.trackingParamsGroupBox, 1, 0, 1, 1)
        self.trackCancelBtn = QtWidgets.QPushButton(self.groupBox)
        self.trackCancelBtn.setEnabled(False)
        self.trackCancelBtn.setObjectName("trackCancelBtn")
        self.gridLayout_2.addWidget(self.trackCancelBtn, 3, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBox)
        self.resultsTabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.resultsTabWidget.setObjectName("resultsTabWidget")
        self.experimentsTab = QtWidgets.QWidget()
        self.experimentsTab.setObjectName("experimentsTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.experimentsTab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.tableView = QtWidgets.QTableView(self.experimentsTab)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.gridLayout_3.addWidget(self.tableView, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.experimentsTab)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnSelectAll = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSelectAll.setObjectName("btnSelectAll")
        self.horizontalLayout_3.addWidget(self.btnSelectAll)
        self.btnSelectNone = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSelectNone.setObjectName("btnSelectNone")
        self.horizontalLayout_3.addWidget(self.btnSelectNone)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.gridLayout_3.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.resultsTabWidget.addTab(self.experimentsTab, "")
        self.imgProcTab = QtWidgets.QWidget()
        self.imgProcTab.setObjectName("imgProcTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.imgProcTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frameShowScrollArea = QtWidgets.QScrollArea(self.imgProcTab)
        self.frameShowScrollArea.setWidgetResizable(True)
        self.frameShowScrollArea.setObjectName("frameShowScrollArea")
        self.frameShowWidget = QtWidgets.QWidget()
        self.frameShowWidget.setGeometry(QtCore.QRect(0, 0, 715, 680))
        self.frameShowWidget.setObjectName("frameShowWidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frameShowWidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.frameShowLbl = QtWidgets.QLabel(self.frameShowWidget)
        self.frameShowLbl.setText("")
        self.frameShowLbl.setScaledContents(False)
        self.frameShowLbl.setObjectName("frameShowLbl")
        self.gridLayout_6.addWidget(self.frameShowLbl, 0, 0, 1, 1)
        self.frameShowScrollArea.setWidget(self.frameShowWidget)
        self.gridLayout_4.addWidget(self.frameShowScrollArea, 0, 0, 1, 1)
        self.zoomCheckbox = QtWidgets.QCheckBox(self.imgProcTab)
        self.zoomCheckbox.setObjectName("zoomCheckbox")
        self.gridLayout_4.addWidget(self.zoomCheckbox, 1, 0, 1, 1)
        self.resultsTabWidget.addTab(self.imgProcTab, "")
        self.horizontalLayout.addWidget(self.resultsTabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1165, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.resultsTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Larvae Track"))
        self.groupBox.setTitle(_translate("MainWindow", "Tracking"))
        self.trackStartBtn.setText(_translate("MainWindow", "Track!!"))
        self.experimentInfoGroupBox.setTitle(_translate("MainWindow", "Experiment Info"))
        self.locationGroupBox.setTitle(_translate("MainWindow", "Location"))
        self.folderBrowseBtn.setText(_translate("MainWindow", "..."))
        self.dishSizeGroupBox.setTitle(_translate("MainWindow", "Dish Size"))
        self.bigDishRadioBtn.setText(_translate("MainWindow", "15 cm (Large)"))
        self.smallDishRadioBtn.setText(_translate("MainWindow", "9cm (Normal)"))
        self.trackingParamsGroupBox.setTitle(_translate("MainWindow", "Tracking Parameters"))
        self.collisionResGroupBox.setTitle(_translate("MainWindow", "Collision Resolution:"))
        self.woColResRadioBtn.setText(_translate("MainWindow", "No collision resolution (Paisios et al. 2017)"))
        self.withColResRadioBtn.setText(_translate("MainWindow", "With collision resolution"))
        self.imageProcGroupBox.setTitle(_translate("MainWindow", "Image processing:"))
        self.contrastCheckbox.setText(_translate("MainWindow", "Contrast"))
        self.brightnessCheckbox.setText(_translate("MainWindow", "Brightness"))
        self.gammaCheckbox.setText(_translate("MainWindow", "Gamma"))
        self.ROIGroupBox.setTitle(_translate("MainWindow", "Region of Interest"))
        self.ROIxlbl.setText(_translate("MainWindow", "X:"))
        self.ROIylbl.setText(_translate("MainWindow", "Y:"))
        self.ROIcheckbox.setText(_translate("MainWindow", "Specify ROI"))
        self.ROIrlbl.setText(_translate("MainWindow", "R:"))
        self.outputGroupBox.setTitle(_translate("MainWindow", "Output Location"))
        self.outputFolderBrowseBtn.setText(_translate("MainWindow", "..."))
        self.outputAppendCheckBox.setText(_translate("MainWindow", "Append to folder"))
        self.trackCancelBtn.setText(_translate("MainWindow", "Cancel"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Manage Selection"))
        self.btnSelectAll.setText(_translate("MainWindow", "Select All"))
        self.btnSelectNone.setText(_translate("MainWindow", "Select None"))
        self.resultsTabWidget.setTabText(self.resultsTabWidget.indexOf(self.experimentsTab), _translate("MainWindow", "Experiments"))
        self.zoomCheckbox.setText(_translate("MainWindow", "Actual Size"))
        self.resultsTabWidget.setTabText(self.resultsTabWidget.indexOf(self.imgProcTab), _translate("MainWindow", "Image Processing"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

