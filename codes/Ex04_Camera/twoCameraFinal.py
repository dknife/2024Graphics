from OpenGL.GL import *
from OpenGL.GLU import *

import sys
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
from PyQt6.QtCore import Qt

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
  
import math
def drawHelix():
    glColor3f(0, 1, 1)
    glBegin(GL_LINE_STRIP)
    for i in range(1000):
        angle = i/10
        x, y = math.cos(angle), math.sin(angle)
        glVertex3f(x, y, -angle/10)
    glEnd()
    
class MyGLWidget(QOpenGLWidget):
    def __init__(self, perspective = False) :
        self.perspective = perspective
        super().__init__()
        
    def initializeGL(self):
        glClearColor(0.5, 0.5, 0.5, 1.0)
    
    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity() 
        if self.perspective:
            glFrustum(-2, 2, -2, 2, 0.5, 2)
        else:
            glOrtho(-2, 2, -2, 2, -2, 2)
        

    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        drawAxes()
        drawHelix()
    
class MyWindow(QMainWindow) :
        
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ortho Space')
        
        #### GUI 설정
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        gui_layout = QHBoxLayout()
        central_widget.setLayout(gui_layout)
        
        self.glWidget1 = MyGLWidget()
        self.glWidget2 = MyGLWidget(perspective=True)
        
        gui_layout.addWidget(self.glWidget1)
        gui_layout.addWidget(self.glWidget2)
 
           
def main(argv = sys.argv) :
    app = QApplication(argv)
    window = MyWindow()
    window.setFixedSize(1200, 600)
    window.show()
    app.exec()
    
if __name__ == '__main__':
    main(sys.argv)
        
