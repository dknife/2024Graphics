from OpenGL.GL import *
from OpenGL.GLU import *

import sys
from PyQt6.QtGui import QResizeEvent
from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
from PyQt6.QtCore import Qt

def drawPlane() :
    n = 50 # 그려지는 바둑판 모양의 땅을 몇 개의 점으로 나눌 것인가
    w = 50 # 그려지는 바둑판 모양의 땅이 너비
    step = w / (n-1) # 각 줄 사이의 간격
    
    start = -w/2
    end = w/2
    
    glBegin(GL_LINES)
    glColor3f(0.5, 0.25, 0.0)
    for i in range(n) : # n 개의 선을 긋자
        # z축과 평행한 선을 긋는다
        glVertex3f(start+i*step, 0, start)
        glVertex3f(start+i*step, 0, end)
        # x축과 평행한 선을 긋는다
        glVertex3f(start, 0, start+i*step)
        glVertex3f(end, 0, start+i*step)
    glEnd()
    
    
    
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
    
class MyGLWidget(QOpenGLWidget):
    def __init__(self):
        super().__init__()
    def initializeGL(self) :
        glClearColor(0.2, 0.2, 0.2, 1.0)
    def resizeGL(self, w, h) :
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        #glFrustum(-2, 2, -2, 2, 0.1, 5.0)
        #gluPerspective
        # y축 각도, 화면 종횡비, near, far
        gluPerspective(60, w/h, 0.1, 200)
        
        
    def paintGL(self):        
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0.5, 0, 0, 0, 1, 0, 1, 0)
        drawAxes()
        drawPlane()

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.glWidget = MyGLWidget()
        self.setCentralWidget(self.glWidget)

def main(argv = sys.argv) :
    app = QApplication(argv)
    window = MyWindow()
    window.setFixedSize(1200, 600)
    window.show()
    app.exec()
    
if __name__ == '__main__':
    main(sys.argv)
    
