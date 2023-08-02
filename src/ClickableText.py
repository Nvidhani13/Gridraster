from PySide6.QtWidgets import QApplication, QLabel, QHBoxLayout, QWidget,QMainWindow
from PySide6.QtCore import Qt
import sys

class ClickableText(QLabel):
    def __init__(self,text="click me",color="black"):
        super().__init__()
        self.color=color
        self.init_ui(text)

    def init_ui(self,text):
        self.setText(text)
        #self.layout=QHBoxLayout()
        self.label = QLabel(text)
        #self.layout.addWidget(self.label)
    
        self.label.setStyleSheet(f"QLabel {{ color: {self.color}; text-decoration: underline; }}")

        

    def mousePressEvent(self, event):
        # Implement your desired functionality here
        #print(event)
        print("Custom Function Performed.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window=QMainWindow()
    label = ClickableText()
    window.setCentralWidget(label)
    window.show()

    sys.exit(app.exec())