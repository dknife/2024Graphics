from OpenGL.GL import *
from OpenGL.GLU import *

import sys
import numpy as np

from PyQt6.QtGui import QKeyEvent, QResizeEvent
from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
from PyQt6.QtCore import Qt

import math

class MyCam :
    def __init__(self):
        self.loc = np.array([0.0, 2.5, 0.0]) # 카메라 위치
        self.up  = np.array([0.0, 1.0, 0.0]) # y축
        self.angle = 0 # 카메라가 쳐다 보는 방향
        # 각도가 0일 때
        # 카메라는 x축을 쳐다보고
        # 카메라의 오른쪽 벡터는 z축이 된다고 정의하자   
    
    def getDirection(self):
        return np.array([math.cos(self.angle), 0, -math.sin(self.angle)])
        
    def getRight(self):  
        return np.array([math.sin(self.angle), 0, math.cos(self.angle)])   
    
    def moveForward(self, step) :
        dir = self.getDirection()
        self.loc += step*dir            
        
    def moveRight(self, step) :
        right = self.getRight()
        self.loc += step*right
            
def drawPlane() :
    n = 1000 # 그려지는 바둑판 모양의 땅을 몇 개의 점으로 나눌 것인가
    w = 1000 # 그려지는 바둑판 모양의 땅이 너비
    d = w / (n-1) # 각 줄 사이의 간격
    
    startX = -w/2
    startZ = -w/2
    
    ###############################################
    # glColor3f(1, 1, 0)
    glPointSize(5)
    glBegin(GL_QUADS)
    for i in range(n):
        for j in range(n):
            if (i+j)%2 == 0 :
                X = startX + i*d
                Z = startZ + j*d
                glVertex3f(X, 0, Z)
                glVertex3f(X+d, 0, Z)
                glVertex3f(X+d, 0, Z+d)
                glVertex3f(X, 0, Z+d)
    glEnd()
    glPointSize(1)
    
            
    
        
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
        self.cam = MyCam()
        ##############################
        self.bDisplayList = True
        ##############################
    
    ###############################################
    def toggleDisplaList(self) :
        if self.bDisplayList:
            self.bDisplayList = False
        else:
            self.bDisplayList = True
    ###############################################
      
    def initializeGL(self) :
        glClearColor(0.2, 0.2, 0.2, 1.0)
        
        # 사용가능한 디스플레이 리스트 번호를 부여 받기
        self.myPlaneDraw_displaylist = glGenLists(1)
        # 해당 번호로 디스플레이 리스트 정의하기
        glNewList(self.myPlaneDraw_displaylist, GL_COMPILE)
        # 실제 그리기 동작을 정의
        drawPlane()
        glEndList()       
        
        
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
        dir = self.cam.getDirection()
        gluLookAt(self.cam.loc[0],
                  self.cam.loc[1],
                  self.cam.loc[2],
                  self.cam.loc[0] + dir[0],
                  self.cam.loc[1] + dir[1],
                  self.cam.loc[2] + dir[2],
                  self.cam.up[0],
                  self.cam.up[1],
                  self.cam.up[2])
        drawAxes()
        
        #####################################################
        if self.bDisplayList:
            # 디스플레이 리스트를 호출하여 빠르게 렌더링
            # self.myPlaneDraw_displaylist를 호출
            glColor3f(0, 1, 1)
            glCallList(self.myPlaneDraw_displaylist)            
        else:
            # 매우 매우 느린 동작
            glColor3f(1, 1, 0)
            drawPlane() 
        #####################################################
        
        

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.glWidget = MyGLWidget()
        self.setCentralWidget(self.glWidget)
        
    def keyPressEvent(self, e):
        step = 0.1
        if e.key() == Qt.Key.Key_W :
            self.glWidget.cam.moveForward(step)                                 
        elif e.key() == Qt.Key.Key_S :
            self.glWidget.cam.moveForward(-step)                     
        elif e.key() == Qt.Key.Key_A:
            self.glWidget.cam.moveRight(-step)            
        elif e.key() == Qt.Key.Key_D:
            self.glWidget.cam.moveRight(step)
        elif e.key() == Qt.Key.Key_Q:
            # turn left
            self.glWidget.cam.angle += 0.1
        elif e.key() == Qt.Key.Key_E:
            # turn right
            self.glWidget.cam.angle -= 0.1     
        ###############################################       
        elif e.key() == Qt.Key.Key_L:
            self.glWidget.toggleDisplaList()
        ###############################################
            
        self.glWidget.update()
            
        

def main(argv = sys.argv) :
    app = QApplication(argv)
    window = MyWindow()
    window.setFixedSize(1200, 600)
    window.show()
    app.exec()
    
if __name__ == '__main__':
    main(sys.argv)
    
