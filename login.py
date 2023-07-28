# # login_form.py
# from PySide6 import QtWidgets
# from PySide6.QtCore import Qt

# class LoginForm(QtWidgets.QFrame):
#     def __init__(self, parent=None):
#         super().__init__(parent)
        
#         self.setWindowTitle("Login")
        
#         self.username_label = QtWidgets.QLabel("Username:")
#         self.username_entry = QtWidgets.QLineEdit()
        
#         self.password_label = QtWidgets.QLabel("Password:")
#         self.password_entry = QtWidgets.QLineEdit()
#         self.password_entry.setEchoMode(QtWidgets.QLineEdit.Password)
        
#         self.login_button = QtWidgets.QPushButton("Login")
#         self.login_button.clicked.connect(self.on_login_button_click)
        
#         layout = QtWidgets.QGridLayout()
#         #layout1=QtWidgets.QVBoxLayout()
#         self.login_button.setMaximumHeight(40)
#         self.login_button.setMaximumWidth(100)
#         layout.addWidget(self.username_label, 0, 0)
#         layout.addWidget(self.username_entry, 0, 1)
#         layout.addWidget(self.password_label, 1, 0)
#         layout.addWidget(self.password_entry, 1, 1)
#         layout.addWidget(self.login_button, 2, 0, 1, 2,Qt.AlignCenter)
#         #layout.setSpacing(10)
        
#         self.setLayout(layout)
    
#     def on_login_button_click(self):
#         # Add your login functionality here
#         username = self.username_entry.text()
#         password = self.password_entry.text()
#         print(f"Username: {username}, Password: {password}")
from PySide6.QtWidgets import QVBoxLayout,QFrame,QLabel,QLineEdit,QPushButton,QHBoxLayout,QSpacerItem,QSizePolicy
import PySide6.QtGui  as QtGui
from PySide6.QtCore import Qt

class LoginForm(QFrame):
    def __init__(self, logo_path, parent=None):
        
        
        super().__init__()
        #self.setWindowTitle("Login")
        
        # Logo Image
        self.logo_label = QLabel()
        logo_pixmap = QtGui.QPixmap(logo_path)
        self.logo_label.setPixmap(logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)
        
        self.username_label = QLabel("Username:")
        self.username_entry = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)
        
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.on_login_button_click)
        
        layout = QVBoxLayout()
        vertical_spacer_up = QSpacerItem(6, 6, QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addItem(vertical_spacer_up)
        
        layout.addWidget(self.logo_label,alignment=Qt.AlignCenter)  # Logo centered on top
        
        layout_username=QVBoxLayout()
        layout_password=QVBoxLayout()
        
        layout_username.addWidget(self.username_label)
       
        layout_username.addWidget(self.username_entry)
        layout_username.addStretch(1)
        
        
        layout_password.addWidget(self.password_label)
        # layout_password.addStretch(-5)
        layout_password.addWidget(self.password_entry)
        layout_password.addStretch(1)
        layout.addLayout(layout_username)
        layout.addLayout(layout_password)
        
        layout.addWidget(self.login_button,alignment=Qt.AlignCenter)
        layout.addStretch(1)
       
        # layout.addWidget(self.username_label, 1, 0)
        # layout.addWidget(self.username_entry, 2, 0)
        # layout.addWidget(self.password_label, 3, 0)
        # layout.addWidget(self.password_entry, 4, 0)
        # layout.addWidget(self.login_button, 3, 0, 1, 2, Qt.AlignCenter)  # Login button centered at the bottom
        vertical_spacer_below = QSpacerItem(6, 6, QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addItem(vertical_spacer_below)
        
        self.login_button.setMaximumHeight(40)
        self.login_button.setMaximumWidth(100)
        self.username_entry.setMaximumHeight(20)
        self.username_entry.setMaximumWidth(700)
        self.password_entry.setMaximumHeight(20)
        self.password_entry.setMaximumWidth(700)
        
        self.setLayout(layout)    
    def on_login_button_click(self):
        # Add your login functionality here
        username = self.username_entry.text()
        password = self.password_entry.text()
        print(f"Username: {username}, Password: {password}")
