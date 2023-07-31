


from PySide6.QtWidgets import QFrame,QApplication,QMainWindow,QHBoxLayout,QLabel
import sys



if __name__=="__main__":
    app=QApplication(sys.argv)
    window=QMainWindow()
    frame=QFrame()
    window.setCentralWidget(frame)
    frame.setStyleSheet("""
                          background-color:blue;""")
    layout=QHBoxLayout()
    label=QLabel("giojogijog")
    layout.addWidget(label)
    frame.setLayout(layout)
    window.show()
    sys.exit(app.exec())
