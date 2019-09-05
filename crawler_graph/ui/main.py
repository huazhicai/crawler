from PyQt5.Qt import *

from start import start, graph_config
from thread_crawler_ui import Ui_Crawler

global sec
sec = 0


# 增加了一个继承自QThread类的类，重新写了它的run()函数
# run()函数即是新线程需要执行的：执行一个循环；发送计算完成的信号。
class WorkThread(QThread):
    trigger = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        start(graph_config)

        self.trigger.emit()


class MainWindow(QWidget, Ui_Crawler):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.timer = QTimer()
        self.timer.timeout.connect(self.count_time)
        self.workThread = WorkThread()

    def start_crawl(self):
        print("开始爬虫")
        self.start_btn.setEnabled(False)
        # 计时器每秒计数
        self.timer.start(1000)
        # 计时开始,调用run方法
        self.workThread.start()
        # 当获得循环完毕的信号时，停止计数
        self.workThread.trigger.connect(self.time_stop)

    def count_time(self):
        global sec
        sec += 1
        # LED显示数字+1
        self.lcdNumber.display(sec)

    def time_stop(self):
        self.timer.stop()
        print("运行结束用时", self.lcdNumber.value())
        self.start_btn.setEnabled(True)
        global sec
        sec = 0

    def stop_crawl(self):
        print("stop crawl")

    def continue_crawl(self):
        pass

    def clean_text(self):
        print("clean text")

    def save(self):
        print("save file")


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    work = MainWindow()

    work.show()
    sys.exit(app.exec_())
