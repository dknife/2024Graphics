from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
from PyQt6.QtCore import *

import sys
import numpy as np
import math
import MeshLoader

verts = np.array([[0, 0.25, 0], [1, 0.1, 0], [1, 0, -1], [0, 0.1, -1], [-1, 0, -1], [-1, 0.1, 0], [-1, 0, 1], [0, 0.1, 1], [1, 0, 1] ], dtype=float)

def computeNormal(v0, v1, v2) :
    u = v1 - v0    
    v = v2 - v0
    N = np.cross(u, v)
    return N / np.linalg.norm(N)

class MyGLWindow(QOpenGLWidget) :
    def __init__(self):
        super().__init__()
        self.myMesh = MeshLoader.MeshLoader()
        self.angle = 0
    
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
    
    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, w/h, 0.1, 1000)
    
    def paintGL(self):
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()        
        
        gluLookAt(1.5, 1.5, 1.5, 0, 0, 0, 0, 1, 0)
        glLightfv(GL_LIGHT0, GL_POSITION, [1,1,0,0])
        
        glBegin(GL_TRIANGLES)
        N = computeNormal(verts[0], verts[1], verts[2])
        glNormal3fv(N)
        glVertex3fv(verts[0])
        glVertex3fv(verts[1])
        glVertex3fv(verts[2])
        
        N = computeNormal(verts[0], verts[2], verts[3])
        glNormal3fv(N)
        glVertex3fv(verts[0])
        glVertex3fv(verts[2])
        glVertex3fv(verts[3])
        
        N = computeNormal(verts[0], verts[3], verts[4])
        glNormal3fv(N)
        glVertex3fv(verts[0])
        glVertex3fv(verts[3])
        glVertex3fv(verts[4])
        
        N = computeNormal(verts[0], verts[4], verts[5])
        glNormal3fv(N)
        glVertex3fv(verts[0])
        glVertex3fv(verts[4])
        glVertex3fv(verts[5])
        
        N = computeNormal(verts[0], verts[5], verts[6])
        glNormal3fv(N)
        glVertex3fv(verts[0])
        glVertex3fv(verts[5])
        glVertex3fv(verts[6])
        
        N = computeNormal(verts[0], verts[6], verts[7])
        glNormal3fv(N)
        glVertex3fv(verts[0])
        glVertex3fv(verts[6])
        glVertex3fv(verts[7])
        
        N = computeNormal(verts[0], verts[7], verts[8])
        glNormal3fv(N)
        glVertex3fv(verts[0])
        glVertex3fv(verts[7])
        glVertex3fv(verts[8])
        
        N = computeNormal(verts[0], verts[8], verts[1])
        glNormal3fv(N)
        glVertex3fv(verts[0])
        glVertex3fv(verts[8])
        glVertex3fv(verts[1])
        glEnd()
        

        
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