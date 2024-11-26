from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import Axis
import Cube

class Robot: 
    def __init__(self):
        
        self.loc = [0, 0, 0]        
        self.body = [1.5, 0.5, 1.5]
        self.arm1 = [0.3, 1.5, 0.3]
        self.arm2 = [0.3, 1.0, 0.3]
        
        self.cube = Cube.Cube(size = 1.0)
        self.axis = Axis.Axis()
        
    def draw(self) :
        
        glTranslatef(self.loc[0], self.loc[1], self.loc[2])
        
        self.axis.draw()
        glPushMatrix()
        glScalef(self.body[0], self.body[1], self.body[2])
        self.cube.draw()
        glPopMatrix()
        
    def move(self, dx, dy, dz):
        self.loc[0] += dx
        self.loc[1] += dy
        self.loc[2] += dz
        
        
        
        