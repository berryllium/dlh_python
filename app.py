import sys

from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout
from game import Game

app = QApplication(sys.argv)
grid = QGridLayout()

window = QWidget()
window.setWindowTitle("My Quiz")
window.setFixedWidth(1200)
window.setStyleSheet("background: #16b8f3;")

game = Game(grid)
game.init()

window.setLayout(grid)
window.show()

sys.exit(app.exec())