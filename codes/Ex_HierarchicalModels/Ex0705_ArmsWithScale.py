from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
from PyQt6.QtCore import *

import sys
import numpy as np
import math
import Axis
import Cube
      
       
class MyGLWindow(QOpenGLWidget) :
    def __init__(self):
        super().__init__()
        self.axisDraw = Axis.Axis() 
        self.cube = Cube.Cube(size = 1.0) 
    
    def initializeGL(self):
        glClearColor(0.5, 0.5, 1.0, 1.0)
        glEnable(GL_DEPTH_TEST)
    
    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, w/h, 0.1, 1000)
    
    def paintGL(self):
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        gluLookAt(0, 0, 15, 0, 0, 0, 0, 1, 0)
        
        angle1, angle2 = 45, 45
        
        glPushMatrix()
        self.axisDraw.draw()
        glScalef(0.3, 2.0, 0.3)  # 길이 2인 물체        
        self.cube.draw()
        glPopMatrix()
        
        glTranslatef(0, 1.0, 0) # 부모 객체의 길이 반을 빠져 나온다
        glRotatef(angle1, 0, 0, 1) # 회전한다.
        glTranslatef(0, 1.5/2, 0)  # 나의 길이 반을 빠져 나온다.
        self.axisDraw.draw()
        glPushMatrix() ############################## Scale은 묶어서 다른 곳에 영향을 막는다다
        glScalef(0.2, 1.5, 0.2)
        self.cube.draw()
        glPopMatrix() ############################## Scale은 묶어서 다른 곳에 영향을 막는다다
        
        # 부모의 반 올라오기
        glTranslatef(0, 1.5/2, 0)
        # 회전하기
        glRotatef(angle2, 0, 0, 1)
        # 나의 반 올라오기
        glTranslatef(0, 1.0/2, 0)
        self.axisDraw.draw()
        glPushMatrix()
        glScalef(0.2, 1.0, 0.2)
        self.cube.draw()
        glPopMatrix()
            
           
class MainWindow(QMainWindow) :
    def __init__(self):
        QMainWindow.__init__(self)
        self.glWidget = MyGLWindow()
        self.setCentralWidget(self.glWidget)
        

        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    
main()
                         
        
        