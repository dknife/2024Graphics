from OpenGL.GL import *
from OpenGL.GLU import *

class Axis() :
    def __init__(self, length=1):
        self.length = length
        
    def draw(self):
        glBegin(GL_LINES)
        glColor3f(1,0,0)
        glVertex3f(0,0,0)
        glVertex3f(self.length,0,0)
        glColor3f(0,1,0)
        glVertex3f(0,0,0)
        glVertex3f(0,self.length,0)
        glColor3f(0,0,1)
        glVertex3f(0,0,0)
        glVertex3f(0,0,self.length)
        glEnd()
