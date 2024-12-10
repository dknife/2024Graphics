from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
from PyQt6.QtCore import *

import sys
import numpy as np
import math
import MeshLoader

class MyGLWindow(QOpenGLWidget) :
    def __init__(self):
        super().__init__()
        self.myMesh = MeshLoader.MeshLoader()
        self.angle = 0
        self.light_pos = [0, 2, 0, 1]
        
        self.light_col = [1, 1, 0, 1]
        self.light_ambient = [0.1, 0.1, 0.1, 1.0]
        self.mat_col = [1, 1, 1, 0]
        self.shininess = [125.0]
    
    def initializeGL(self):
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        self.myMesh.loadMesh('cow.txt')
        self.myMesh.prepareBufferRendering()
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.light_col)
        glLightfv(GL_LIGHT0, GL_SPECULAR, self.light_col)
        glLightfv(GL_LIGHT0, GL_AMBIENT, self.light_ambient)
        #glLightf(GL_LIGHT0, GL_SPOT_CUTOFF, 60.0)
        #glLightfv(GL_LIGHT0, GL_SPOT_DIRECTION, [0, -1, -1])
        
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.light_col)
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.light_col)
        glMaterialfv(GL_FRONT, GL_SHININESS, self.shininess)
        
    
    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, w/h, 0.1, 1000)
    
    def paintGL(self):
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        
        gluLookAt(4.5, 4.5, 6.5, 0, 0, 0, 0, 1, 0)
        
        glLightfv(GL_LIGHT0, GL_POSITION, self.light_pos)
        
        # draw code here        
        for i in range(-20, 20, 2):
            for j in range(-20, 20, 2):
                glPushMatrix()
                glTranslatef(i, 0, j)
                self.myMesh.render()
                glPopMatrix()
        
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
        
        self.glWidget.update()


        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    
main()