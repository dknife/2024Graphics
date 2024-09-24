from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

import sys

class MyGLWindow(QOpenGLWidget):
    def __init__(self):
        super().__init__()

def main(argv):
    app = QApplication(argv)
    window = MyGLWindow()
    window.show()
    app.exec()

if __name__ == '__main__' :
    main(sys.argv)