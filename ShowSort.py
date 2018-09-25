#!/usr/bin/env python3

import sys
from PyQt4 import QtCore,QtGui
from Resources.ShowSortGUI import Ui_Form as MainUI
from Resources.ShowSort_About import Ui_Form as AboutUI
from Resources.ShowSort_Help import Ui_helpDock as HelpUI

class Main(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = MainUI()
        self.ui.setupUi(self)

class About(QtGui.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = AboutUI()
        self.ui.setupUi(self)

class Help(QtGui.QDockWidget):
    def __init__(self):
        super().__init__()
        self.ui = HelpUI()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWin = Main()
    mainWin.show()
    aboutWin = About()
    helpWin = Help()
    mainWin.ui.aboutBtn.clicked.connect(aboutWin.show)
    mainWin.ui.helpBtn.clicked.connect(helpWin.show)
    sys.exit(app.exec_())