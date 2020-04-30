import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton

class voiceSeparator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        fileInputBtn = QPushButton('파일 입력', self)
        separateBtn = QPushButton('음성 분리하기', self)
        fileNameLabel = QLabel('파일 이름', self)

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(fileNameLabel)
        hbox1.addStretch(1)
        hbox1.addWidget(fileInputBtn)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(separateBtn)
        hbox2.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)

        self.setLayout(vbox)
        self.setWindowTitle('Voice Separator')
        self.resize(400, 150)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = voiceSeparator()
   sys.exit(app.exec_())
