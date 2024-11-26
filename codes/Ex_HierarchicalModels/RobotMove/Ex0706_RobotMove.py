from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtGui import QKeyEvent
from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
from PyQt6.QtCore import *

import sys
import numpy as np
import math
import Robot
      
class MyGLWindow(QOpenGLWidget) :
    def __init__(self):
        super().__init__()
        self.myRobot = Robot.Robot()
    
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
        
        self.myRobot.draw()      
        
        
           
class MainWindow(QMainWindow) :
    def __init__(self):
        QMainWindow.__init__(self)
        self.glWidget = MyGLWindow()
        self.setCentralWidget(self.glWidget)
        
    def keyPressEvent(self, e) :
        dx, dy, dz = 0., 0., 0.
        if e.key() == Qt.Key.Key_W :
            dz = -0.1
        if e.key() == Qt.Key.Key_S :
            dz = 0.1
        self.glWidget.myRobot.move(dx, dy, dz)
        self.glWidget.update()
        

        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    
main()
                         
        
        