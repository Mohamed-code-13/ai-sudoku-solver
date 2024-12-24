from PyQt5.QtWidgets import QHBoxLayout, QWidget, QGridLayout, QLabel, QVBoxLayout, QPushButton, QFrame, QInputDialog, QMessageBox
from PyQt5.QtCore import Qt
from solver.sudoku_solver import SudokuSolver

class UserInputWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sudoku - User Input")
        self.setGeometry(700, 300, 600, 600)
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        b_layout = QHBoxLayout()
        self.board_layout = QGridLayout()
        self.board_layout.setContentsMargins(0, 0, 0, 0)
        self.board_layout.setHorizontalSpacing(0)
        self.labels = [[QLabel("") for _ in range(9)] for _ in range(9)]

        cell_style = """
            QLabel {
                background-color: #ffffff;
                border: 1px solid #333;
                font-size: 12px;
                font-weight: bold;
                color: #000;
                min-width: 40px;
                min-height: 40px;
                max-width: 40px;
                max-height: 40px;
                qproperty-alignment: AlignCenter;
            }
        """

        for r in range(9):
            for c in range(9):
                label = self.labels[r][c]
                label.setFrameStyle(QFrame.Box)
                label.setAlignment(Qt.AlignCenter)
                label.setStyleSheet(self.get_cell_style(r, c))
                label.mousePressEvent = lambda event, r=r, c=c: self.cell_clicked(r, c)
                self.board_layout.addWidget(label, r, c)

        self.solve_button = QPushButton("Solve")
        self.solve_button.setStyleSheet("""
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
        self.solve_button.clicked.connect(self.solve_button_clicked)

        b_layout.addLayout(self.board_layout)
        layout.addLayout(b_layout)
        layout.addWidget(self.solve_button)
        
        self.setLayout(layout)

    def get_cell_style(self, row, col):
        """Return the style string for the cell based on its row and column."""
        style = "font-size: 20px; min-width: 50px; min-height: 50px; "
        if (row % 2 == 0 and col % 2 == 0) or (row % 2 != 0 and col % 2 != 0):
            style += "background-color: #f9f9f9;"
        else:
            style += "background-color: #e0e0e0;"

        if (row % 3 == 0 and row != 0) or (col % 3 == 0 and col != 0):
            style += "border: 1px solid #333;"
        else:
            style += "border: 1px solid #ccc;"

        return style
    
    def cell_clicked(self, row, col):
        """Handle clicking on a cell to input a number."""
        current_value = self.board[row][col]
        number, ok = QInputDialog.getInt(self, "Enter Value", f"Enter a number for cell ({row+1}, {col+1}):", 
                                         value=current_value, min=1, max=9)
        
        if ok:
            self.board[row][col] = number
            self.labels[row][col].setText(str(number))

    def update_tile(self, row, col, value):
        self.labels[row][col].setText(str(value))
        self.board[row][col] = value

    def solve_button_clicked(self):
        """Validate the board when the user clicks the confirm button."""
        if self.is_solvable(self.board):
            for (i, j), value in self.solution.items():
                self.update_tile(i, j, value)
        else:
            self.show_error_message("The Sudoku puzzle is not solvable!")

    def is_solvable(self, board):
        """Check if the Sudoku board is solvable."""
        solver = SudokuSolver(board)
        self.solution = solver.solve()

        if self.solution:
            return True
        else:
            return False

    def solve_board(self):
        """Solve the Sudoku puzzle."""
        self.show_info_message("Puzzle solved successfully!")

    def show_error_message(self, message):
        """Show an error message box."""
        QMessageBox.critical(self, "Error", message)
        self.close()

    def show_info_message(self, message):
        """Show an info message box."""
        QMessageBox.information(self, "Info", message)

    def resizeEvent(self, event):
        """Override the resize event to adjust cell sizes to keep them square."""
        size = min(self.width(), self.height())
        cell_size = size // 9
        self.set_cell_sizes(cell_size)
        super().resizeEvent(event)

    def set_cell_sizes(self, size):
        """Set the size of each cell to ensure they remain square."""
        for r in range(9):
            for c in range(9):
                label = self.labels[r][c]
                label.setFixedSize(size, size)
