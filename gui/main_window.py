from PyQt5.QtWidgets import QMainWindow, QVBoxLayout,  QWidget, QStackedWidget, QApplication
from .main_menu_window import MainMenuWindow
from .difficulty_window import DifficultyWindow
from .game_modes import GameModesWindow
from .user_input_window import UserInputWindow
from .controllers import GameController

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.controller = GameController(self)
        self.setMinimumSize(700, 300)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Sudoku")
        self.setGeometry(700, 300, 600, 400)
        self.setStyleSheet('background-color: #f5f5f5;')

        self.stack = QStackedWidget()
        self.main_menu_window = MainMenuWindow(self)
        self.game_modes_window = GameModesWindow(self) 
        self.user_input_window = UserInputWindow()
        self.difficulty_window = DifficultyWindow(self.controller)

        self.stack.addWidget(self.main_menu_window)
        self.stack.addWidget(self.game_modes_window)
        self.stack.addWidget(self.user_input_window)
        self.stack.addWidget(self.difficulty_window)

        self.stack.setCurrentWidget(self.main_menu_window)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stack)
        l = QWidget()
        l.setLayout(main_layout)
        self.setCentralWidget(l)
    
    def toggle_fullscreen(self):
        """Toggle fullscreen while ensuring the window fits the screen properly."""
        if self.isFullScreen():
            self.showNormal()  # Exit fullscreen mode
        else:
            screen = QApplication.primaryScreen()
            available_geometry = screen.availableGeometry()  # Get usable screen space
            self.setGeometry(available_geometry)  # Adjust window geometry to fit the screen
            self.showFullScreen()

    def show_game_modes_window(self):
        self.stack.setCurrentWidget(self.game_modes_window)

    def show_user_input_window(self):
        self.stack.setCurrentWidget(self.user_input_window)

    def show_difficulty_window(self):
        self.stack.setCurrentWidget(self.difficulty_window)
    
    def show_game_window(self, game_window):
        self.stack.addWidget(game_window)
        self.stack.setCurrentWidget(game_window)