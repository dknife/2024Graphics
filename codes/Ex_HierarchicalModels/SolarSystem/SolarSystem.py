from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
from PyQt6.QtCore import *

import sys
import numpy as np
import math
import Sphere
      
class MyGLWindow(QOpenGLWidget) :
    def __init__(self):
        super().__init__()
        self.mySphere = Sphere.Sphere()
        self.sun_angle = 0.0
    
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
        
        gluLookAt(3, 3, 15, 0, 0, 0, 0, 1, 0)
        
        glRotatef(self.sun_angle, 0, 1, 0)
        self.mySphere.draw()
        
    def rotateSun(self):
        self.sun_angle += 1.0
        if self.sun_angle >= 360 :
            self.sun_angle -= 360            
        self.update()
        
        
        
           
class MainWindow(QMainWindow) :
    def __init__(self):
        QMainWindow.__init__(self)
        self.glWidget = MyGLWindow()
        self.setCentralWidget(self.glWidget)
        
        self.Timer = QTimer()
        self.Timer.setInterval(1)
        self.Timer.timeout.connect(self.timeout)
        self.Timer.start()
        
    def timeout(self):
        self.glWidget.rotateSun()
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    
main()
                         
        
        