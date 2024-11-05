from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *

import sys

class Drawable() :
    def __init__(self, length=1):
        self.length = length
        
    def draw(self):
        glBegin(GL_LINES)
        glColor3f(1,0,0)
        glVertex3f(0,0,0)
        glVertex3f(self.length,0,0)
        glColor3f(0,1,0)
        glVertex3f(0,0,0)
        glVertex3f(0,self.length,0)
        glColor3f(0,0,1)
        glVertex3f(0,0,0)
        glVertex3f(0,0,self.length)
        glEnd()
        
        
class MyGLWindow(QOpenGLWidget) :
    def __init__(self):
        super().__init__()
        self.myObj = Drawable(1.75)
    
    def initializeGL(self):
        glClearColor(0.5, 0.5, 1.0, 1.0)
    
    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, w/h, 0.1, 1000)
    
    def paintGL(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(2, 2, 2, 0, 0, 0, 0, 1, 0)
        # draw code
        self.myObj.draw()
    
def main():
    app = QApplication(sys.argv)
    window = MyGLWindow()
    window.show()
    app.exec()
    
main()
                         
        
        
