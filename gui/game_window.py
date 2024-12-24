from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QWidget, QGridLayout, QFrame, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont
import time

from solver.sudoku_solver import SudokuSolver


class GameWindow(QWidget):
    def __init__(self, controller, difficulty):
        super().__init__()
        self.controller = controller
        self.difficulty = difficulty
        self.tile_styles = []
        self.setWindowTitle("Sudoku Game")
        self.setGeometry(700, 300, 600, 400)

        self.init_ui()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_timer)
        self.start_time = None
        self.elapsed_time = 0  # in milliseconds

    def init_ui(self):
        layout = QHBoxLayout()

        cell_style = """
            QLabel {
                background-color: #ffffff;
                border: 1px solid #333;
                font-size: 18px;
                font-weight: bold;
                color: #000;
                min-width: 40px;
                min-height: 40px;
                max-width: 40px;
                max-height: 40px;
                qproperty-alignment: AlignCenter;
            }
        """

        # Sudoku board
        self.board_layout = QGridLayout()
        self.board = [[QLabel("") for _ in range(9)] for _ in range(9)]
        for r in range(9):
            for c in range(9):
                self.board[r][c].setFrameStyle(QFrame.Box)
                self.board[r][c].setAlignment(Qt.AlignCenter)
                self.board[r][c].setStyleSheet(cell_style)
                self.board[r][c].mousePressEvent = lambda event, r=r, c=c: self.cell_clicked(
                    r, c)
                self.board_layout.addWidget(self.board[r][c], r, c)

        layout.addLayout(self.board_layout)

        # Right-side controls
        controls_layout = QVBoxLayout()
        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet("""
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
        self.reset_button.clicked.connect(self.controller.reset_board)

        self.start_button = QPushButton("Solve")
        self.start_button.setStyleSheet("""
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
        self.start_button.clicked.connect(self.controller.start_solving)

        self.timer_label = QLabel("Timer: 0.000000ms")
        self.timer_label.setFont(QFont("Press Start 2P", 10))

        controls_layout.addWidget(self.reset_button)
        controls_layout.addWidget(self.start_button)
        controls_layout.addWidget(self.timer_label)

        layout.addLayout(controls_layout)
        self.setLayout(layout)

    def set_tile_styles(self, tile_styles):
        """Set the tile styles from the controller."""
        self.tile_styles = tile_styles

    def resizeEvent(self, event):
        """Override resizeEvent to adjust cell sizes dynamically."""

        if not self.tile_styles or len(self.tile_styles) != 9 or len(self.tile_styles[0]) != 9:
            print("Error: tile_styles is not properly initialized!")
            return  # Exit early to prevent further errors

        window_width = self.width()
        window_height = self.height()
        available_width = window_width * 0.75
        available_height = window_height

        size = min(available_width, available_height)
        cell_size = int(size // 9)

        set_tile = """
            QLabel {
                background-color: #d3d3d3;  # Light gray for set tiles
                border: 1px solid #333;
                font-size: {cell_size // 3}px;
                font-weight: bold;
                color: #000;
                qproperty-alignment: AlignCenter;
            }
        """

        empty_tile = """
            QLabel {
                background-color: #fff;  # Light gray for set tiles
                border: 1px solid #333;
                font-size: {cell_size // 3}px;
                font-weight: bold;
                color: #000;
                qproperty-alignment: AlignCenter;
            }
        """

        for r in range(9):
            for c in range(9):
                label = self.board[r][c]
                label.setFixedSize(cell_size, cell_size)
                # if self.tile_styles[r][c] == 'set':
                #     label.setStyleSheet(set_tile)
                # else:
                #     label.setStyleSheet(empty_tile)
                label.setStyleSheet(f"""
                    QLabel {{
                        background-color: #ffffff;
                        border: 1px solid #333;
                        font-size: {cell_size // 3}px;
                        font-weight: bold;
                        color: #000;
                        qproperty-alignment: AlignCenter;
                    }}
                """)

        super().resizeEvent(event)

    def update_tile(self, row, col, value):
        self.board[row][col].setText(str(value))

    def remove_tile(self, row, col):
        self.board[row][col].setText("")

    def start_timer(self):
        """Start the timer."""
        self.start_time = time.time() * 1_000_000  # Store the current time in microseconds
        self.timer.start(5)  # Update every 100ms (0.1s)

    def stop_timer(self):
        """Stop the timer."""
        self.timer.stop()
        self.elapsed_time = 0  # Reset elapsed time to 0

    def update_timer(self):
        """Update the timer display every 100ms."""
        if self.start_time is not None:
            current_time = time.time() * 1_000_000  # Get the current time in microseconds
            elapsed_us = current_time - self.start_time
            milliseconds = int(elapsed_us // 1_000)  # Convert to milliseconds
            # Get the remainder as microseconds
            microseconds = int(elapsed_us % 1_000)
            self.timer_label.setText(f"Timer: {milliseconds}.{
                                     microseconds:03d}ms")

    def on_sudoku_solved(self):
        """Called when Sudoku puzzle is solved."""
        self.stop_timer()  # Stop the timer when the puzzle is solved

    def cell_clicked(self, row, col):
        """Handle clicking on a cell to input a number."""
        current_value = self.board[row][col].text()
        if len(current_value) == 0:
            current_value = 0
        else:
            current_value = int(current_value)

        number, ok = QInputDialog.getInt(self, "Enter Value", f"Enter a number for cell ({row+1}, {col+1}):",
                                         value=current_value, min=1, max=9)

        if ok:
            b = self.get_board()
            b[row][col] = number
            solver = SudokuSolver(b)
            sol = solver.solve()

            if sol:
                self.board[row][col].setText(str(number))
            else:
                QMessageBox.critical(self, "Error", 'Invalid Input')

    def get_board(self):
        b = [[0] * 9 for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val = self.board[r][c].text()
                if len(val) == 0:
                    val = 0
                else:
                    val = int(val)
                b[r][c] = val
        return b
