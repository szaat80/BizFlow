# ui/windows/main_window.py
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton
from app.ui.panels.driver_panel import DriverPanel
from app.ui.panels.vehicle_panel import VehiclePanel
from app.ui.panels.calendar_panel import CalendarPanel
from app.ui.panels.delivery_panel import DeliveryPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("BizFlow")
        self.setupUI()

    def setupUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Panel nyitó gombok
        buttons = {
            "Sofőr": DriverPanel,
            "Jármű": VehiclePanel,
            "Munkaidő": CalendarPanel,
            "Fuvar": DeliveryPanel
        }
        
        for text, panel_class in buttons.items():
            btn = QPushButton(text)
            btn.clicked.connect(lambda c, p=panel_class: self.open_panel(p))
            layout.addWidget(btn)
            
    def open_panel(self, panel_class):
        panel = panel_class(self)
        panel.show()