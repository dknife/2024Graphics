from OpenGL.GL import *
from OpenGL.GLU import *

import sys
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *

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
    
def drawBox(l, r, b, t, n, f) :
    glColor3f(1, 1, 1)
    glBegin(GL_LINE_LOOP) # 앞면 그리기
    glVertex3f(l, t, n)
    glVertex3f(r, t, n)
    glVertex3f(r, b, n)
    glVertex3f(l, b, n)    
    glEnd()
    glBegin(GL_LINE_LOOP) # 뒷면 그리기
    glVertex3f(l, t, f)
    glVertex3f(r, t, f)
    glVertex3f(r, b, f)
    glVertex3f(l, b, f)    
    glEnd()
    glBegin(GL_LINE_LOOP) # 오른쪽 면
    glVertex3f(r, t, n)
    glVertex3f(r, t, f)
    glVertex3f(r, b, f)
    glVertex3f(r, b, n)    
    glEnd()
    glBegin(GL_LINE_LOOP) # 왼쪽 면
    glVertex3f(l, t, n)
    glVertex3f(l, t, f)
    glVertex3f(l, b, f)
    glVertex3f(l, b, n)    
    glEnd()
    
class MyGLWidget(QOpenGLWidget):
    def __init__(self) :
        super().__init__()
        self.observation = False
        self.l = -1.5
        self.r = 1.5
        self.b = -2
        self.t = 2
        self.n = -1
        self.f = 1
        
    def setObserver(self) :
        self.observation = True
        
    def initializeGL(self):
        glClearColor(0.5, 0.5, 0.5, 1.0)
    
    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()   
        glOrtho(self.l, self.r, self.b, self.t, self.n, self.f)     
        if self.observation == True:
            glOrtho(-4, 4, -4, 4, -100, 100)
    
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        if self.observation == True:
            gluLookAt(0.5, 0.7, 1, 0, 0, 0, 0, 1, 0)
        drawAxes()
        drawBox(self.l, self.r, self.b, self.t, self.n, self.f)
    
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
        self.glWidget2 = MyGLWidget()
        self.glWidget2.setObserver()
        
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
        
