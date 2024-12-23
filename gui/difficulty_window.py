from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

class DifficultyWindow(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Sudoku - Select Difficulty")
        self.setGeometry(700, 300, 600, 400)
        layout = QVBoxLayout()

        self.difficulty_label = QLabel("Select Difficulty:")
        self.difficulty_label.setFont(QFont("Press Start 2P", 20))
        layout.addWidget(self.difficulty_label)

        buttons = QVBoxLayout()
        self.easy_button = QPushButton("Easy")
        self.easy_button.setStyleSheet("""
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
        self.medium_button = QPushButton("Medium")
        self.medium_button.setStyleSheet("""
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
        self.hard_button = QPushButton("Hard")
        self.hard_button.setStyleSheet("""
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

        # Connect buttons to the handler method
        self.easy_button.clicked.connect(lambda: self.confirm_difficulty("easy"))
        self.medium_button.clicked.connect(lambda: self.confirm_difficulty("medium"))
        self.hard_button.clicked.connect(lambda: self.confirm_difficulty("hard"))

        buttons.addWidget(self.easy_button)
        buttons.addWidget(self.medium_button)
        buttons.addWidget(self.hard_button)

        layout.addLayout(buttons)

        self.setLayout(layout)

    def confirm_difficulty(self, difficulty):
        # Call the controller's start_game method with the selected difficulty
        self.controller.start_game(difficulty)
        self.close()
