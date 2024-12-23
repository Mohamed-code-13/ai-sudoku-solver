# from PyQt5.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QWidget, QGridLayout, QFrame
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont
# from .controllers import GameController

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Sudoku Solver")
#         self.setGeometry(100, 100, 800, 600)
#         self.controller = GameController(self)

#         # Initialize UI
#         self.init_ui()

#     def init_ui(self):

#         self.game_title = QLabel("SUDOKU")
#         self.game_title.setFont(QFont("Press Start 2P", 12))

#         self.play_button = QPushButton("Play")
#         self.play_button.setStyleSheet("""
#             QPushButton {
#                 background-color: #333;
#                 border: 2px solid #333;
#                 border-radius: 5px;
#                 padding: 5px;
#                 font-size: 12px;
#                 font-family: 'Press Start 2P';
#                 color: #f0f0f0;
#             }
#         """)
#         self.play_button.clicked.connect(self.controller.show_difficulty_window)

#         self.addWidget(self.game_title)
#         self.addWidget(self.play_button)

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout,  QWidget, QStackedWidget
from .main_menu_window import MainMenuWindow
from .difficulty_window import DifficultyWindow
from .game_window import GameWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Sudoku")
        self.setGeometry(700, 300, 600, 400)
        self.setStyleSheet('background-color: #f5f5f5;')

        self.stack = QStackedWidget()
        self.main_menu_window = MainMenuWindow(self)
        self.difficulty_window = DifficultyWindow(self)
        # self.game_window = GameWindow(self)

        self.stack.addWidget(self.main_menu_window)
        self.stack.addWidget(self.difficulty_window)
        # self.stack.addWidget(self.game_window)

        self.stack.setCurrentWidget(self.main_menu_window)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stack)
        l = QWidget()
        l.setLayout(main_layout)
        self.setCentralWidget(l)
    
    def show_difficulty_window(self):
        self.stack.setCurrentWidget(self.difficulty_window)
    
    def show_game_window(self):
        """Switch to the DifficultyWindow."""
        self.stack.setCurrentWidget(self.game_window)