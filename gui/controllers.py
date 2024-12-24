from PyQt5.QtCore import QTimer
from solver.sudoku_generation import SudokuPuzzleGeneration
from solver.sudoku_solver import SudokuSolver
from .game_window import GameWindow
from .difficulty_window import DifficultyWindow

class GameController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.difficulty_window = None
        self.difficulty = None
        self.generator = SudokuPuzzleGeneration()

    def start_game(self, difficulty):
        self.difficulty = difficulty
        board, solution = self.generator.generate_board(difficulty)
        self.game_window = GameWindow(self, difficulty)
        self.main_window.show_game_window(self.game_window)

        self.tile_styles = []

        set_tile_style = """
            QLabel {
                background-color: #D3D3D3;
                border: 1px solid #333;
                font-size: 18px;
                font-weight: bold;
                color: #000;
                min-width: 40px;
                min-height: 40px;
                max-width: 40px;
                max-height: 40px;
                text-align: center;
            }
        """
        empty_tile_style = """
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
                text-align: center;
            }
        """

        # Initialize the board
        # for r in range(9):
        #     for c in range(9):
        #         self.game_window.board[r][c].setText(str(board[r][c]) if board[r][c] != 0 else "")
        
        for r in range(9):
            row_styles = []
            for c in range(9):
                # Check if the tile is empty or set
                tile_value = board[r][c]
                if tile_value != 0:
                    self.game_window.board[r][c].setText(str(tile_value))
                    self.game_window.board[r][c].setStyleSheet(set_tile_style)
                    row_styles.append('set')
                else:
                    self.game_window.board[r][c].setText("")  # Empty tile
                    self.game_window.board[r][c].setStyleSheet(empty_tile_style)
                    row_styles.append('empty')

            self.tile_styles.append(row_styles)
        
        print(self.tile_styles)

        self.game_window.set_tile_styles(self.tile_styles)

    def reset_board(self):
        self.start_game(self.game_window.difficulty)

    def start_solving(self):
        self.game_window.start_timer()
        current_board = [
            [
                int(self.game_window.board[r][c].text()) if self.game_window.board[r][c].text().isdigit() else 0
                for c in range(9)
            ]
            for r in range(9)
        ]

        solver = SudokuSolver(current_board)
        solution = solver.solve()

        if solution:
            for (i, j), value in solution.items():
                self.game_window.update_tile(i, j, value)
            self.game_window.on_sudoku_solved()
        else:
            print("The puzzle cannot be solved.")
