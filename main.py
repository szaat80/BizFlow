# main.py
import os
import sys
import traceback
from pathlib import Path

from PySide6.QtWidgets import QApplication
from app.ui.base.ui_manager import UIManager  # UIManager import hozzáadva


def setup_environment():
    """Környezet beállítása és útvonalak inicializálása"""
    try:
        # Path objektumot használunk a projekt gyökér meghatározásához
        project_root = Path(__file__).parent.absolute()
        if str(project_root) not in sys.path:
            sys.path.append(str(project_root))

        # Styles és resources mappák ellenőrzése
        styles_dir = project_root / "styles"
        resources_dir = project_root / "resources"

        if not styles_dir.exists() or not (styles_dir / "main.qss").exists():
            print(f"[ERROR] Main: Hiányzó styles mappa vagy main.qss: {styles_dir}")
            return False

        if not resources_dir.exists():
            print(f"[ERROR] Main: Hiányzó resources mappa: {resources_dir}")
            return False

        print(f"[DEBUG] Main: Projekt gyökér beállítva: {project_root}")
        print(f"[DEBUG] Main: Styles mappa ellenőrizve: {styles_dir}")
        print(f"[DEBUG] Main: Resources mappa ellenőrizve: {resources_dir}")
        return True

    except Exception as e:
        print(f"[ERROR] Main: Környezeti beállítási hiba: {e}")
        print(traceback.format_exc())
        return False


def init_application():
    try:
        app = QApplication(sys.argv)
        app.setStyle("Fusion")  # Először beállítjuk az alap stílust
        app.setObjectName("dashboardMainWindow")  # Majd az objektum nevet

        ui_manager = UIManager()
        ui_manager.apply_dashboard_style(app)

        return app, ui_manager

    except Exception as e:
        print(f"[ERROR] Main: Qt alkalmazás inicializálási hiba: {e}")
        print(traceback.format_exc())
        return None, None


def load_main_window(ui_manager=None):
    """Főablak betöltése és inicializálása"""
    try:
        from app.ui.components.main_window import MainWindow

        # Főablak létrehozása és UI manager átadása
        window = MainWindow(ui_manager=ui_manager)
        window.showFullScreen()

        print("[DEBUG] Main: Főablak sikeresen betöltve")
        return window

    except ImportError as e:
        print(f"[ERROR] Main: MainWindow importálási hiba: {e}")
        print(f"[DEBUG] Main: sys.path = {sys.path}")
        return None
    except Exception as e:
        print(f"[ERROR] Main: Főablak betöltési hiba: {e}")
        print(traceback.format_exc())
        return None


def main():
    """Fő alkalmazás indítási folyamat"""
    try:
        # Környezet beállítása
        if not setup_environment():
            print("[ERROR] Main: Környezet beállítása sikertelen")
            return 1

        # Adatbázis inicializálása - EZT KELL HOZZÁADNI
        from app.database.base import db_manager
        from app.database.models.driver import Driver
        if not db_manager.initialize():
            print("[ERROR] Main: Adatbázis inicializálása sikertelen")
            return 1

        Driver.metadata.create_all(db_manager._engine)

        # Alkalmazás inicializálása
        app, ui_manager = init_application()
        if not app:
            print("[ERROR] Main: Alkalmazás inicializálása sikertelen")
            return 1

        # Főablak betöltése
        window = load_main_window(ui_manager)
        if not window:
            print("[ERROR] Main: Főablak betöltése sikertelen")
            return 1

        # Alkalmazás indítása
        print("[DEBUG] Main: Alkalmazás indítása...")
        return app.exec()

    except Exception as e:
        print(f"[ERROR] Main: Kritikus hiba az alkalmazás indításakor: {e}")
        print(traceback.format_exc())
        return 1


if __name__ == "__main__":
    sys.exit(main())