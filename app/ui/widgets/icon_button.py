# widgets/icon_button.py
from PySide6.QtWidgets import QPushButton, QToolTip
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon

class IconButton(QPushButton):
    def __init__(self, icon=None, tooltip="", size=40):
        super().__init__()
        print(f"[DEBUG] IconButton: Inicializálás - Tooltip: {tooltip}")
        self.setObjectName("iconButton")
        self.setup_button(icon, tooltip, size)
        
    def setup_button(self, icon, tooltip, size):
        print(f"[DEBUG] IconButton: Gomb beállítása - Méret: {size}")
        try:
            self.setFixedSize(size, size)
            if icon:
                self.setIcon(icon)
                self.setIconSize(QSize(size-16, size-16))
                print("[DEBUG] IconButton: Ikon beállítva")
            if tooltip:
                self.setToolTip(tooltip)
                print(f"[DEBUG] IconButton: Tooltip beállítva: {tooltip}")
        except Exception as e:
            print(f"[ERROR] IconButton: Hiba a gomb beállításakor: {e}")
    
    def enterEvent(self, event):
        print(f"[DEBUG] IconButton: Belépési esemény - Tooltip: {self.toolTip()}")
        QToolTip.showText(event.globalPos(), self.toolTip())
        
    def leaveEvent(self, event):
        print(f"[DEBUG] IconButton: Kilépési esemény - Tooltip: {self.toolTip()}")
        QToolTip.hideText()