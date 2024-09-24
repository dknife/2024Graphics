from OpenGL.GL import *
from OpenGL.GLU import *

import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

class MyGLWindow(QOpenGLWidget) :
    def __init__(self):
        super().__init__()
    
    def initializeGL(self):
        glClearColor(1, 1, 0, 1)

    def resizeGL(self, width, height):
        glClearColor(width/(width+height), height/(width+height), 0, 1) 

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glFlush()

def main(argv=[]):
    app = QApplication(argv)
    window = MyGLWindow()
    if len(sys.argv) > 1:
        window.setWindowTitle(argv[1])
    else:
        window.setWindowTitle('Untitled')
    
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
     main(sys.argv)