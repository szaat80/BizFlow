# layouts/main_layout.py
from PySide6.QtWidgets import QHBoxLayout

class MainLayout(QHBoxLayout):
    def __init__(self):
        super().__init__()
        print("[DEBUG] MainLayout: Inicializálás")
        self.setup_ui()
        
    def setup_ui(self):
        print("[DEBUG] MainLayout: UI beállítása")
        # Layout beállítások
        self.setSpacing(0)
        self.setContentsMargins(0, 0, 0, 0)
