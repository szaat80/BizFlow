# panels/delivery_panel.py
from PySide6.QtWidgets import (QVBoxLayout, QLineEdit, 
                             QLabel, QComboBox, QSpinBox,
                             QDoubleSpinBox)
from PySide6.QtCore import Qt
from app.ui.base.base_panel import BasePanel

class DeliveryPanel(BasePanel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Fuvar Kezelés")
        print("[DEBUG] DeliveryPanel: Inicializálás")
        self.setup_content()
        self.load_styles()

    def setup_content(self):
        print("[DEBUG] DeliveryPanel: Tartalom beállítása")
        try:
            layout = QVBoxLayout(self.content)
            
            # Szállítólevél szám
            self.delivery_label = QLabel("Szállítólevél szám:")
            self.delivery_input = QLineEdit()
            
            # Gyár
            self.factory_label = QLabel("Gyár:")
            self.factory_combo = QComboBox()
            self.factory_combo.addItems(["Gyár 1", "Gyár 2", "Gyár 3"])
            
            # Mennyiség
            self.amount_label = QLabel("Mennyiség (m³):")
            self.amount_spin = QDoubleSpinBox()
            self.amount_spin.setRange(0, 100)
            self.amount_spin.setDecimals(1)
            
            # Övezet
            self.zone_label = QLabel("Övezet:")
            self.zone_combo = QComboBox()
            self.zone_combo.addItems(["1-es", "2-es", "3-as", "4-es"])
            
            # Cím
            self.address_label = QLabel("Szállítási cím:")
            self.address_input = QLineEdit()
            
            # Státusz
            self.status_label = QLabel("Státusz:")
            self.status_combo = QComboBox()
            self.status_combo.addItems([
                "Felvett", "Úton", "Teljesítve", "Törölt"
            ])
            
            # Elemek hozzáadása
            for widget in [self.delivery_label, self.delivery_input,
                         self.factory_label, self.factory_combo,
                         self.amount_label, self.amount_spin,
                         self.zone_label, self.zone_combo,
                         self.address_label, self.address_input,
                         self.status_label, self.status_combo]:
                layout.addWidget(widget)
            
            # Mentés gomb
            from app.ui.components.save_button import SaveButton
            self.save_btn = SaveButton(self, "delivery_save")
            self.save_btn.set_click_handler(self.save_delivery)
            layout.addWidget(self.save_btn)

        except Exception as e:
            print(f"[ERROR] DeliveryPanel: Tartalom beállítási hiba: {str(e)}")

    def save_delivery(self):
        print("[DEBUG] DeliveryPanel: Fuvar mentése")
        try:
            data = {
                "delivery_number": self.delivery_input.text(),
                "factory": self.factory_combo.currentText(),
                "amount": self.amount_spin.value(),
                "zone": self.zone_combo.currentText(),
                "address": self.address_input.text(),
                "status": self.status_combo.currentText()
            }
            print(f"[DEBUG] DeliveryPanel: Mentendő adatok: {data}")
            
        except Exception as e:
            print(f"[ERROR] DeliveryPanel: Mentési hiba: {str(e)}")
            
    def closeEvent(self, event):
        print("[DEBUG] DeliveryPanel: Panel bezárása")
        event.accept()