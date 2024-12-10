from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
from PyQt6.QtCore import *

import sys
import numpy as np
import math

verts = np.array([[0, 0.25, 0], [1, 0.1, 0], [1, 0, -1], [0, 0.1, -1], [-1, 0, -1], [-1, 0.1, 0], [-1, 0, 1], [0, 0.1, 1], [1, 0, 1] ], dtype=float)

def computeNormal(v0, v1, v2) :
    u = v1 - v0    
    v = v2 - v0
    N = np.cross(u, v)
    return N / np.linalg.norm(N)

class MyGLWindow(QOpenGLWidget) :
    def __init__(self):
        super().__init__()
    
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