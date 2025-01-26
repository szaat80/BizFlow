# ui/styles/style_loader.py
class StyleLoader:
    BASE_PANEL_STYLE = """
        QDialog {
            background-color: #2d2d2d;
            border: 1px solid #3d3d3d;
            border-radius: 5px;
            min-width: 400px;
        }
        QLabel {
            color: #e0e0e0;
            font-size: 13px;
            margin-top: 8px;
        }
        QLineEdit, QComboBox, QSpinBox, QDoubleSpinBox, QTimeEdit {
            background-color: #3d3d3d;
            border: 1px solid #4d4d4d;
            border-radius: 4px;
            padding: 8px;
            color: white;
            font-size: 13px;
            selection-background-color: #4B9DFF;
            margin-bottom: 8px;
        }
        QLineEdit:focus, QComboBox:focus, QSpinBox:focus, QDoubleSpinBox:focus {
            border: 1px solid #4B9DFF;
        }
        QPushButton {
            background-color: #4B9DFF;
            color: white;
            border: none;
            border-radius: 4px;
            padding: 8px 16px;
            font-weight: bold;
            margin-top: 16px;
        }
        QPushButton:hover {
            background-color: #3d8ae0;
        }
        QCalendarWidget {
            background-color: #2d2d2d;
            color: white;
        }
        QCalendarWidget QToolButton {
            color: white;
            background-color: transparent;
        }
        QCalendarWidget QMenu {
            background-color: #3d3d3d;
        }
        QCalendarWidget QSpinBox {
            background-color: #3d3d3d;
            color: white;
        }
        QTimeEdit::up-button, QTimeEdit::down-button,
        QSpinBox::up-button, QSpinBox::down-button,
        QDoubleSpinBox::up-button, QDoubleSpinBox::down-button {
            background: transparent;
            border: none;
        }
        QComboBox::drop-down {
            border: none;
            width: 20px;
        }
        QComboBox::down-arrow {
            image: none;
        }
    """

    @staticmethod
    def load_panel_style(panel):
        print("[DEBUG] StyleLoader: Stílus betöltése")
        try:
            panel.setStyleSheet(StyleLoader.BASE_PANEL_STYLE)
        except Exception as e:
            print(f"[ERROR] StyleLoader: Stílus betöltési hiba: {str(e)}")