# import os
# from PyQt5.Qt import *
# from dlg import OverrideDialog
# from start import start, graph_config
# from ui.thread_crawler_ui import Ui_Crawler
#
# global sec
# sec = 0
#
#
# # 增加了一个继承自QThread类的类，重新写了它的run()函数
# # run()函数即是新线程需要执行的：执行一个循环；发送计算完成的信号。
# class WorkThread(QThread):
#     trigger = pyqtSignal()
#
#     def __init__(self, qt_text):
#         super().__init__()
#         self.qt_text = qt_text
#
#     def run(self):
#         start(graph_config, self.qt_text)
#         self.trigger.emit()
#
#
# class MainWindow(QWidget, Ui_Crawler):
#
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setupUi(self)
#         self.timer = QTimer()
#         self.timer.timeout.connect(self.count_time)
#         self.workThread = WorkThread(self.textBrowser)
#
#         cursor = self.textBrowser.textCursor()
#         self.textBrowser.moveCursor(cursor.End)
#
#     def start_crawl(self):
#         self.textBrowser.append('<font color="red">Start Crawling...\n</font>')
#         self.start_btn.setEnabled(False)
#         # 计时器每秒计数
#         self.timer.start(1000)
#         # 计时开始,调用run方法
#         self.workThread.start()
#
#         # 当获得循环完毕的信号时，停止计数
#         self.workThread.trigger.connect(self.time_stop)
#
#     def count_time(self):
#         global sec
#         sec += 1
#         # LED显示数字+1
#         self.lcdNumber.display(sec)
#
#     def time_stop(self):
#         self.timer.stop()
#         print("运行结束用时", self.lcdNumber.value())
#         global sec
#         sec = 0
#         self.textBrowser.append('<font color="red">Crawl Done</font>')
#         self.start_btn.setEnabled(True)
#
#     def stop_crawl(self):
#         print("stop crawl")
#         self.workThread.wait()
#         self.stop_btn.setEnabled(False)
#         # self.start_btn.setEnabled(True)
#
#     def continue_crawl(self):
#         print('继续爬虫')
#         self.textBrowser.append("the button invalid temporarily")
#
#     def clean_text(self):
#         print("clean text")
#         self.textBrowser.clear()
#         self.textBrowser.update()
#
#     def close(self):
#         self.textBrowser.close()
#
#     def save(self):
#         print("save file")
#         str_text = self.textBrowser.toPlainText()
#         print(type(str_text))
#         saveGraphDir = os.path.join(os.getcwd())
#         filename = QFileDialog.getSaveFileName(self,
#                                                'Save Graph',
#                                                saveGraphDir,
#                                                "All Files (*);;Text Files (*.txt)")
#         if filename:
#             if type(filename) == tuple:
#                 filename = str(filename[0])
#             else:
#                 filename = str(filename)
#
#             if filename.strip() == '':
#                 QMessageBox(QMessageBox.Warning, "文件名不能为空", QMessageBox.Ok, self)
#
#                 if not filename.endswith('.txt'):
#                     filename = filename + '.txt'
#
#                 if os.path.exists(filename):
#                     # 此文件已存在
#                     overrideDlg = OverrideDialog()
#                     if overrideDlg.exec_():
#                         with open(filename, 'w') as f:
#                             f.write(str_text)
#                     else:
#                         return False
#
#
# if __name__ == '__main__':
#     import sys
#
#     app = QApplication(sys.argv)
#
#     work = MainWindow()
#
#     work.show()
#     sys.exit(app.exec_())
