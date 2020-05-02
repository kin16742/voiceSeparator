import sys
from wavToText import *
from videoToWav import *
from PyQt5.QtWidgets import *


class voiceSeparator(QWidget):

    def __init__(self):
        super().__init__()
        self.separateBtn = QPushButton('음성 분리')
        self.fileInputBtn = QPushButton('파일 입력')
        self.fileName = QLineEdit()
        self.initUI()

    def initUI(self):
        self.fileName.setEnabled(False)
        self.fileName.setFixedWidth(300)
        self.fileName.setStyleSheet("background: white;")

        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.fileName)
        hbox1.addStretch(1)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        hbox2.addWidget(self.fileInputBtn)
        hbox2.addStretch(1)
        hbox2.addWidget(self.separateBtn)
        hbox2.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox1)
        vbox.addStretch(1)
        vbox.addLayout(hbox2)
        vbox.addStretch(1)

        self.fileInputBtn.clicked.connect(self.fileInput)
        self.separateBtn.clicked.connect(self.separate)

        self.setLayout(vbox)
        self.setWindowTitle('Voice Separator')
        self.resize(400, 100)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def fileInput(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            self.fileName.setText(fname[0])
        else:
            QMessageBox.about(self, "warning", "파일을 선택하지 않았습니다.")

    def separate(self):
        path = self.fileName.text()

        if path.split('.')[-1] == 'mp4':
            wavToText(videoToWav(path))
        else:
            wavToText(path)

        msg = QMessageBox()
        msg.setWindowTitle('음성 분리 완료')
        msg.setText(path.split('/')[-1].split('.')[0] + '.txt로 저장되었습니다!')
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = voiceSeparator()
    sys.exit(app.exec_())
