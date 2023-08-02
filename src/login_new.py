from PySide6.QtWidgets import QVBoxLayout,QFrame,QLabel,QLineEdit,QPushButton,QHBoxLayout,QSpacerItem,QSizePolicy,QApplication,QMainWindow,QWidget
import PySide6.QtGui  as QtGui
from ClickableText import ClickableText
from PySide6.QtCore import Qt,QSize
import sys

class LoginForm(QFrame):
    def __init__(self, logo_path=None, parent=None):
        
        
        super().__init__()
        
        
        # Logo Image
        self.logo_label = QLabel()
        logo_pixmap = QtGui.QPixmap(logo_path)
        self.logo_label.setPixmap(logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)
        self.logo_label.setMaximumHeight(80)
        self.logo_label.setMaximumWidth(100)
        
        
        #APP name and it's configuration
        self.appName_label=QLabel("Some APP")
        self.appName_label.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        self.appName_label.setStyleSheet("""
                                          font-size: 20px;
                                           color:#182C61;""")
        
        # after this we need vertical spacer 

        self.vertical_spacerItem1=QSpacerItem(0,50,QSizePolicy.Fixed,QSizePolicy.Maximum)
        
        

        #adding To QHBOXLAYout
        self.heading_layout=QHBoxLayout()
        self.button_layout=QHBoxLayout()
        self.spacerItem=QSpacerItem(0,0,QSizePolicy.Expanding,QSizePolicy.Minimum)
        self.spacerItem3=QSpacerItem(0,0,QSizePolicy.Expanding,QSizePolicy.Minimum)
        self.heading_layout.addItem(self.spacerItem)
        self.heading_layout.addWidget(self.logo_label,alignment=Qt.AlignCenter)
        
        self.heading_layout.addWidget(self.appName_label,alignment=Qt.AlignCenter)
        self.heading_layout.addItem(self.spacerItem3)

        
        #Login to Continue Label 
        self.Login_label=QLabel("Login to Continue")
        
        # after this we need another vertical spacer
        self.vertical_spacerItem2=QSpacerItem(0,20,QSizePolicy.Fixed,QSizePolicy.Maximum)
        




        #username text field 
        self.username_layout=QHBoxLayout()
        
        self.username_layout=QHBoxLayout()
        self.username_entry = QLineEdit()
        self.username_entry.setPlaceholderText("Username")
        self.username_entry.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.username_spacer=QSpacerItem(0,0,QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.username_entry.setMinimumWidth(100)
        self.username_entry.setMaximumWidth(400)
        
        #self.username_spacer.setAlignment(Qt.AlignCenter)

        self.username_entry.setFixedHeight(28)
        self.username_layout.addItem(self.username_spacer)
        #self.username_layout.addStretch(0)
        self.username_layout.addWidget(self.username_entry)
        

        self.vertical_spacerItem3=QSpacerItem(0,10,QSizePolicy.Fixed,QSizePolicy.Maximum)
        #password text field 
        self.password_layout=QHBoxLayout()
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)
        self.password_entry.setPlaceholderText("Password")
        self.password_entry.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.password_entry.setMinimumWidth(100)
        self.password_entry.setMaximumWidth(400)
        self.password_entry.setFixedHeight(28)
        #self.password_entry.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.password_spacer=QSpacerItem(0,0,QSizePolicy.Fixed,QSizePolicy.Fixed)
        
        self.password_layout.addItem(self.password_spacer)
        #self.username_layout.addStretch(0)
        self.password_layout.addWidget(self.password_entry)

        
        #before login button we new forgot password 
        self.forgot_password_layout=QHBoxLayout()
        self.forgot_password_spacer=QSpacerItem(0,0,QSizePolicy.Expanding,QSizePolicy.Fixed)
        self.forgot_password_spacer_left=QSpacerItem(62,0,QSizePolicy.Fixed,QSizePolicy.Fixed)
        self.forgot_password=ClickableText(text="Forgot Password ?",color="red")
        self.forgot_password.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.forgot_password_layout.addItem(self.forgot_password_spacer)
        
        self.forgot_password_layout.addWidget(self.forgot_password)
        self.forgot_password_layout.addItem(self.forgot_password_spacer_left)
        #self.forgot_password_layout.addItem(self.forgot_password_spacer)
        




        #let's start(Login)Button 
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.on_login_button_click)
        self.button_layout.addItem(self.spacerItem)
        self.button_layout.addWidget(self.login_button)
        self.spacerItem4=QSpacerItem(10,0,QSizePolicy.Expanding,QSizePolicy.Minimum)
        self.button_layout.addItem(self.spacerItem4)
        #self.size1=QSize(100,100)
        self.spacerItem1=QSpacerItem(0,0,QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.spacerItem2=QSpacerItem(0,0,QSizePolicy.Expanding,QSizePolicy.Expanding)




        
        
        
        #add them to layout 
        self.layout1 = QVBoxLayout()
        #self.layout1.addItem(self.spacerItem1)
        self.layout1.addLayout(self.heading_layout)
        self.layout1.addItem(self.vertical_spacerItem1)
        self.layout1.addWidget(self.Login_label,alignment=Qt.AlignCenter)
        self.layout1.addItem(self.vertical_spacerItem2)
        self.layout1.addLayout(self.username_layout)
        self.layout1.addItem(self.vertical_spacerItem2)
        self.layout1.addLayout(self.password_layout)
        self.layout1.addItem(self.vertical_spacerItem2)
        self.layout1.addLayout(self.forgot_password_layout)
        self.layout1.addLayout(self.button_layout)
        
        #self.layout.addItem(self.spacerItem1)
        self.layout1.addStretch(0)
        
        self.login_button.setMaximumHeight(40)
        self.login_button.setMaximumWidth(100)
       
        
        self.setLayout(self.layout1)    
    def on_login_button_click(self):
        # Add your login functionality here
        username = self.username_entry.text()
        password = self.password_entry.text()
        print(f"Username: {username}, Password: {password}")

#this is running main functionality just for checking 
if __name__=="__main__":
    app=QApplication(sys.argv)
    window=QMainWindow()
    widget=QWidget()
    window.setCentralWidget(widget)
    
    frame=LoginForm("./sample.png")
    
    layout_vertical=QVBoxLayout()
    layout_horizontal=QHBoxLayout()
    widget.setLayout(layout_vertical)
    spacer_up=QSpacerItem(0,0,QSizePolicy.Fixed,QSizePolicy.Expanding)
    #spacer_down=QSpacerItem(0,0,QSizePolicy.Fixed,QSizePolicy.Expanding)
    spacer_left=QSpacerItem(0,0,QSizePolicy.Expanding,QSizePolicy.Fixed)
    #spacer_right=QSpacerItem(0,0,QSizePolicy.Expanding,QSizePolicy.Fixed)
    layout_vertical.addItem(spacer_up)
    layout_vertical.addLayout(layout_horizontal)
    layout_horizontal.addItem(spacer_left)
    layout_horizontal.addWidget(frame)
    layout_horizontal.addItem(spacer_left)
    layout_vertical.addItem(spacer_up)



    frame.setStyleSheet("""
                          background-color:#3498db;""")
    
    window.show()
    sys.exit(app.exec())
