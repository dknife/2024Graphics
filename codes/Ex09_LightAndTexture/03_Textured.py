from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
from PyQt6.QtCore import *

import sys
import numpy as np
import math
import MeshLoader
#import drawPlane

class MyGLWindow(QOpenGLWidget) :
    def __init__(self):
        super().__init__()
        self.myMesh = MeshLoader.MeshLoader()
        self.angle = 0
        self.light_pos = [0, 1, 0, 0]
        
        self.light_col = [1, 1, 0, 1]
        self.light_ambient = [0.1, 0.1, 0.1, 1.0]
        self.mat_col = [1, 1, 1, 0]
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
        glMaterialfv(GL_FRONT, GL_SHININESS, self.mat_col)
        
        #self.plane = drawPlane.TexturedPlane()
        
    
    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, w/h, 0.1, 1000)
    
    def paintGL(self):
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        
        theta = 3.14 * self.angle/180
        r = 2.5
        x = r * math.cos(theta)
        z = r * math.sin(theta)
        gluLookAt(x, 1.5, z, 0, 0, 0, 0, 1, 0)
        
        glLightfv(GL_LIGHT0, GL_POSITION, self.light_pos)
        
        # draw code here        
        self.myMesh.render()
        #self.plane.drawPlane()
        
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
