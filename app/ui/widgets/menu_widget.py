# widgets/menu_widget.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QDialog, QHBoxLayout, QLabel, QApplication
from PySide6.QtCore import Qt, QPoint, QSize
from PySide6.QtGui import QIcon

class MenuWidget(QWidget):
    def __init__(self, icon_path):
        super().__init__()
        print("[DEBUG] MenuWidget: Inicializálás")
        self.icon_path = icon_path
        self.dialog = None
        self.is_dialog_open = False
        self.setup_ui()

    def setup_ui(self):
        print("[DEBUG] MenuWidget: UI beállítása")
        try:
            layout = QVBoxLayout()
            self.setLayout(layout)

            self.menu_button = QPushButton()
            self.menu_button.setObjectName("menuButton")
            self.menu_button.setIcon(QIcon(self.icon_path))
            self.menu_button.setFixedSize(40, 40)
            self.menu_button.setIconSize(QSize(24, 24))
            self.menu_button.clicked.connect(self.toggle_menu_dialog)
            layout.addWidget(self.menu_button)
            print("[DEBUG] MenuWidget: Menü gomb létrehozva")
        except Exception as e:
            print(f"[ERROR] MenuWidget: Hiba a UI beállításakor: {e}")

    def toggle_menu_dialog(self):
        print("[DEBUG] MenuWidget: Menü kapcsolás")
        try:
            if self.is_dialog_open:
                self.close_dialog()
            else:
                self.show_menu_dialog()
        except Exception as e:
            print(f"[ERROR] MenuWidget: Hiba a menü kapcsolásakor: {e}")

    def show_menu_dialog(self):
        print("[DEBUG] MenuWidget: Menü megjelenítése")
        try:
            self.dialog = QDialog(self)
            self.dialog.setWindowTitle("Menü")
            self.dialog.setWindowFlag(Qt.FramelessWindowHint)
            self.dialog.setModal(False)
            self.dialog.setFixedSize(200, 300)

            dialog_layout = QVBoxLayout()
            self.dialog.setLayout(dialog_layout)

            buttons = {
                "Nyomtatás": self.print_action,
                "Excel megnyitás": self.excel_action,
                "Export": self.export_action,
                "Import": self.import_action,
                "Mentés": self.save_action,
                "Kilépés": self.exit_application
            }

            for text, action in buttons.items():
                button = QPushButton(text)
                button.clicked.connect(action)
                dialog_layout.addWidget(button)
                print(f"[DEBUG] MenuWidget: {text} gomb hozzáadva")

            self.dialog.move(self.mapToGlobal(QPoint(self.width(), 0)))
            self.dialog.show()
            self.is_dialog_open = True
            print("[DEBUG] MenuWidget: Menü dialógus megjelenítve")
        except Exception as e:
            print(f"[ERROR] MenuWidget: Hiba a menü megjelenítésekor: {e}")

    def close_dialog(self):
        print("[DEBUG] MenuWidget: Menü bezárása")
        if self.dialog:
            self.dialog.close()
            self.is_dialog_open = False
            print("[DEBUG] MenuWidget: Menü dialógus bezárva")

    def print_action(self):
        print("[DEBUG] MenuWidget: Nyomtatás akció")
        from ..utils.print_handler import PrintHandler
        printer = PrintHandler(self)
        test_data = [
            {
                "Azonosító": "EMP001",
                "Név": "Kovács János",
                "Pozíció": "Sofőr",
                "Munkaidő": "8:00 - 16:00",
                "Fuvar státusz": "Folyamatban"
            }
        ]
        printer.print_data(test_data)
        self.close_dialog()
        
    def excel_action(self):
        print("[DEBUG] MenuWidget: Excel megnyitás akció")
        self.close_dialog()

    def export_action(self):
        print("[DEBUG] MenuWidget: Export akció")
        self.close_dialog()

    def import_action(self):
        print("[DEBUG] MenuWidget: Import akció")
        self.close_dialog()

    def save_action(self):
        print("[DEBUG] MenuWidget: Mentés akció")
        self.close_dialog()

    def exit_application(self):
        print("[DEBUG] MenuWidget: Alkalmazás bezárása")
        QApplication.quit()