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
        
        self.light_pos = [0, 1, 0, 0]
        
        self.light_col = [1, 1, 0, 1] # 조명의 색은 노랑
        self.light_ambient = [0.1, 0.1, 0.1, 1.0]
        
        self.mat_col = [1, 1, 1, 0] # 물체는 흰색
        self.shininess = [125.0]
    
    def initializeGL(self):
        glClearColor(0.5, 0.5, 1.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        self.myMesh.loadMesh('cow.txt')
        self.myMesh.prepareBufferRendering()
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        
        glLightfv(GL_LIGHT0, GL_DIFFUSE, self.light_col)
        glLightfv(GL_LIGHT0, GL_SPECULAR, self.light_col)
        glLightfv(GL_LIGHT0, GL_AMBIENT, self.light_ambient)
        
        glMaterialfv(GL_FRONT, GL_DIFFUSE, self.mat_col)
        glMaterialfv(GL_FRONT, GL_SPECULAR, self.mat_col)
        glMaterialfv(GL_FRONT, GL_SHININESS, self.shininess)
        
    
    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, w/h, 0.1, 1000)
    
    def paintGL(self):
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        gluLookAt(1.5, 1.5, 1.5, 0, 0, 0, 0, 1, 0)
        
        glLightfv(GL_LIGHT0, GL_POSITION, self.light_pos)
        
        # draw code here        
        self.myMesh.render()
        
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
        
        self.glWidget.update()

        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    
main()
