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
        
        gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)
        
        angle1, angle2 = 45, 45
        self.axisDraw.draw()
        self.cube.draw()
        glTranslatef(0, 0.5, 0)
        glRotatef(angle1, 0, 0, 1)
        glTranslatef(0, 0.5, 0)
        self.cube.draw()
        glTranslatef(0, 0.5, 0)
        glRotatef(angle2, 0, 0, 1)
        glTranslatef(0, 0.5, 0)
        self.cube.draw()
        
            
           
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
                         
        
        