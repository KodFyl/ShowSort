from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_helpDock(object):
    def setupUi(self, helpDock):
        helpDock.setObjectName(_fromUtf8("helpDock"))
        helpDock.resize(592, 425)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(helpDock.sizePolicy().hasHeightForWidth())
        helpDock.setSizePolicy(sizePolicy)
        helpDock.setMinimumSize(QtCore.QSize(592, 425))
        helpDock.setMaximumSize(QtCore.QSize(592, 425))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nimbus Roman No9 L"))
        font.setPointSize(12)
        helpDock.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons8-retro-tv-90.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        helpDock.setWindowIcon(icon)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.tabWidget = QtGui.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setGeometry(QtCore.QRect(10, -1, 571, 361))
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.patternTab = QtGui.QWidget()
        self.patternTab.setObjectName(_fromUtf8("patternTab"))
        self.label = QtGui.QLabel(self.patternTab)
        self.label.setGeometry(QtCore.QRect(10, 10, 571, 301))
        self.label.setObjectName(_fromUtf8("label"))
        self.tabWidget.addTab(self.patternTab, _fromUtf8(""))
        self.searchDirTab = QtGui.QWidget()
        self.searchDirTab.setObjectName(_fromUtf8("searchDirTab"))
        self.label_3 = QtGui.QLabel(self.searchDirTab)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 571, 301))
        self.label_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.addTab(self.searchDirTab, _fromUtf8(""))
        self.targetDirTab = QtGui.QWidget()
        self.targetDirTab.setObjectName(_fromUtf8("targetDirTab"))
        self.label_4 = QtGui.QLabel(self.targetDirTab)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 571, 301))
        self.label_4.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.tabWidget.addTab(self.targetDirTab, _fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.dockWidgetContents)
        self.label_2.setGeometry(QtCore.QRect(10, 370, 571, 20))
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        helpDock.setWidget(self.dockWidgetContents)

        self.retranslateUi(helpDock)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(helpDock)

    def retranslateUi(self, helpDock):
        helpDock.setWindowTitle(_translate("helpDock", "Help Sort.", None))
        self.label.setText(_translate("helpDock", "Pattern represents the format of files to be searched.\n"
"\n"
"Usage: filename(season-identifier)(episode-identifier)\n"
"\n"
"? filename:  This represents any characters which repeats in all the files.\n"
"? season-identifier: This is usually a number representing the season. This varies with \n"
"each files and thus in pattern, each of this characters are represented with a \"*\" and \n"
"enclosed in brackets.\n"
"? episode-identifier: This is usually a number representing the season. This varies with \n"
"each files and thus in pattern, each of this characters are represented with a \"*\" and \n"
"enclosed in brackets.\n"
"\n"
"Eg: To match a file \"Game of Thrones S08E01\", use pattern \n"
"\"Game of Thrones S(**)E(**)\".\n"
"\n"
"Remember, patterns are case-sensitive.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.patternTab), _translate("helpDock", "Pattern", None))
        self.label_3.setText(_translate("helpDock", "Search Directory specifies the path where search operation is to be perfomed. \n"
"This directory should contain the files that is to be sorted\n"
"\n"
"\n"
"If \"Present Directory\" is checked, the search is perfomed in the directory where the \n"
"Show Sort tool is run. Otherwise, uncheck the \"Present Directory\" and browse for \n"
"search directory manually.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.searchDirTab), _translate("helpDock", "Search Directory", None))
        self.label_4.setText(_translate("helpDock", "Target Directory specifies the path where after the soting operation, the files are to be \n"
"stored. This directory contains the sorted files.\n"
"\n"
"\n"
"If \"Present Directory\" is checked, the files will be stored in the directory where the \n"
"Show Sort tool is run. Otherwise, uncheck the \"Present Directory\" and browse for \n"
"target directory manually.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.targetDirTab), _translate("helpDock", "Target Directory", None))
        self.label_2.setText(_translate("helpDock", "For more info, visit <a href=\"http://showsort.wordpress.com\">showsort.wordpress.com</a>", None))

import Resources.ShowSortResources_rc
