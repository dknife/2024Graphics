from OpenGL.GL import *
from OpenGL.GLU import *

from PyQt6.QtWidgets import *
from PyQt6.QtOpenGLWidgets import *
from PyQt6.QtCore import *

import sys
import numpy as np
import math

class MeshLoader():
    def __init__(self):
        self.nV = 0
        self.nF = 0
        
        # 필요한 버퍼를 준비
        self.vBuffer = None # vertex buffer
        self.cBuffer = None # color buffer
        self.iBuffer = None # face index buffer
        self.nBuffer = None # normal buffer
        
    
    def loadMesh(self, filename):
        with open(filename, 'rt') as input:
            # nV 읽기
            self.nV = int(next(input))
            
            # nV만큼의 공간을 가진 정점/컬러/법선 버퍼 준비
            self.vBuffer = np.zeros(shape=(self.nV*3, ), dtype=float)
            self.nBuffer = np.zeros(shape=(self.nV*3,), dtype=float)
            
            # 정점 데이터 읽기 : nV만큼 읽기
            for i in range(self.nV):
                self.vBuffer[i*3:i*3+3] = next(input).split()[0:3]                
            # nF 읽기
            self.nF = int(next(input))
            
            # nF만큼의 공간을 가진 인덱스 버퍼 준비하고 읽기
            #### 면의 개수만큼 데이터를 읽어 들이는 부분 ********
            self.iBuffer = np.zeros(shape=(self.nF*3), dtype=int)
            for i in range(self.nF):
                idx_list_for_face = next(input).split()
                self.iBuffer[i*3:i*3+3] = idx_list_for_face[1:4]    
                index = self.iBuffer[i*3:i*3+3]
                ## 법선 벡터를 계산해 보자.
                
                # 면을 구성하는 세 정점의 좌표를 알자
                p0 = self.vBuffer[index[0]*3: index[0]*3+3]
                p1 = self.vBuffer[index[1]*3: index[1]*3+3]
                p2 = self.vBuffer[index[2]*3: index[2]*3+3]
                
                # 이 삼각형 위의 두 벡터를 구한다.
                # p0에서 p1으로 가는 벡터  : p1-p0
                # p0에서 p2로 가는 벡터 : p2 - p0
                u = p1 - p0
                v = p2 - p0
                # 두 벡터의 크로스 프로덕트 (가위곱, 벡터곱, 외적) 연산 실행
                # 두 벡터에 동시에 수직인 벡터를 얻는다 = 법선 벡터와 같은 방향
                N = np.cross(u, v)
                self.nBuffer[index[0]*3: index[0]*3+3] += N
                self.nBuffer[index[1]*3: index[1]*3+3] += N
                self.nBuffer[index[2]*3: index[2]*3+3] += N
                
            for i in range(self.nV) :
                N = self.nBuffer[i*3:i*3+3]
                norm = np.linalg.norm(N)
                N = N / norm
                self.nBuffer[i*3: i*3+3] = -N
                
            minVal = self.vBuffer.min()
            maxVal = self.vBuffer.max()
            scale = max([minVal, maxVal], key=abs)
            self.vBuffer /= scale
            
    def prepareBufferRendering(self):
        glEnableClientState(GL_VERTEX_ARRAY)
        glEnableClientState(GL_NORMAL_ARRAY)
        ### 실제로 넘겨줄 버퍼를 설정
        # VERTEX 
        glVertexPointer(3, GL_FLOAT, 0, self.vBuffer)
        glNormalPointer(GL_FLOAT, 0, self.nBuffer)

        
    def render(self):
        glDrawElements(GL_TRIANGLES, self.nF * 3, GL_UNSIGNED_INT, self.iBuffer)
