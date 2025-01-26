# app/ui/base/base_panel.py
from PySide6.QtWidgets import QDialog, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

class BasePanel(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        print("[DEBUG] BasePanel: Inicializálás")
        self.setup_ui()
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        
    def setup_ui(self):
        print("[DEBUG] BasePanel: UI beállítása")
        try:
            self.layout = QVBoxLayout(self)
            self.content = QWidget()
            self.layout.addWidget(self.content)
            
        except Exception as e:
            print(f"[ERROR] BasePanel: UI beállítási hiba: {str(e)}")

    def load_styles(self):
        try:
            from app.ui.styles.style_loader import StyleLoader
            StyleLoader.load_panel_style(self)
        except Exception as e:
            print(f"[ERROR] BasePanel: Stílus betöltési hiba: {str(e)}")