from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

import sys
import random

class MyGLWindow(QOpenGLWidget):
    def __init__(self, argv):
        super().__init__()
        self.setWindowTitle('Primitive')

    # 초기화
    def initializeGL(self) :
        glClearColor(0.0, 0.0, 1.0, 1.0)
        glPointSize(2)
    
    # 윈도 크기 변경
    def resizeGL(self, w, h):
        pass

    
    # 그리기 함수
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        
        glColor3f(0.2, 0.2, 0.2)
        r = [-0.9, 0.9]
        glBegin(GL_POINTS)
        for i in range(10000):
            x = random.randint(0, 100)
            y = random.randint(0, 100)   
            interval = r[1] - r[0] 
            x = interval * x / 100 + r[0]
            y = interval * y / 100 + r[0]
            glVertex2f(x, y)
        glEnd()
         
        # 좌표 축을 그려보자
        # x 축은 붉은 색
        # y 축은 초록 색
        # x축 (-1에서 1까지)
        glBegin(GL_LINES)
        glColor3f(1,0,0)
        glVertex2f(-1, 0)
        glVertex2f(1, 0)
        glColor3f(0, 1, 0)
        glVertex2f(0, 1)
        glVertex2f(0, -1)
        glEnd()
        
        
        


def main(argv):
    app = QApplication(argv)
    window = MyGLWindow(argv)
    window.show()
    app.exec()

if __name__ == '__main__' :
    main(sys.argv)