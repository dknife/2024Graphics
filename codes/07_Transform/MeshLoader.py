from OpenGL.GL import *
from OpenGL.GLU import *


import numpy as np

           
class MeshLoader():
    def __init__(self):
        self.nV = 0
        self.nF = 0
        
        # 필요한 버퍼를 준비
        self.vBuffer = None # vertex buffer
        self.cBuffer = None # color buffer
        self.iBuffer = None # face index buffer
        
    
    def loadMesh(self, filename):
        with open(filename, 'rt') as input:
            # nV 읽기
            self.nV = int(next(input))
            
            # nV만큼의 공간을 가진 정점/컬러 버퍼 준비
            self.vBuffer = np.zeros(shape=(self.nV*3, ), dtype=float)
            self.cBuffer = np.zeros(shape=(self.nV*3, ), dtype=float)
            
            # 정점 데이터 읽기 : nV만큼 읽기
            for i in range(self.nV):
                self.vBuffer[i*3:i*3+3] = next(input).split()[0:3]                
            # nF 읽기
            self.nF = int(next(input))
            # nF만큼의 공간을 가진 인덱스 버퍼 준비하고 읽기
            self.iBuffer = np.zeros(shape=(self.nF*3), dtype=int)
            for i in range(self.nF):
                idx_list_for_face = next(input).split()
                self.iBuffer[i*3:i*3+3] = idx_list_for_face[1:4]                
            minVal = self.vBuffer.min()
            maxVal = self.vBuffer.max()
            dSize = (maxVal - minVal)
            center = (maxVal + minVal)/2.0
            self.vBuffer = 2*(self.vBuffer - center ) / dSize
            self.cBuffer = (self.vBuffer + np.array([1]))/2.
            
            print(self.cBuffer.min(), self.cBuffer.max())
            
    def prepareBufferRendering(self):
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_COLOR_ARRAY)
        ### 실제로 넘겨줄 버퍼를 설정
        # VERTEX 
        glVertexPointer(3, GL_FLOAT, 0, self.vBuffer)
        # COLOR
        glColorPointer(3, GL_FLOAT, 0, self.cBuffer)
        
    def render(self):
        glPointSize(2)
        glEnableClientState(GL_COLOR_ARRAY)
        glDrawElements(GL_TRIANGLES, self.nF * 3, GL_UNSIGNED_INT, self.iBuffer)
        glDisableClientState(GL_COLOR_ARRAY)
        glDrawArrays(GL_POINTS, 0, self.nV)        
       