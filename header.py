from PyQt5.QtWidgets import QLabel
from PyQt5 import QtCore

class Header(QLabel):
    def __init__(self, label):
        super().__init__(label)
        self.setStyleSheet("color: white; font-size: 36px;")
        self.setAlignment(QtCore.Qt.AlignCenter)