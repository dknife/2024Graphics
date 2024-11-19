from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
from PyQt6.QtCore import *

import sys
import numpy as np
import math
import Drawable
import MeshLoader
           
      
       
class MyGLWindow(QOpenGLWidget) :
    def __init__(self):
        super().__init__()
        self.myMesh = MeshLoader.MeshLoader()
        self.axisDraw = Drawable.Drawable()  
    
    def initializeGL(self):
        glClearColor(0.5, 0.5, 1.0, 1.0)
        glEnable(GL_DEPTH_TEST)
        self.myMesh.loadMesh('cow.txt')
        self.myMesh.prepareBufferRendering()
    
    def resizeGL(self, w, h):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60, w/h, 0.1, 1000)
    
    def paintGL(self):
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
        gluLookAt(2, 15, 15, 0, 0, 0, 0, 1, 0)
        
        self.axisDraw.draw()
        
        # draw  cows here        
        nCow = 15
        dAngle = 360/nCow
        angle = 0
        
        
        for i in range(nCow) :            
            glPushMatrix()
            glRotatef(angle, 0, 1, 0)
            glTranslatef(5.5, 0, 0)
            angle += dAngle
            
            self.myMesh.render()
            glPopMatrix()
            
           
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
                         
        
        
