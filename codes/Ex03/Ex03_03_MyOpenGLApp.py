from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

import sys

class MyGLWindow(QOpenGLWidget):
    def __init__(self, argv):
        super().__init__()
        if len(argv) > 1 :
            self.setWindowTitle(argv[1])
        else:
            self.setWindowTitle('The Window')
            
    # 세가지 주요 콜백 함수를 이 윈도의 메소드로 구현
    
    # 초기화
    def initializeGL(self) :
        glClearColor(1.0, 0.0, 1.0, 1.0)
        glPointSize(10)
    
    # 윈도 크기 변경
    def resizeGL(self, w, h):
        r = w/(w+h)
        g = h/(w+h)
        glClearColor(r, g, r*g, 1.0)
    
    # 그리기 함수
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        
        glBegin(GL_TRIANGLES)
        glVertex2f( 0.0, 0.0)
        glVertex2f( 0.5, 0.5)
        glVertex2f( 0.5,-0.5)
        glVertex2f(-0.5,-0.5)
        glEnd()

def main(argv):
    app = QApplication(argv)
    window = MyGLWindow(argv)
    window.show()
    app.exec()

if __name__ == '__main__' :
    main(sys.argv)