# panels/left_panel.py
import os
from PySide6.QtWidgets import QWidget, QVBoxLayout, QSpacerItem, QSizePolicy
from ..widgets.icon_button import IconButton
from ..widgets.menu_widget import MenuWidget
from PySide6.QtGui import QIcon

class LeftPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("leftPanel")
        print("[DEBUG] LeftPanel: Inicializálás")
        self.setup_ui()
        
    def setup_ui(self):
        print("[DEBUG] LeftPanel: UI beállítása")
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        icons_path = "D:/BizFlow/resources/icon"
        
        menu_icon = QIcon(os.path.join(icons_path, "menu_icon.png"))
        database_icon = QIcon(os.path.join(icons_path, "database_icon.png"))
        employees_icon = QIcon(os.path.join(icons_path, "employees_icon.png"))
        vehicle_icon = QIcon(os.path.join(icons_path, "vehicle_icon.png"))
        worktime_icon = QIcon(os.path.join(icons_path, "worktime_icon.png"))
        transport_icon = QIcon(os.path.join(icons_path, "transport_icon.png"))
        settings_icon = QIcon(os.path.join(icons_path, "settings_icon.png"))
        help_icon = QIcon(os.path.join(icons_path, "help_icon.png"))

        self.menu_widget = MenuWidget(os.path.join(icons_path, "menu_icon.png"))
        layout.addWidget(self.menu_widget)

        self.database_button = IconButton(database_icon, "Adatbázis", 40)
        self.employees_button = IconButton(employees_icon, "Alkalmazott", 40)
        self.vehicle_button = IconButton(vehicle_icon, "Gépjármű", 40)
        self.worktime_button = IconButton(worktime_icon, "Munkaidő", 40)
        self.transport_button = IconButton(transport_icon, "Fuvar", 40)
        self.settings_button = IconButton(settings_icon, "Beállítások", 40)
        self.help_button = IconButton(help_icon, "Segítség", 40)

        layout.addWidget(self.database_button)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        layout.addWidget(self.employees_button)
        layout.addWidget(self.vehicle_button)
        layout.addWidget(self.worktime_button)
        layout.addWidget(self.transport_button)
        
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding))
        
        layout.addWidget(self.settings_button)
        layout.addWidget(self.help_button)