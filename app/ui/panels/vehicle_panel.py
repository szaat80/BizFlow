# panels/vehicle_panel.py
from PySide6.QtWidgets import (QVBoxLayout, QLineEdit, 
                             QPushButton, QLabel, QComboBox)
from app.ui.base.base_panel import BasePanel

class VehiclePanel(BasePanel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Jármű Kezelés")
        print("[DEBUG] VehiclePanel: Inicializálás")
        self.setup_content()
        self.load_styles()

    def setup_content(self):
        print("[DEBUG] VehiclePanel: Tartalom beállítása")
        try:
            layout = QVBoxLayout(self.content)
            
            # Rendszám
            self.plate_label = QLabel("Rendszám:")
            self.plate_input = QLineEdit()
            
            # Jármű típus
            self.type_label = QLabel("Jármű típusa:")  
            self.type_combo = QComboBox()
            self.type_combo.addItems(["Mixer", "Szivattyú", "Pumix"])
            
            # Kapacitás
            self.capacity_label = QLabel("Kapacitás (m³):")
            self.capacity_input = QLineEdit()
            
            # Státusz
            self.status_label = QLabel("Státusz:")
            self.status_combo = QComboBox()
            self.status_combo.addItems(["Aktív", "Szervizben", "Inaktív"])
            
            # Elemek hozzáadása
            for widget in [self.plate_label, self.plate_input,
                         self.type_label, self.type_combo,
                         self.capacity_label, self.capacity_input,
                         self.status_label, self.status_combo]:
                layout.addWidget(widget)
            
            # Mentés gomb
            from app.ui.components.save_button import SaveButton
            self.save_btn = SaveButton(self, "vehicle_save")
            self.save_btn.set_click_handler(self.save_vehicle)
            layout.addWidget(self.save_btn)

        except Exception as e:
            print(f"[ERROR] VehiclePanel: Tartalom beállítási hiba: {str(e)}")

    def save_vehicle(self):
        print("[DEBUG] VehiclePanel: Jármű mentése")
        try:
            data = {
                "plate": self.plate_input.text(),
                "type": self.type_combo.currentText(),
                "capacity": self.capacity_input.text(),
                "status": self.status_combo.currentText()
            }
            print(f"[DEBUG] VehiclePanel: Mentendő adatok: {data}")
            
        except Exception as e:
            print(f"[ERROR] VehiclePanel: Mentési hiba: {str(e)}")
            
    def closeEvent(self, event):
        print("[DEBUG] VehiclePanel: Panel bezárása")
        event.accept()class my_class(object):
    pass




