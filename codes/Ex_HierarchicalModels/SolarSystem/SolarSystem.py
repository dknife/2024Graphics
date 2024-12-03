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
        self.earth_revolve = 0.0 # 공전
        self.earth_rotate = 0.0 # 회전
    
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
        
        glPushMatrix() #### 태양의 자전을 고립시키자
        glRotatef(self.sun_angle, 0, 1, 0)
        self.mySphere.draw() # SUN
        glPopMatrix() #### 태양 자전 변환의 끝
        
        glRotatef(self.earth_revolve, 0, 1, 0) ## 공전
        glTranslatef(3, 0, 0)
        glRotatef(self.earth_rotate, 0, 1, 0) ## 자전
        glScalef(0.3, 0.3, 0.3)
        self.mySphere.draw() # EARTH
        
    def increaseAngles(self):
        self.sun_angle = self.increaseAngle(self.sun_angle, 0.1)
        self.earth_revolve = self.increaseAngle(self.earth_revolve, 1.23)
        self.earth_rotate = self.increaseAngle(self.earth_rotate, 3.1)
        
    def increaseAngle(self, angle, step):
        angle += step
        if angle >= 360 :
            angle -= 360     
        return angle    
           
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
        self.glWidget.increaseAngles()
        self.glWidget.update()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    
main()
                         
        
        