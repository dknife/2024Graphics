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
        self.moon_revolve = 0.0 # 달의 공전
        self.jupiter_revolve = 0.0
        self.jupiter_rotate = 0.0
        self.jupiter_moon1_revolve = 0.0
        self.jupiter_moon1_rotate = 0.0
        self.jupiter_moon2_revolve = 0.0
        self.jupiter_moon2_rotate = 0.0
    
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
        
        ################# 지구계를 고립시키자
        glPushMatrix()
        
        glRotatef(self.earth_revolve, 0, 1, 0) ## 공전
        glTranslatef(3, 0, 0)
        glPushMatrix() ############ 지구 자전을 고립시키기 ###########
        glRotatef(self.earth_rotate, 0, 1, 0) ## 자전
        #####################################
        # earth
        glPushMatrix()
        glScalef(0.3, 0.3, 0.3)
        self.mySphere.draw() # EARTH
        glPopMatrix()
        #####################################
        glPopMatrix() ############ 지구 자전을 고립시키기 ###########
        
        ## MOON
        glRotate(self.moon_revolve, 0.1, 1, 0.2)
        glTranslatef(1, 0, 0)
        glScalef(0.1, 0.1, 0.1)
        self.mySphere.draw() # MOON
        
        glPopMatrix()
        ################# 지구계를 고립시키자
        
        ############ 목성계 시작
        glPushMatrix()
        
        glRotatef(self.jupiter_revolve, 0, 1, 0)
        glTranslatef(5, 0, 0)
        glPushMatrix() ######## 위성에 영향을 주면 안 되는 변환
        glRotatef(self.jupiter_rotate, 0, 1, 0)
        glScalef(0.5, 0.5, 0.5)
        self.mySphere.draw()
        glPopMatrix()  ######## 위성에 영향을 주면 안 되는 변환
        
        
        ############### 위성 1 고립
        glPushMatrix()
        glRotatef(self.jupiter_moon1_revolve, 0, 1, 0)
        glTranslatef(0.9, 0, 0)
        glRotatef(self.jupiter_moon1_rotate, 0, 1, 0)
        glScalef(0.2, 0.2, 0.2)
        self.mySphere.draw()
        glPopMatrix()
        
        ############### 위성 2
        glPushMatrix()
        glRotatef(self.jupiter_moon2_revolve, 0, 1, 0)
        glTranslatef(1.5, 0, 0)
        glRotatef(self.jupiter_moon2_rotate, 0, 1, 0)
        glScalef(0.2, 0.2, 0.2)
        self.mySphere.draw()
        glPopMatrix()
        
        
        glPopMatrix()
        ################# 목성계 끝
        
        
        
    def increaseAngles(self):
        self.sun_angle = self.increaseAngle(self.sun_angle, 0.1)
        self.earth_revolve = self.increaseAngle(self.earth_revolve, 1.23)
        self.earth_rotate = self.increaseAngle(self.earth_rotate, 13.1)
        self.moon_revolve = self.increaseAngle(self.moon_revolve, 2.0)
        self.jupiter_revolve = self.increaseAngle(self.jupiter_revolve, 3.1)
        self.jupiter_rotate = self.increaseAngle(self.jupiter_rotate, 3.1)
        self.jupiter_moon1_revolve = self.increaseAngle(self.jupiter_moon1_revolve, 2.1)
        self.jupiter_moon1_rotate = self.increaseAngle(self.jupiter_moon1_rotate, 5.1)
        self.jupiter_moon2_revolve = self.increaseAngle(self.jupiter_moon2_revolve, 10.1)
        self.jupiter_moon2_rotate = self.increaseAngle(self.jupiter_moon2_rotate, 13.1)
        
        
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
                         
        
        