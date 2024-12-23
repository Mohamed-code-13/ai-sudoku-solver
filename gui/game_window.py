from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QWidget, QGridLayout, QFrame
from PyQt5.QtCore import Qt

class GameWindow(QWidget):
    def __init__(self, controller, difficulty):
        super().__init__()
        self.controller = controller
        self.difficulty = difficulty
        self.setWindowTitle("Sudoku Game")
        self.setGeometry(200, 200, 800, 600)

        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        # Sudoku board
        self.board_layout = QGridLayout()
        self.board = [[QLabel("0") for _ in range(9)] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                self.board[r][c].setFrameStyle(QFrame.Box)
                self.board[r][c].setAlignment(Qt.AlignCenter)
                self.board_layout.addWidget(self.board[r][c], r, c)

        layout.addLayout(self.board_layout)

        # Right-side controls
        controls_layout = QVBoxLayout()
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.controller.reset_board)

        self.start_button = QPushButton("Start Solving")
        self.start_button.clicked.connect(self.controller.start_solving)

        self.timer_label = QLabel("Timer: 0s")

        controls_layout.addWidget(self.reset_button)
        controls_layout.addWidget(self.start_button)
        controls_layout.addWidget(self.timer_label)

        layout.addLayout(controls_layout)
        self.setLayout(layout)

    def start_game(self):
        # Initialize the board for the selected difficulty
        # For simplicity, assuming a default board for now
        board = [[0 for _ in range(9)] for _ in range(9)]  # Replace with actual puzzle generation logic
        for r in range(9):
            for c in range(9):
                self.board[r][c].setText(str(board[r][c]))

    def update_tile(self, row, col, value):
        self.board[row][col].setText(str(value))

    def remove_tile(self, row, col):
        self.board[row][col].setText("0")