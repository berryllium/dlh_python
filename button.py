from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QCursor
from PyQt5 import QtCore

class Button(QPushButton):
    def __init__(self, label):
        super().__init__(label)
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet(
            "*{border: 4px solid #b8ddf8;" +
            "border-radius: 45px;" +
            "font-size: 35px;" +
            "color: #b8ddf8;" +
            "padding: 25px 0;" +
            "margin: 10px 10px;}"
            "*:hover{background: #b8ddf8;" +
            "color: #16b8f3;}"
        )