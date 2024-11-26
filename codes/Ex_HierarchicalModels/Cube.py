from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import Axis

class Cube :
    def __init__(self, size=1.0) :
        self.myAxis = Axis.Axis()
        self.size = size
        half_size = size / 2.0
        self.verts = np.array([
            [-half_size, -half_size, -half_size],
            [half_size, -half_size, -half_size], 
            [half_size, half_size, -half_size], 
            [-half_size, half_size, -half_size],  
            [-half_size, -half_size, half_size],
            [half_size, -half_size, half_size],
            [half_size, half_size, half_size],  
            [-half_size, half_size, half_size]  
        ])
        self.edges = np.array([
            [0, 1], [1, 2], [2, 3], [3, 0],
            [4, 5], [5, 6], [6, 7], [7, 4],
            [0, 4], [1, 5], [2, 6], [3, 7]     
        ])
        
    def draw(self) :
        self.myAxis.draw()
        glBegin(GL_LINES)
        # draw every edge
        for edge in self.edges:
            glVertex3fv(self.verts[edge[0]])
            glVertex3fv(self.verts[edge[1]])
        glEnd()
