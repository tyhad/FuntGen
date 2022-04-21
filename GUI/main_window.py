import sys
import main_window_gui

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMessageBox, QFileDialog, QLineEdit

from helper import show_message_dialog


class MainApp(QtWidgets.QMainWindow, main_window_gui.Ui_MainWindow):
    formula = ""
    results = 0
    list_of_wave = []

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)

        self.btn_num_0.clicked.connect(self.func_btn_num_0)
        self.btn_num_1.clicked.connect(self.func_btn_num_1)
        self.btn_num_2.clicked.connect(self.func_btn_num_2)
        self.btn_num_3.clicked.connect(self.func_btn_num_3)
        self.btn_num_4.clicked.connect(self.func_btn_num_4)
        self.btn_num_5.clicked.connect(self.func_btn_num_5)
        self.btn_num_6.clicked.connect(self.func_btn_num_6)
        self.btn_num_7.clicked.connect(self.func_btn_num_7)
        self.btn_num_8.clicked.connect(self.func_btn_num_8)
        self.btn_num_9.clicked.connect(self.func_btn_num_9)

        self.btn_add.clicked.connect(self.func_btn_opr_add)

        self.btn_submit.clicked.connect(self.func_btn_opr_submit)

    def set_formula(self, key: str):
        self.formula = self.formula + key
        self.le_formula_box.setText(self.formula)

    def func_btn_num_0(self):
        self.set_formula("0")

    def func_btn_num_1(self):
        self.set_formula("1")

    def func_btn_num_2(self):
        self.set_formula("2")

    def func_btn_num_3(self):
        self.set_formula("3")

    def func_btn_num_4(self):
        self.set_formula("4")

    def func_btn_num_5(self):
        self.set_formula("5")

    def func_btn_num_6(self):
        self.set_formula("6")

    def func_btn_num_7(self):
        self.set_formula("7")

    def func_btn_num_8(self):
        self.set_formula("8")

    def func_btn_num_9(self):
        self.set_formula("9")

    def func_btn_opr_add(self):
        self.set_formula("+")

#     =======================
    def func_btn_opr_submit(self):
        self.list_of_wave.clear()
        for i in range(1, 300 + 1):
            self.list_of_wave.append(i)

        show_message_dialog(self.list_of_wave)






def main():
    app = QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
