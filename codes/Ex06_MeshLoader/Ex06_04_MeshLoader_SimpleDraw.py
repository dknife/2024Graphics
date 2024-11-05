from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *

import sys
import numpy as np
import Drawable
           
class MeshLoader():
    def __init__(self):
        self.nV = 0
        self.nF = 0
        self.vBuffer = None
        self.iBuffer = None
    
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
        
        for i in range(self.nF) :
            glBegin(GL_LINE_LOOP)
            face = self.iBuffer[i*3: i*3+3]
            glVertex3fv(self.getVertex(face[0]))
            glVertex3fv(self.getVertex(face[1]))
            glVertex3fv(self.getVertex(face[2]))
            glEnd()
            
    def getVertex(self, idx):
        return self.vBuffer[idx*3: idx*3+3]
    
class MyGLWindow(QOpenGLWidget) :
    def __init__(self):
        super().__init__()
        self.myMesh = MeshLoader()
        self.axisDraw = Drawable.Drawable()
        self.myMesh.loadMesh('skull.txt')
        
    
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
        gluLookAt(1.5, 1.5, 1.5, 0, 0, 0, 0, 1, 0)
        # draw code
        self.myMesh.drawMesh()
        self.axisDraw.draw()
        
    
def main():
    app = QApplication(sys.argv)
    window = MyGLWindow()
    window.show()
    app.exec()
    
main()
                         
        
        
