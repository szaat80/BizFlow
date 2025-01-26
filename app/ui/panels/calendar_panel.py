# panels/calendar_panel.py
from PySide6.QtWidgets import (QVBoxLayout, QCalendarWidget, 
                             QTimeEdit, QLabel, QComboBox)
from PySide6.QtCore import QDate, QTime
from app.ui.base.base_panel import BasePanel

class CalendarPanel(BasePanel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Munkaidő Kezelés")
        print("[DEBUG] CalendarPanel: Inicializálás")
        self.setup_content()
        self.load_styles()

    def setup_content(self):
        print("[DEBUG] CalendarPanel: Tartalom beállítása")
        try:
            layout = QVBoxLayout(self.content)
            
            # Naptár widget
            self.calendar = QCalendarWidget()
            self.calendar.setSelectedDate(QDate.currentDate())
            
            # Kezdés időpont
            self.start_label = QLabel("Kezdés:")
            self.start_time = QTimeEdit()
            self.start_time.setTime(QTime(8, 0))
            
            # Befejezés időpont
            self.end_label = QLabel("Befejezés:")
            self.end_time = QTimeEdit()
            self.end_time.setTime(QTime(16, 0))
            
            # Munka típusa
            self.type_label = QLabel("Munka típusa:")
            self.type_combo = QComboBox()
            self.type_combo.addItems([
                "Normál munkanap",
                "Túlóra",
                "Hétvégi munka",
                "Szabadság",
                "Betegszabadság"
            ])
            
            # Elemek hozzáadása
            for widget in [self.calendar,
                         self.start_label, self.start_time,
                         self.end_label, self.end_time,
                         self.type_label, self.type_combo]:
                layout.addWidget(widget)
            
            # Mentés gomb
            from app.ui.components.save_button import SaveButton
            self.save_btn = SaveButton(self, "calendar_save")
            self.save_btn.set_click_handler(self.save_worktime)
            layout.addWidget(self.save_btn)

        except Exception as e:
            print(f"[ERROR] CalendarPanel: Tartalom beállítási hiba: {str(e)}")

    def save_worktime(self):
        print("[DEBUG] CalendarPanel: Munkaidő mentése")
        try:
            data = {
                "date": self.calendar.selectedDate().toString("yyyy-MM-dd"),
                "start_time": self.start_time.time().toString("HH:mm"),
                "end_time": self.end_time.time().toString("HH:mm"),
                "type": self.type_combo.currentText()
            }
            print(f"[DEBUG] CalendarPanel: Mentendő adatok: {data}")
            
        except Exception as e:
            print(f"[ERROR] CalendarPanel: Mentési hiba: {str(e)}")
            
    def closeEvent(self, event):
        print("[DEBUG] CalendarPanel: Panel bezárása")
        event.accept()