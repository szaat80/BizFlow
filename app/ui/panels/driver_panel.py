# panels/driver_panel.py
from PySide6.QtWidgets import (QVBoxLayout, QLineEdit, 
                             QPushButton, QLabel, QComboBox)
from ui.base.base_panel import BasePanel
from ui.components.save_button import SaveButton

class DriverPanel(BasePanel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sofőr Kezelés")
        print("[DEBUG] DriverPanel: Inicializálás")
        self.setup_content()
        self.load_styles()

    def setup_content(self):
        print("[DEBUG] DriverPanel: Tartalom beállítása")
        try:
            layout = QVBoxLayout(self.content)
            
            # Név bevitel
            self.name_label = QLabel("Sofőr neve:")
            self.name_input = QLineEdit()
            
            # Telefonszám
            self.phone_label = QLabel("Telefonszám:")  
            self.phone_input = QLineEdit()
            
            # Jogosítvány típus
            self.license_label = QLabel("Jogosítvány típusa:")
            self.license_combo = QComboBox()
            self.license_combo.addItems(["B", "C", "D", "E"])
            
            # Státusz
            self.status_label = QLabel("Státusz:")
            self.status_combo = QComboBox()
            self.status_combo.addItems(["Aktív", "Inaktív", "Szabadságon"])
            
            # Elemek hozzáadása
            for widget in [self.name_label, self.name_input,
                         self.phone_label, self.phone_input,
                         self.license_label, self.license_combo,
                         self.status_label, self.status_combo]:
                layout.addWidget(widget)
            
            # Mentés gomb hozzáadása
            from app.ui.components.save_button import SaveButton
            self.save_btn = SaveButton(self, "driver_save")
            self.save_btn.set_click_handler(self.save_driver)
            layout.addWidget(self.save_btn)

        except Exception as e:
            print(f"[ERROR] DriverPanel: Tartalom beállítási hiba: {str(e)}")

    def save_driver(self):
        print("[DEBUG] DriverPanel: Sofőr mentése")
        try:
            # Adatok összegyűjtése
            data = {
                "name": self.name_input.text(),
                "phone": self.phone_input.text(),
                "license": self.license_combo.currentText(),
                "status": self.status_combo.currentText()
            }
            
            # TODO: Adatok validálása és mentése az adatbázisba
            print(f"[DEBUG] DriverPanel: Mentendő adatok: {data}")
            
        except Exception as e:
            print(f"[ERROR] DriverPanel: Mentési hiba: {str(e)}")
            
    def closeEvent(self, event):
        print("[DEBUG] DriverPanel: Panel bezárása")
        event.accept()