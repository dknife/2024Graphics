from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

import sys
import math

def draw_circle(cx, cy, r) :
    # 원그리기
    angle = 0    
    n_points = 100
    d_angle = 2 * 3.141592 / n_points # radian angle interval
    glColor3f(1, 1, 1)
    glBegin(GL_POLYGON)
    for i in range(n_points):
        x, y = r * math.cos(angle) + cx , r * math.sin(angle) + cy
        glVertex2f(x, y)
        angle += d_angle
        
    glEnd()
    
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
        
        # 삼각형 그리기
        glBegin(GL_TRIANGLES)
        glColor3f(0, 0.5, 0)
        glVertex2f(-0.75, 0)
        glVertex2f(0.25, 0)
        glVertex2f(-0.25, 0.5)
        glEnd()
        
        draw_circle(0.5, 0.5, 0.25)
        draw_circle(0.25, 0.25, 0.15)
        
        
        
        
        
        


def main(argv):
    app = QApplication(argv)
    window = MyGLWindow(argv)
    window.show()
    app.exec()

if __name__ == '__main__' :
    main(sys.argv)