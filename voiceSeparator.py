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
        self.notice = QLabel('wav, mp4 파일만 가능합니다.')
        self.initUI()

    def initUI(self):
        self.fileName.setEnabled(False)
        self.fileName.setFixedWidth(300)
        self.fileName.setStyleSheet("background: white;")

        hboxFileName = QHBoxLayout()
        hboxFileName.addStretch(1)
        hboxFileName.addWidget(self.fileName)
        hboxFileName.addStretch(1)

        hboxNotice = QHBoxLayout()
        hboxNotice.addStretch(1)
        hboxNotice.addWidget(self.notice)
        hboxNotice.addStretch(1)

        hboxButtons = QHBoxLayout()
        hboxButtons.addStretch(1)
        hboxButtons.addWidget(self.fileInputBtn)
        hboxButtons.addStretch(1)
        hboxButtons.addWidget(self.separateBtn)
        hboxButtons.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hboxFileName)
        vbox.addLayout(hboxNotice)
        vbox.addStretch(1)
        vbox.addLayout(hboxButtons)
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

    def messageBox(self, text):
        msg = QMessageBox()
        msg.setWindowTitle('Notice')
        msg.setText(text)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def separate(self):
        path = self.fileName.text()
        fileType = path.split('.')[-1]

        if fileType == 'mp4':
            wavToText(videoToWav(path))
            self.messageBox('음성 분리 완료!\n' + path.split('/')[-1].split('.')[0] + '.txt로 저장되었습니다!')
        elif fileType == 'wav':
            wavToText(path)
            self.messageBox('음성 분리 완료!\n' + path.split('/')[-1].split('.')[0] + '.txt로 저장되었습니다!')
        else:
            self.messageBox('잘못된 파일 형식입니다!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = voiceSeparator()
    sys.exit(app.exec_())
