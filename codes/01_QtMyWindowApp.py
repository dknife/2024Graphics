
## Qt 임포트
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtWidgets import QLabel, QLineEdit, QVBoxLayout

## 나의 윈도우 클래스를 설계한다
class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('멋진 나의 윈도우')

        self.label = QLabel()
        self.input = QLineEdit()
        self.myLayout = QVBoxLayout()

        self.myLayout.addWidget(self.label)
        self.myLayout.addWidget(self.input)

        container = QWidget()
        container.setLayout(self.myLayout)
        self.setCentralWidget(container)

        self.input.textChanged.connect(self.label.setText)

        

## 앱을 실행한다
import sys
app = QApplication(sys.argv)

window = MyWindow() # 내가 구현한 윈도우 클래스를 사용하자
window.show()

app.exec()