[수업전체](https://github.com/dknife/dknife.github.io/wiki/Lecture_Homepage)

### 중간고사 
[중간고사 문제지](https://forms.office.com/r/rsc61Wn0Nm)

[중간고사 평가 결과](https://github.com/dknife/2024Graphics/blob/main/LN/midterm_result.jpg)

[답변 분석](https://github.com/dknife/2024Graphics/blob/main/LN/midterm_analysis.pdf)

### 기본적인 설치
1. python interpreter (python.org)

2. visual studio code (code.microsoft.com)

3. packages for graphics programming

pip install --upgrade pip

pip install numpy

pip install pyqt6

pip install pyopengl

# 2024Graphics

### 수업전 사전 설문 조사

[설문 조사 링크](https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAO__fVSsTlUNFZWRksyUDczOVNQR1VTSkNLUlVFS1lTVy4u)

[응답 결과](https://forms.office.com/Pages/AnalysisPage.aspx?AnalyzerToken=AiRzmUfwW0bIduVPTEMLrCiZnAnsJqfx&id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAO__fVSsTlUNFZWRksyUDczOVNQR1VTSkNLUlVFS1lTVy4u)

## 강의 자료

[강의 00 오리엔테이션](https://github.com/dknife/2024Graphics/raw/main/LN/Lec00_Orientation.pdf)

### 강의 01 그래픽스 소개

[자료](https://github.com/dknife/2024Graphics/raw/main/LN/Lec01_Introduction2Graphics.pdf)

### 강의 02 OpenGL 소개

[수업 자료](https://github.com/dknife/2024Graphics/raw/main/LN/Lec02_BasicGraphicsProgramming.pdf)

[강의 노트](https://github.com/dknife/2024Graphics/raw/main/LN/Lec02_BasicGraphicsProgramming_Pres.pdf)

#### 실습
[2-1 파이썬 테스트](https://github.com/dknife/2024Graphics/blob/main/codes/01_test.py)

[2-2 리스트 테스트](https://github.com/dknife/2024Graphics/blob/main/codes/01_listtest.py)

[2-3 함수 테스트](https://github.com/dknife/2024Graphics/blob/main/codes/01_function_test.py)

[2-1 PyQt Window 테스트](https://github.com/dknife/2024Graphics/blob/main/codes/01_QtApp.py)

[2-1 나만의 윈도우 클래스 만들기](https://github.com/dknife/2024Graphics/blob/main/codes/01_QtMyWindowApp.py)

### 강의 03 OpenGL Primitives

[수업 자료](https://github.com/dknife/2024Graphics/raw/main/LN/Lec03_Primitives.pdf)

[강의 노트](https://github.com/dknife/2024Graphics/raw/main/LN/Lec03_Primitives_Pres.pdf)

#### 실습

[3-1 오픈지엘 위짓](https://github.com/dknife/2024Graphics/blob/main/codes/Ex03/Ex0301_OpenGLWidget.py)

[3-2 오픈지엘 위짓의 콜백](https://github.com/dknife/2024Graphics/blob/main/codes/Ex03/Ex0302_OpenGL_Callbacks.py)

[3-3 Step by Step OpenGL Window]

[step 1 QWidget을 상속받은 클래스를 윈도로 사용](https://github.com/dknife/2024Graphics/blob/main/codes/Ex03/Ex03_01_CustomWindowApp.py)

[step 2 QOpenGLWidget을 상속받은 클래스를 윈도로 사용](https://github.com/dknife/2024Graphics/blob/main/codes/Ex03/Ex03_02_CustomGLWindow.py)

[step 3 QOpenGLWidget에 세 개의 핵심 콜백 구현하기](https://github.com/dknife/2024Graphics/blob/main/codes/Ex03/Ex03_03_MyOpenGLApp.py)

[3-4 프리미티브 연습](https://github.com/dknife/2024Graphics/blob/main/codes/Ex03/Ex03_04_Primitives.py)

[3-5 원 그리기](https://github.com/dknife/2024Graphics/blob/main/codes/Ex03/Ex03_05_Drawing.py)

### 강의 4 Camera 다루기

[수업 자료](https://github.com/dknife/2024Graphics/raw/main/LN/Lec04_CameraProjection.pdf)

[강의 노트](https://github.com/dknife/2024Graphics/raw/main/LN/Lec04_CameraProjection_pres.pdf)

#### 실습 

[4-1 glOrtho 사용](https://github.com/dknife/2024Graphics/blob/main/codes/Ex04_Camera/0401_glOrthoTest.py)

[4-2 두 개의 OpenGL Widgets](https://github.com/dknife/2024Graphics/blob/main/codes/Ex04_Camera/0403_TwoGLWidgets.py)

[4-3 관측공간(glOrtho) 확인하기](https://github.com/dknife/2024Graphics/blob/main/codes/Ex04_Camera/Ex04_03_ObserverOrtho.py)

[4-4 카메라 렌즈 비교](https://github.com/dknife/2024Graphics/blob/main/codes/Ex04_Camera/0403_twocameras.py)

[4-５ 카메라 렌즈 비교 최종](https://github.com/dknife/2024Graphics/blob/main/codes/Ex04_Camera/twoCameraFinal.py)

#### 카메라 실습 추가

[4-6 원근 카메라 설정과 카메라 위치 잡기](https://github.com/dknife/2024Graphics/blob/main/codes/05CameraWalk/0501_basicCam.py)

[4-7 평면 가시화와 카메라 놓기](https://github.com/dknife/2024Graphics/blob/main/codes/05CameraWalk/0502_CamWithPlane.py)

[4-8 키보드 처리를 통해 카메라 전후 이동](https://github.com/dknife/2024Graphics/blob/main/codes/05CameraWalk/0503_CameraSimpleMove.py)

[4-9 임의의 방향으로 전후진](https://github.com/dknife/2024Graphics/blob/main/codes/05CameraWalk/0503_CameraSimpleMove2.py)

[4-10 넘파이 버전으로 수정한 전후좌우 카메라 이동](https://github.com/dknife/2024Graphics/blob/main/codes/05CameraWalk/0505_CameraSimpleMoveNumpy.py)

### 강의 5 렌더링 속도 개선

[수업 자료](https://github.com/dknife/2024Graphics/raw/main/LN/Lec05_RenderingEfficiency.pdf)

[강의 노트](https://github.com/dknife/2024Graphics/raw/main/LN/Lec05_RenderingEfficiency_pres.pptx)

#### 실습


[5-1 선으로 이루어진 평면 이동](https://github.com/dknife/2024Graphics/blob/main/codes/06RenderEfficiency/0601_SimplePlane.py)

[5-2 25000개 정점으로 느려진 렌더링](https://github.com/dknife/2024Graphics/blob/main/codes/06RenderEfficiency/0602SlowRendering.py)

[5-3 Display List를 사용한 렌러링 속도 개선](https://github.com/dknife/2024Graphics/tree/main/codes/06RenderEfficiency)

[5-4 Display List / Immediat Mode toggle](https://github.com/dknife/2024Graphics/tree/main/codes/06RenderEfficiency)

[5-5 DrawArray 사용](https://github.com/dknife/2024Graphics/blob/main/codes/06RenderEfficiency/0605_DisplayList_DrawArray.py)

[5-6 Vertex Buffer와 Color Buffer](https://github.com/dknife/2024Graphics/blob/main/codes/06RenderEfficiency/0606_DrawArrays_withColor.py)

### 강의 6 메시 읽기

[수업 자료](https://github.com/dknife/2024Graphics/raw/main/LN/Lec06_MeshLoading.pdf)

[강의 노트](https://github.com/dknife/2024Graphics/raw/main/LN/Lec06_MeshLoading_pres.pdf)

#### 실습

[데이터]

* [메시 데이터 예시](https://github.com/dknife/2023Graphics/blob/main/Ex/Ex06/mesh.txt)
* [소 메시 데이터](https://github.com/dknife/2023Graphics/blob/main/Ex/Ex06/cow.txt)
* [두개골 메시](https://github.com/dknife/2023Graphics/blob/main/Ex/Ex06/skull.txt)

[6-1 OpenGL Widget](https://github.com/dknife/2024Graphics/blob/main/codes/Ex06_MeshLoader/Ex06_01_OpenGLEnv.py)

[6-2 그리기 객체 생성](https://github.com/dknife/2024Graphics/blob/main/codes/Ex06_MeshLoader/Ex06_02_OpenGLDraw.py)

[6-3 메시 데이터 읽기](https://github.com/dknife/2024Graphics/blob/main/codes/Ex06_MeshLoader/Ex06_03_MeshLoader_basic.py)

[6-4 메시 그리기 간단한 방식(비효율적)](https://github.com/dknife/2024Graphics/blob/main/codes/Ex06_MeshLoader/Ex06_04_MeshLoader_SimpleDraw.py)

#### 실습 2

[6-5 색상을 넣어보기](https://github.com/dknife/2024Graphics/blob/main/codes/Ex06_MeshLoader/Ex06_05_3DSpace.py)

[6-6 Timer](https://github.com/dknife/2024Graphics/blob/main/codes/Ex06_MeshLoader/Ex06_06_Timer.py)

[6-7 Efficient Mesh Drawing with Display List](https://github.com/dknife/2024Graphics/blob/main/codes/Ex06_MeshLoader/Ex06_07_Mesh_Displaylist.py)

[6-8 Draw with Buffers](https://github.com/dknife/2024Graphics/blob/main/codes/Ex06_MeshLoader/Ex06_08_MeshDrawWithBuffers.py)


### 강의 7 변환과 계층적 모델링

[수업 자료](https://github.com/dknife/2024Graphics/raw/main/LN/Lec07_HierarchicalModeling.pdf)

[강의 노트](https://github.com/dknife/2024Graphics/raw/main/LN/Lec07_HierarchicalModeling_pres.pdf)

#### 실습 1

[Main](https://github.com/dknife/2024Graphics/blob/main/codes/07_Transform/Ex07_01_MeshDraw.py)

[Drawable.py](https://github.com/dknife/2024Graphics/blob/main/codes/07_Transform/Drawable.py)

[MeshLoader.py](https://github.com/dknife/2024Graphics/blob/main/codes/07_Transform/MeshLoader.py)

#### 실습 2
* 위의 Drawable, MeshLoader를 그대로 활용

* 변환 적용 예 1
[Ex0702_Transform.py](https://github.com/dknife/2024Graphics/blob/main/codes/07_Transform/Ex0702_Transform.py)

* 변환 적용 예 2
[Ex0703_CowCircle.py](https://github.com/dknife/2024Graphics/blob/main/codes/07_Transform/Ex0703_CowCircle.py)


#### 실습 3

[로봇 팔을 만들기 위한 준비](https://github.com/dknife/2024Graphics/tree/main/codes/Ex_HierarchicalModels)

[개선 1: 3개의 요소를 관절로 묶기](https://github.com/dknife/2024Graphics/blob/main/codes/Ex_HierarchicalModels/Ex0704_Arms.py)

[개선 2: glScalef를 이용하여 길이가 다른 로봇 팔을 요소를 연결하기](https://github.com/dknife/2024Graphics/blob/main/codes/Ex_HierarchicalModels/Ex0705_ArmsWithScale.py)

#### 프로젝트 1

[계층적 모델링 프로젝트 1 Robot 팔 제어](https://github.com/dknife/2024Graphics/tree/main/codes/Ex_HierarchicalModels/RobotMove)

* [로봇 그리기 개선](https://github.com/dknife/2024Graphics/blob/main/codes/Ex_HierarchicalModels/RobotMove/Robot.py)
* [제어 프로그램 개선](https://github.com/dknife/2024Graphics/blob/main/codes/Ex_HierarchicalModels/RobotMove/Ex0706_RobotMove.py)

#### 프로젝트 2

[태양계 프로젝트]()

* [구 그리기](https://github.com/dknife/2024Graphics/blob/main/codes/Ex_HierarchicalModels/Sphere.py)

  
### 강의 8

[색과 빛 - 강의 자료](https://github.com/dknife/2024Graphics/blob/main/LN/Lec08_Colors_Lights.pdf)

[색과 빛 - 강의 노트](https://github.com/dknife/2024Graphics/blob/main/LN/Lec08_Colors_Lights_pres.pdf)

[정점별 법선 - 강의 자료](https://github.com/dknife/2024Graphics/blob/main/LN/Lec09_PerVertexNormal.pdf)

[정점별 법선 - 강의 노트](https://github.com/dknife/2024Graphics/blob/main/LN/Lec09_PerVertexNormal_pres.pdf)

