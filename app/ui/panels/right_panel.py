# panels/right_panel.py
from PySide6.QtWidgets import QWidget, QVBoxLayout

class RightPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("rightPanel")
        print("[DEBUG] RightPanel: Inicializálás")
        self.setup_ui()
        
    def setup_ui(self):
        print("[DEBUG] RightPanel: UI beállítása")
        try:
            layout = QVBoxLayout()
            self.setLayout(layout)
            
            self.content = QWidget()
            layout.addWidget(self.content)
            print("[DEBUG] RightPanel: Tartalom widget hozzáadva")
        except Exception as e:
            print(f"[ERROR] RightPanel: Hiba a UI beállításakor: {e}")