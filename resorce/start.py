# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
#
#
# class ListWidget(QListWidget):
#     def clicked(self, item):
#         QMessageBox.information(self, "ListWidget", "你选择了: " + item.text())
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     # 实例化对象，目的只是单纯的使用里面的槽函数............
#     listWidget = ListWidget()
#
#     # 设置初始大小，增加条目，设置标题
#     listWidget.resize(300, 120)
#     listWidget.addItem("Item 1")
#     listWidget.addItem("Item 2")
#     listWidget.addItem("Item 3")
#     listWidget.addItem("Item 4")
#     listWidget.setWindowTitle('QListwidget 例子')
#
#     # 单击触发绑定的槽函数
#     listWidget.itemClicked.connect(listWidget.clicked)
#
#     listWidget.show()
#     sys.exit(app.exec_())


# import sys
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QAbstractItemView
# from PyQt5.QtCore import QStringListModel
# from PyQt5 import QtWidgets


# class ListViewDemo(QWidget):
#     def __init__(self, parent=None):
#         super(ListViewDemo, self).__init__(parent)
#         # 设置初始大小与标题
#         self.resize(300, 270)
#         self.setWindowTitle('QListView 多选问题')
#
#         # 垂直布局
#         self.layout = QVBoxLayout()
#
#         # 实例化列表视图
#         self.listview = QListView()
#
#         # 实例化列表模型，添加数据
#         self.slm = QStringListModel()
#         self.qList = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6', 'Item 7', 'Item 8', 'Item 9']
#
#         # 设置模型列表视图，加载数据列表
#         self.slm.setStringList(self.qList)
#
#         # 设置列表视图的模型
#         self.listview.setModel(self.slm)
#
#         # 多选
#         self.listview.setSelectionMode(QAbstractItemView.ExtendedSelection)
#         # 不能对表格进行修改（双击重命名等）
#         self.listview.setEditTriggers(QAbstractItemView.NoEditTriggers)
#
#         self.label_dqxz = QtWidgets.QLabel()
#         self.label_dqxz.setText("当前选择：-")
#
#         # 单击触发自定义的槽函数
#         self.listview.clicked.connect(self.clicked)
#
#         # 设置窗口布局，加载控件
#         self.layout.addWidget(self.listview)
#         self.layout.addWidget(self.label_dqxz)
#         self.setLayout(self.layout)
#
#     def clicked(self):
#         textlist = ''
#         for i in self.listview.selectedIndexes():
#             text = i.data()
#             textlist = textlist + ' ' + text
#         self.label_dqxz.setText('当前选择：' + textlist)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = ListViewDemo()
#     win.show()
#     sys.exit(app.exec_())


# from pypinyin import lazy_pinyin
#
# a = ['中国人', '啊', '你好', '台湾人']
# b = [''.join(lazy_pinyin(_)) for _ in a]
# print(sorted(b))

seven = {'A': ["上海", "北京", "天津", "广州", "深圳", "杭州", "重庆"]}
print(tuple(seven.keys()))
print(tuple(seven.values()))

print(seven.items())
print(type(seven.items()))
print(list(seven.items()))
print(tuple(seven.items()))


# # from __future__ import unicode_literals
# from pypinyin import lazy_pinyin
#
#
# def sort_pinyin(hanzi_list):
#     hanzi_list_pinyin=[]
#     hanzi_list_pinyin_alias_dict={}
#     for single_str in hanzi_list:
#         py_r = lazy_pinyin(single_str)
#         # print("整理下")
#         single_str_py=''
#         for py_list in py_r:
#             single_str_py=single_str_py+py_list
#         hanzi_list_pinyin.append(single_str_py)
#         hanzi_list_pinyin_alias_dict[single_str_py]=single_str
#     hanzi_list_pinyin.sort()
#     sorted_hanzi_list=[]
#     for single_str_py in hanzi_list_pinyin:
#         sorted_hanzi_list.append(hanzi_list_pinyin_alias_dict[single_str_py])
#     return sorted_hanzi_list
#
# str=['床前', '明月', '光','疑是','地上霜','举头','望','明日','低头','思','故乡']
# print(str)
# str=sort_pinyin(str)
# print(str)
