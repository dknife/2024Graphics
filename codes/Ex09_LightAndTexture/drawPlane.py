from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

TEXSIZE = 16

class TexturedPlane() :
    def __init__(self) :
        self.tex = None
        myImage = self.create_texture_image()
        self.setup_texture(myImage)
        

    def create_texture_image(self):
        return np.random.rand(TEXSIZE, TEXSIZE, 3)

    def setup_texture(self, imageData):
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, TEXSIZE, TEXSIZE, 0, GL_RGB, GL_FLOAT, imageData)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        

    def drawPlane(self) :    
        glEnable(GL_TEXTURE_2D)
        glColor3f(1,1,1)
        glBegin(GL_QUADS)
        glNormal3f(0, 1, 0)
        glTexCoord2d(0, 0)
        glVertex3f(-1, 0, -1)
        glTexCoord2d(0, 2)
        glVertex3f(-1, 0,  1)
        glTexCoord2d(2, 2)
        glVertex3f( 1, 0,  1)
        glTexCoord2d(2, 0)
        glVertex3f( 1, 0, -1)
        glEnd()