import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from src.interface_display.ui_initial_page import Ui_Dialog  # Import the generated UI code

class InitialPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()  # Create an instance of the generated UI class
        self.ui.setupUi(self)       # Setup the UI