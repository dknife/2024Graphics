from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtOpenGLWidgets import QOpenGLWidget

import sys

def drawAxes():
    glBegin(GL_LINES)  # 2개의 정점을 묶어 선분을 그림
    # x축
    glColor3f(1,0,0)
    glVertex3f(0,0,0)
    glVertex3f(1,0,0)
    # y축
    glColor3f(0,1,0)
    glVertex3f(0,0,0)
    glVertex3f(0,1,0)
    # z축
    glColor3f(0,0,1)
    glVertex3f(0,0,0)
    glVertex3f(0,0,1)
    glEnd()

class MyGLWindow(QOpenGLWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('glOrtho 연습')
        
    def initializeGL(self) :
        glClearColor(0.5, 0.5, 0.5, 1.0)
        
    def resizeGL(self, w: int, h: int) :
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-10, 10, -10, 10, -1, 1)
        
    def paintGL(self) :
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glBegin(GL_POLYGON)
        glColor3f(1,1,0)
        glVertex3f(0, 1, 0)
        glVertex3f( -1, 0, 0)
        glVertex3f(0, -1, 0)
        glVertex3f(1, 0, 0)
        glEnd()
        drawAxes()
        
    
def main(argv = sys.argv) :
    app = QApplication(argv)
    window = MyGLWindow()
    window.show()
    
    app.exec()
    
if __name__ == '__main__':
    main(sys.argv)
