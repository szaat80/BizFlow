# main.py
from PySide6.QtWidgets import QApplication
import sys
import os

# Hozzáadjuk a projekt gyökérkönyvtárát a sys.path-hoz
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)
print("Project root added to sys.path:", project_root)
print("Current sys.path:", sys.path)

from app.ui.components.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

