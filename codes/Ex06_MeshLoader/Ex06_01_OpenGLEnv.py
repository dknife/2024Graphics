from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *

import sys

class MyGLWindow(QOpenGLWidget) :
    def __init__(self):
        super().__init__()
        
def main():
    app = QApplication(sys.argv)
    window = MyGLWindow()
    window.show()
    app.exec()
    
main()
                         
        
        
