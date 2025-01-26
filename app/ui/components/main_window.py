# main_window.py
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from PySide6.QtCore import Qt
from app.ui.panels.left_panel import LeftPanel
from app.ui.panels.right_panel import RightPanel
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        print("[DEBUG] MainWindow: Inicializálás")
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowTitle("BizFlow Alkalmazás")
        self.showFullScreen()
        self.setup_ui()
        self.load_style()

    def setup_ui(self):
        print("[DEBUG] MainWindow: UI beállítása")
        try:
            self.central_widget = QWidget()
            self.setCentralWidget(self.central_widget)
            print("[DEBUG] MainWindow: Központi widget beállítva")

            self.main_layout = QHBoxLayout()
            self.central_widget.setLayout(self.main_layout)
            print("[DEBUG] MainWindow: Layout beállítva")

            self.left_panel = LeftPanel()
            self.right_panel = RightPanel()
            print("[DEBUG] MainWindow: Panelek létrehozva")

            self.main_layout.addWidget(self.left_panel)
            self.main_layout.addStretch()
            self.main_layout.addWidget(self.right_panel)
            print("[DEBUG] MainWindow: Panelek hozzáadva a layouthoz")

        except Exception as e:
            print(f"[ERROR] MainWindow: UI beállítási hiba: {e}")

    def load_style(self):
        print("[DEBUG] MainWindow: Stílus betöltése")
        try:
            style_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../styles/main.qss")
            with open(style_path, "r", encoding='utf-8') as file:
                self.setStyleSheet(file.read())
                print("[DEBUG] MainWindow: Stílus betöltve")
        except Exception as e:
            print(f"[ERROR] MainWindow: Stílus betöltési hiba: {e}")