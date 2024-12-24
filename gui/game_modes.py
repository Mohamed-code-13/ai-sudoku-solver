from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from .game_window import GameWindow

class GameModesWindow(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.setWindowTitle("Sudoku - Game Mode")
        self.setGeometry(700, 300, 600, 400)
        layout = QVBoxLayout()

        self.difficulty_label = QLabel("Select Game Mode:")
        self.difficulty_label.setFont(QFont("Press Start 2P", 20))
        layout.addWidget(self.difficulty_label)

        buttons = QVBoxLayout()
        self.random_button = QPushButton("Random Board")
        self.random_button.setStyleSheet("""
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
        self.user_button = QPushButton("User Input")
        self.user_button.setStyleSheet("""
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

        buttons.addWidget(self.random_button)
        buttons.addWidget(self.user_button)

        layout.addLayout(buttons)

        self.setLayout(layout)

        self.random_button.clicked.connect(self.on_random_button_clicked)
        self.user_button.clicked.connect(self.on_user_button_clicked)

    def on_random_button_clicked(self):
        """Handle Random Board button click."""
        self.main_window.show_difficulty_window()  # Show the difficulty window

    def on_user_button_clicked(self):
        """Handle User Input button click."""
        self.main_window.show_user_input_window()