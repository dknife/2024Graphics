[수업전체](https://github.com/dknife/dknife.github.io/wiki/Lecture_Homepage)

### 중간고사 
[중간고사 문제지](https://forms.office.com/r/rsc61Wn0Nm)

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

