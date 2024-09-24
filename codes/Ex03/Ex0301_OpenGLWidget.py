from OpenGL.GL import *
from OpenGL.GLU import *

import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

class MyGLWindow(QOpenGLWidget) :
    def __init__(self):
        super().__init__()

def main(argv=[]):
    app = QApplication(argv)
    window = MyGLWindow()
    if len(sys.argv) > 1:
        window.setWindowTitle(argv[1])
    else:
        window.setWindowTitle('Untitled')
    window.setFixedSize(600, 600)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
     main(sys.argv)
