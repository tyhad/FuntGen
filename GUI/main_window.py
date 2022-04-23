import sys
import main_window_gui

from math import sin, cos, tan, pi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication


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
        self.btn_substraction.clicked.connect(self.func_btn_opr_subs)
        self.btn_multiplication.clicked.connect(self.func_btn_opr_mul)
        self.btn_divide.clicked.connect(self.func_btn_opr_div)
        self.btn_cos.clicked.connect(self.func_btn_opr_cos)
        self.btn_sin.clicked.connect(self.func_btn_opr_sin)
        self.btn_tan.clicked.connect(self.func_btn_opr_tan)
        self.btn_close_bracket.clicked.connect(self.func_btn_opr_close_bracket)
        self.btn_open_bracket.clicked.connect(self.func_btn_opr_open_bracket)
        self.btn_pi.clicked.connect(self.func_btn_opr_pi)

        self.btn_equal.clicked.connect(self.func_btn_opr_equal)

    def set_formula(self, key: str):
        self.formula = self.le_formula_box.text()
        self.current_cursor = self.le_formula_box.cursorPosition()
        self.formula = self.formula[:self.current_cursor] + key + self.formula[self.current_cursor:]
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

    def func_btn_opr_subs(self):
        self.set_formula("-")

    def func_btn_opr_mul(self):
        self.set_formula("*")

    def func_btn_opr_div(self):
        self.set_formula("/")

    def func_btn_opr_cos(self):
        self.set_formula("cos")

    def func_btn_opr_sin(self):
        self.set_formula("sin")

    def func_btn_opr_tan(self):
        self.set_formula("tan")

    def func_btn_opr_open_bracket(self):
        self.set_formula("(")

    def func_btn_opr_close_bracket(self):
        self.set_formula(")")

    def func_btn_opr_pi(self):
        self.set_formula("pi")

    def func_btn_opr_comma(self):
        self.set_formula(".")

    def func_btn_opr_equal(self):
        self.list_of_wave.clear()
        self.evaluate_formula()
        print(self.list_of_wave)

    def evaluate_formula(self):
        formula = self.le_formula_box.text()
        t = 0.01
        form = formula.split("*")[1]
        idx = form.find("(")
        freq = int(form[idx + 1:])
        d = int((2*pi/freq) / t)

        for i in range(0, d):
            result = eval(formula)
            self.list_of_wave.append(round(result, 3))
            t = t + 0.01


def main():
    app = QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()


if __name__ == "__main__":
    main()
