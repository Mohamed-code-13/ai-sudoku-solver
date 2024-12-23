from PyQt5.QtCore import QTimer
from solver.sudoku_generation import SudokuPuzzleGeneration
from .game_window import GameWindow
from .difficulty_window import DifficultyWindow

class GameController:
    def __init__(self, main_window):
        self.main_window = main_window
        self.difficulty_window = None
        self.game_window = None
        self.difficulty = None
        self.generator = SudokuPuzzleGeneration()

    def show_difficulty_window(self):
        self.difficulty_window = DifficultyWindow(self)
        self.difficulty_window.show()

    def start_game(self, difficulty):
        self.difficulty = difficulty
        board, solution = self.generator.generate_board(difficulty)
        self.game_window = GameWindow(self, difficulty)
        # self.main_window.setCentralWidget(self.game_window)
        self.main_window.show_game_window()
        self.game_window.start_game()
        # Initialize the board
        # for r in range(9):
        #     for c in range(9):
        #         self.game_window.board[r][c].setText(str(board[r][c]) if board[r][c] != 0 else "0")

    def reset_board(self):
        self.start_game(self.game_window.difficulty)

    def start_solving(self):
        # TODO: Implement solving logic with timer updates
        pass
