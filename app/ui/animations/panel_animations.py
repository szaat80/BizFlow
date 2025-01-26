# animations/panel_animations.py
from PySide6.QtCore import QPropertyAnimation, QEasingCurve, QSize, Property
from PySide6.QtWidgets import QWidget

class HoverAnimation(QWidget):
    def __init__(self, widget, hover_scale=1.2):
        super().__init__()
        print(f"[DEBUG] HoverAnimation: Inicializálás - Widget: {widget}")
        self.widget = widget
        self.hover_scale = hover_scale
        self.setupAnimation()
        
    def setupAnimation(self):
        print("[DEBUG] HoverAnimation: Animáció beállítása")
        try:
            # Méretezési animáció
            self.scale_anim = QPropertyAnimation(self.widget, b"size")
            self.scale_anim.setDuration(200)  # 200ms 
            self.scale_anim.setEasingCurve(QEasingCurve.InOutQuad)
            
            # Eredeti méret mentése
            self.original_size = self.widget.size()
            print(f"[DEBUG] HoverAnimation: Eredeti méret: {self.original_size}")
            
        except Exception as e:
            print(f"[ERROR] HoverAnimation: Hiba az animáció beállításakor: {e}")
        
    def enterEvent(self, event):
        print("[DEBUG] HoverAnimation: Belépési esemény")
        try:
            # Növelés animáció
            target_size = QSize(
                int(self.original_size.width() * self.hover_scale),
                int(self.original_size.height() * self.hover_scale)
            )
            self.scale_anim.setEndValue(target_size)
            self.scale_anim.start()
            print(f"[DEBUG] HoverAnimation: Új méret: {target_size}")
            
        except Exception as e:
            print(f"[ERROR] HoverAnimation: Hiba a méretezéskor: {e}")
        
    def leaveEvent(self, event):
        print("[DEBUG] HoverAnimation: Kilépési esemény")
        try:
            # Visszaállítás animáció
            self.scale_anim.setEndValue(self.original_size)
            self.scale_anim.start()
            print("[DEBUG] HoverAnimation: Visszaállítás az eredeti méretre")
            
        except Exception as e:
            print(f"[ERROR] HoverAnimation: Hiba a visszaállításkor: {e}")