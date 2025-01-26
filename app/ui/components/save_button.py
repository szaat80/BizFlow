# components/save_button.py
from PySide6.QtWidgets import QPushButton

class SaveButton(QPushButton):
    def __init__(self, parent=None, button_id=None):
        super().__init__("Mentés", parent)
        self.setObjectName(f"saveButton_{button_id}")
        print(f"[DEBUG] SaveButton: Inicializálás - ID: {button_id}")
        
    def set_click_handler(self, handler):
        print("[DEBUG] SaveButton: Click handler beállítása")
        self.clicked.connect(handler)class my_class(object):
    pass




