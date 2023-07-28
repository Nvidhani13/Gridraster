from PySide6.QtWidgets import QApplication, QMainWindow, QHBoxLayout, QWidget, QFrame,QPushButton,QVBoxLayout
from PySide6.QtCore import Qt
from PySide6.QtGui import QScreen
from login import LoginForm

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()

    # Create a central widget and set it as the central widget of the main window
    central_widget = QWidget()
    window.setCentralWidget(central_widget)

    layout = QHBoxLayout(central_widget)  # Pass the central widget to QHBoxLayout
    frame1 = QFrame()
    frame2 = QFrame()

    layout.addWidget(frame1)

    # Set the fixed width for frame2 as 1/4 of the total screen width
    screen = QApplication.primaryScreen()
    frame2_width = screen.availableGeometry().width() /2
    frame2.setMaximumWidth(frame2_width)

    layout.addWidget(frame2)

    #frame2.setStyleSheet("background-color: #e74c3c")
    frame2.setStyleSheet("background-color:#D9D9D9;")

    #window.setStyleSheet("background-color: #95a5a6")
    login=LoginForm("./gridraster.png")
    layout=QVBoxLayout()
    frame2.setLayout(layout)
    layout.addWidget(login)
    

    window.show()
    sys.exit(app.exec())
