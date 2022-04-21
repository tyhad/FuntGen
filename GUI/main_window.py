import sys
import main_window_gui

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMessageBox, QFileDialog, QLineEdit


class MainApp(QtWidgets.QMainWindow, main_window_gui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
