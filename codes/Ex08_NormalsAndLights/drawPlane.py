from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

from PIL import Image
# pip install Pillow 필요


TEXSIZE = 16

class TexturedPlane() :
    def __init__(self, file_name = "") :
        self.tex = None
        if file_name == "":
            myImage = self.create_texture_image()
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, 
                         TEXSIZE, TEXSIZE, 0, GL_RGB, GL_FLOAT, myImage)
        else :
            img = Image.open(file_name)
            myImage = img.tobytes('raw', 'RGB', 0, -1)
            glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                        img.width, img.height, 0, GL_RGB, GL_UNSIGNED_BYTE, myImage)
            
        self.setup_texture(myImage)
        

    def create_texture_image(self):
        return np.random.rand(TEXSIZE, TEXSIZE, 3)

    def setup_texture(self, imageData):        
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
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
        glDisable(GL_TEXTURE_2D)