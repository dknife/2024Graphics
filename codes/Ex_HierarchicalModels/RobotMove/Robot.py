from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import Axis
import Cube

class Robot: 
    def __init__(self):
        
        self.loc = [0, 0, 0]    
        self.angles = [0, 0]  # arm1, arm2의 회전 각도   
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
        
        # 부모의 반만큼 위로 가서 (관절 지점으로 원점을 옮기고)
        glTranslatef(0, self.body[1]/2.0, 0)
        # 내가 원하는 회전을 하고 (회전하고)
        glRotatef(self.angles[0], 0, 0, 1)
        # 나의 반만큼 더 나온다 (내 부품의 끝이 관절에 맞춰지게 한다)
        glTranslatef(0, self.arm1[1]/2.0, 0)
        self.axis.draw()
        glPushMatrix()
        glScalef(self.arm1[0], self.arm1[1], self.arm1[2])
        self.cube.draw()
        glPopMatrix()
        
        # 부모의 반만큼 위로 가서 (관절 지점으로 원점을 옮기고)
        glTranslatef(0, self.arm1[1]/2.0, 0)
        # 내가 원하는 회전을 하고 (회전하고)
        glRotatef(self.angles[1], 0, 0, 1)
        # 나의 반만큼 더 나온다 (내 부품의 끝이 관절에 맞춰지게 한다)
        glTranslatef(0, self.arm2[1]/2.0, 0)
        self.axis.draw()
        glPushMatrix()
        glScalef(self.arm2[0], self.arm2[1], self.arm2[2])
        self.cube.draw()
        glPopMatrix()
        
    def move(self, dx, dy, dz):
        self.loc[0] += dx
        self.loc[1] += dy
        self.loc[2] += dz
        
        
        
        
