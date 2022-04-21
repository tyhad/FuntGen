from PyQt5.QtWidgets import QMessageBox


def show_message_dialog(message=""):
    """
    Static function that use to show Message Dialog
    Param:
      message : str
    """
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText(str(message))
    msg.setWindowTitle("Information")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()
