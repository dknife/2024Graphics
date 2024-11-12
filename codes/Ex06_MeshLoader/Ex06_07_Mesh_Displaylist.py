from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
from PyQt6.QtCore import *

import sys
import numpy as np
import math
import Drawable
           
class MeshLoader():
    def __init__(self):
        self.nV = 0
        self.nF = 0
        self.vBuffer = None
        self.iBuffer = None
        self.list_number = -1 # 아직 만들어지지 않은 리스트 번호
    
    def loadMesh(self, filename):
        with open(filename, 'rt') as input:
            # nV 읽기
            self.nV = int(next(input))
            # nV만큼의 공간을 가진 정점 버퍼 준비
            self.vBuffer = np.zeros(shape=(self.nV*3, ), dtype=float)
            # 정점 데이터 읽기 : nV만큼 읽기
            for i in range(self.nV):
                self.vBuffer[i*3:i*3+3] = next(input).split()[0:3]
                
            # nF 읽기
            self.nF = int(next(input))
            # nF만큼의 공간을 가진 인덱스 버퍼 준비하고 읽기
            self.iBuffer = np.zeros(shape=(self.nF*3), dtype=int)
            for i in range(self.nF):
                idx_list_for_face = next(input).split()
                self.iBuffer[i*3:i*3+3] = idx_list_for_face[1:4]
                
            minVal = self.vBuffer.min()
            maxVal = self.vBuffer.max()
            scale = max([minVal, maxVal], key=abs)
            self.vBuffer /= scale
            print(self.iBuffer)
    
    def drawMesh(self):
        glBegin(GL_POINTS)
        for i in range(self.nV):
            # 정점 버퍼 self.vBuffer
            glVertex3fv(self.vBuffer[i*3:i*3+3])
        glEnd()
        
        # 면을 그려 보자
        
        glBegin(GL_TRIANGLES)
        for i in range(self.nF) :            
            face = self.iBuffer[i*3: i*3+3]
            glColor3fv((self.getVertex(face[0]) + np.array([1])) / 2)
            glVertex3fv(self.getVertex(face[0]))
            glVertex3fv(self.getVertex(face[1]))
            glVertex3fv(self.getVertex(face[2]))
        glEnd()
            
    def getVertex(self, idx):
        return self.vBuffer[idx*3: idx*3+3]
    
    ##### 속도를 빠르게 하는 방법을 찾아 보자
    # 1. 그리기 동작을 디스플레이 리스트로 만들어 둔다
    def make_display_list(self):
        self.list_number = glGenLists(1)
        glNewList(self.list_number, GL_COMPILE)
        # DRAWING
        self.drawMesh()
        glEndList()
        
    # 2. 그릴 때는 리스트를 호출한다.
    def call_display_list(self):
        if self.list_number >= 0:
            glCallList(self.list_number)
    
class MyGLWindow(QOpenGLWidget) :
    def __init__(self):
        super().__init__()
        self.myMesh = MeshLoader()
        self.axisDraw = Drawable.Drawable()
        self.myMesh.loadMesh('skull.txt')
        
        self.angle = 0
        
    
    def initializeGL(self):
        glClearColor(0.5, 0.5, 1.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        self.myMesh.make_display_list()
    
    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, w/h, 0.1, 1000)
    
    def paintGL(self):
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        theta = 3.14 * self.angle/180
        r = 1.5
        x = r * math.cos(theta)
        z = r * math.sin(theta)
        gluLookAt(x, 1.5, z, 0, 0, 0, 0, 1, 0)
        # draw code
        #self.myMesh.drawMesh()
        self.myMesh.call_display_list()
        
        self.axisDraw.draw()
        
class MainWindow(QMainWindow) :
    def __init__(self):
        QMainWindow.__init__(self)
        self.glWidget = MyGLWindow()
        self.setCentralWidget(self.glWidget)
        self.viewing_angle = 0
        
        self.Timer = QTimer()
        self.Timer.setInterval(1)
        self.Timer.timeout.connect(self.timeout)
        self.Timer.start()
        
    def timeout(self):
        self.viewing_angle += 1
        if self.viewing_angle > 360 :
            self.viewing_angle -= 360
        self.glWidget.angle = self.viewing_angle
        self.glWidget.update()

        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    
main()
                         
        
        
