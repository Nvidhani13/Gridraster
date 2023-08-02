import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QLabel,QSizePolicy,QSpacerItem,QPushButton
from PySide6.QtGui import QGuiApplication, QColor, QPixmap,QIcon

class TitleBar(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout() #this is main layout setted to our QWidget 
        # layout.setContentsMargins(100, 100, 1000, 0)
        
        self.setLayout(self.layout)

        # Add the image to the title bar
        self.image_label = QLabel(self)
        pixmap = QPixmap("..//Resources//LogoTitleBar.png")  # Load the image
        self.image_label.setPixmap(pixmap)
        self.image_label.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.image_label.setMinimumHeight(52)

        # Create a QLabel for the title text
        self.title_label = QLabel("3D Scanner", self)
        self.title_label.setStyleSheet("""color: white; font-size: 25px; font-weight: bold; 
                                                            """)
        self.title_label.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.title_label.setMaximumWidth(140)
        self.title_label.setMinimumWidth(10)


        self.spacer1=QSpacerItem(10,0,QSizePolicy.Expanding,QSizePolicy.Fixed)
        
        #now three label for My WorkSpace Connect Device Mesh Visualiser that is window name 
        self.MyWorkspace = QLabel("My Worksapce")
        self.MyWorkspace.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        self.connectDevice = QLabel("Connect Device")
        self.connectDevice.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")
        self.MeshVisualiser= QLabel("Mesh Visualiser")
        self.MeshVisualiser.setStyleSheet("color: white; font-size: 16px; font-weight: bold;")

        # create a HBoxLayout 
        self.window_name_layout=QHBoxLayout()
        self.spacer2=QSpacerItem(30,0,QSizePolicy.Expanding,QSizePolicy.Fixed)#spaces between window names 
        self.window_name_layout.addWidget(self.MyWorkspace)
        self.window_name_layout.addItem(self.spacer2)
        self.window_name_layout.addWidget(self.connectDevice)
        self.window_name_layout.addItem(self.spacer2)
        self.window_name_layout.addWidget(self.MeshVisualiser)

        self.settingsIcon = QIcon("..//Resources//setting.png") 
        self.settingButton=QPushButton()
        self.settingButton.setIcon(self.settingsIcon)
        #self.settingButton.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.settingButton.setStyleSheet("""
                                            border:none;
                                            background-color:rgb(31,31,31)""")


        #Let's create a seprate QLabel for title and 

        self.title_layout=QHBoxLayout()
        self.title_layout.addItem(self.spacer1)

        self.title_layout.addWidget(self.image_label)
        self.title_layout.addItem(self.spacer1)
        self.title_layout.addWidget(self.title_label)
        self.title_layout.addStretch(1)
       
    


        # Add the title_label and image_label to the layout
        self.spacer3=QSpacerItem(200,0,QSizePolicy.Expanding,QSizePolicy.Fixed)#spaces between window names 

        self.layout.addLayout(self.title_layout)
        self.title_layout.addItem(self.spacer3)
        self.layout.addStretch(1)
        self.title_layout.addLayout(self.window_name_layout)
        self.layout.addStretch(0)
        self.layout.addWidget(self.settingButton)
        




        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), QColor(31,31,31))  # Set black color
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        title_bar = TitleBar()
        self.setMenuWidget(title_bar)  # Set the custom title bar as the menu widget

        # Additional code to add widgets and customize the main window can be added here

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
