


from PySide6.QtWidgets import QFrame,QApplication,QMainWindow,QHBoxLayout,QLabel,QVBoxLayout,QSpacerItem,QSizePolicy,QWidget
from login_new import LoginForm
import sys



if __name__=="__main__":
    app=QApplication(sys.argv)
    window=QMainWindow()
    widget=QWidget()
    window.setCentralWidget(widget)
    
    frame=LoginForm("./sample.png")
    window.setCentralWidget(frame)
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
                          background-color:blue;""")
    
    window.show()
    sys.exit(app.exec())
