import sys
from PyQt5.QtWidgets import QApplication, QWidget

class voiceSeparator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Voice Separator')
        self.move(300, 300)
        self.resize(400, 200)
        self.show()

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = voiceSeparator()
   sys.exit(app.exec_())
