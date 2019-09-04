from PyQt5.Qt import *
import sys
import time
import threading


class MyWindow(QDialog, QWidget):
    sigSetTime = pyqtSignal(str)  ####信号定义

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setFont(QFont("Roman times", 14))  #####设置字体
        self.resize(200, 50)
        self.mainlayout = QGridLayout(self)
        self.timeLabel = QLabel()
        self.timeLabel.setText(u"时间：")
        self.mainlayout.addWidget(self.timeLabel, 0, 0, 1, 1)
        self.timeLineEdit = QLineEdit()
        self.mainlayout.addWidget(self.timeLineEdit, 0, 1, 1, 1)
        self.sigSetTime.connect(self.setTime)  ####信号槽连接
        t = threading.Thread(target=self.getTimeAndSetTime, args=(self.sigSetTime,))
        t.setDaemon(True)
        t.start()

    def setTime(self, str_time):
        self.timeLineEdit.setText(str_time)

    def getTimeAndSetTime(self, setTimeSignal):
        while True:
            setTimeSignal.emit(str(time.localtime().tm_hour) + ":" + str(time.localtime().tm_min) + ":" + str(
                time.localtime().tm_sec))  ######信号换发
            time.sleep(1)


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
