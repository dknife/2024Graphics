from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

import sys

class MyGLWindow(QOpenGLWidget):
    def __init__(self, argv):
        super().__init__()
        self.setWindowTitle('Primitive')

    # 초기화
    def initializeGL(self) :
        glClearColor(0.0, 1.0, 1.0, 1.0)
        glPointSize(10)
    
    # 윈도 크기 변경
    def resizeGL(self, w, h):
        pass

    
    # 그리기 함수
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        


def main(argv):
    app = QApplication(argv)
    window = MyGLWindow(argv)
    window.show()
    app.exec()

if __name__ == '__main__' :
    main(sys.argv)