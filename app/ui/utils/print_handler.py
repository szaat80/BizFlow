# utils/print_handler.py
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QPainter, QTextDocument, QPageSize, QFont
from PySide6.QtCore import Qt, QDateTime

class PrintHandler:
    def __init__(self, parent_widget: QWidget):
        print("[DEBUG] PrintHandler: Inicializálás")
        self.parent = parent_widget
        self.printer = QPrinter(QPrinter.HighResolution)
        self.setup_printer()
        
    def setup_printer(self):
        print("[DEBUG] PrintHandler: Nyomtató beállítása")
        try:
            self.printer.setPageSize(QPageSize(QPageSize.A4))
            self.printer.setPageOrientation(QPageSize.Portrait)
            print("[DEBUG] PrintHandler: Nyomtató beállítva")
        except Exception as e:
            print(f"[ERROR] PrintHandler: Nyomtató beállítási hiba: {e}")

    def print_data(self, data):
        print("[DEBUG] PrintHandler: Nyomtatás indítása")
        try:
            dialog = QPrintDialog(self.printer, self.parent)
            if dialog.exec() == QPrintDialog.Accepted:
                print("[DEBUG] PrintHandler: Nyomtatás elfogadva")
                document = QTextDocument()
                document.setDefaultFont(QFont("Arial", 10))
                document.setHtml(self.create_html_content(data))
                document.print_(self.printer)
                print("[DEBUG] PrintHandler: Nyomtatás sikeres")
                return True
            return False
        except Exception as e:
            print(f"[ERROR] PrintHandler: Nyomtatási hiba: {e}")
            return False