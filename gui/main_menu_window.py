from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QWidget, QGridLayout, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from .controllers import GameController

class MainMenuWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.setWindowTitle("Sudoku - Main Menu")
        self.setGeometry(700, 300, 600, 400)
        # self.controller = GameController(self)
        self.main_window = main_window
        self.init_ui()

    def init_ui(self):
        
        layout = QVBoxLayout()

        self.game_title = QLabel("SUDOKU")
        self.game_title.setAlignment(Qt.AlignCenter)
        self.game_title.setFont(QFont("Press Start 2P", 64))

        self.play_button = QPushButton("Play")
        self.play_button.setStyleSheet("""
            QPushButton {
                background-color: #333;
                border: 2px solid #333;
                border-radius: 5px;
                padding: 20px;
                font-size: 12px;
                font-family: 'Press Start 2P';
                color: #f0f0f0;
            }
        """)
        self.play_button.setFixedWidth(600)
        self.play_button.clicked.connect(self.main_window.show_difficulty_window)

        layout.addWidget(self.game_title)
        layout.addWidget(self.play_button, alignment=Qt.AlignHCenter)
        self.setLayout(layout)