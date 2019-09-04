from PyQt5.Qt import *

from start import start, graph_config
from ui.thread_crawler_ui import Ui_Form


# 增加了一个继承自QThread类的类，重新写了它的run()函数
# run()函数即是新线程需要执行的：执行一个循环；发送计算完成的信号。
class WorkThread(QThread):
    trigger = pyqtSignal()

    def __init__(self):
        super().__init__()

    def run(self):
        start(graph_config)

        self.trigger.emit()

    @classmethod
    def work(cls, timer):
        # 计时器每秒计数
        timer.start(1000)
        # 计时开始
        cls.start()
        # 当获得循环完毕的信号时，停止计数
        cls.trigger.connect(self.timeStop)

    def timeStop(self, timer):
        timer.stop()
        print("运行结束用时", lcdNumber.value())
        global sec
        sec = 0


class MainWindow(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def start_crawl(self):
        print("开始爬虫")
        start(graph_config)

    def stop_crawl(self):
        print("stop crawl")

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