import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QGuiApplication
from titlebar import TitleBar

class GridRaster(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("3D Scanner")

        # Get the available screen geometry
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()

        # Set the main window size to fit the screen
        self.resize(screen_geometry.width() , screen_geometry.height() )
        title_bar = TitleBar()
        self.setMenuWidget(title_bar)

        # Additional code to add widgets and customize the main window can be added here

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = GridRaster()
    mainWindow.show()
    sys.exit(app.exec())


