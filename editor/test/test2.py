# coding:utf-8

# !/usr/bin/env python

############################################################################
##
## Copyright (C) 2005-2005 Trolltech AS. All rights reserved.
##
## This file is part of the example classes of the Qt Toolkit.
##
## This file may be used under the terms of the GNU General Public
## License version 2.0 as published by the Free Software Foundation
## and appearing in the file LICENSE.GPL included in the packaging of
## this file.  Please review the following information to ensure GNU
## General Public Licensing requirements will be met:
## http://www.trolltech.com/products/qt/opensource.html
##
## If you are unsure which license is appropriate for your use, please
## review the following information:
## http://www.trolltech.com/products/qt/licensing.html or contact the
## sales department at sales@trolltech.com.
##
## This file is provided AS IS with NO WARRANTY OF ANY KIND, INCLUDING THE
## WARRANTY OF DESIGN, MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE.
##
############################################################################

# This is only needed for Python v2 but is harmless for Python v3.
# import sip
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# sip.setapi('QVariant', 2)

from math import cos, pi, sin


class RenderArea(QWidget):
    def __init__(self, path, parent=None):
        super(RenderArea, self).__init__(parent)

        self.path = path

        self.penWidth = 1
        self.rotationAngle = 0
        self.setBackgroundRole(QPalette.Base)

    def minimumSizeHint(self):
        return QSize(50, 50)

    def sizeHint(self):
        return QSize(100, 100)

    def setFillRule(self, rule):
        self.path.setFillRule(rule)
        self.update()

    def setFillGradient(self, color1, color2):
        self.fillColor1 = color1
        self.fillColor2 = color2
        self.update()

    def setPenWidth(self, width):
        self.penWidth = width
        self.update()

    def setPenColor(self, color):
        self.penColor = color
        self.update()

    def setRotationAngle(self, degrees):
        self.rotationAngle = degrees
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.scale(self.width() / 100.0, self.height() / 100.0)
        painter.translate(50.0, 50.0)
        painter.rotate(-self.rotationAngle)
        painter.translate(-50.0, -50.0)

        painter.setPen(QPen(self.penColor, self.penWidth,
                            Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        gradient = QLinearGradient(0, 0, 0, 100)
        gradient.setColorAt(0.0, self.fillColor1)
        gradient.setColorAt(1.0, self.fillColor2)
        painter.setBrush(QBrush(gradient))
        painter.drawPath(self.path)


class Window(QWidget):
    NumRenderAreas = 9   # 数字渲染区

    def __init__(self):
        super(Window, self).__init__()

        # 子空件绘画路径对象， 画矩形
        rectPath = QPainterPath()
        rectPath.moveTo(20.0, 30.0)
        rectPath.lineTo(80.0, 30.0)
        rectPath.lineTo(80.0, 70.0)
        rectPath.lineTo(20.0, 70.0)
        rectPath.closeSubpath()  # 关闭当前子路径，开启下一个路径

        # 画圆角矩形
        roundRectPath = QPainterPath()
        roundRectPath.moveTo(80.0, 35.0)
        roundRectPath.arcTo(70.0, 30.0, 10.0, 10.0, 0.0, 90.0)
        roundRectPath.lineTo(25.0, 30.0)
        roundRectPath.arcTo(20.0, 30.0, 10.0, 10.0, 90.0, 90.0)
        roundRectPath.lineTo(20.0, 65.0)
        roundRectPath.arcTo(20.0, 60.0, 10.0, 10.0, 180.0, 90.0)
        roundRectPath.lineTo(75.0, 70.0)
        roundRectPath.arcTo(70.0, 60.0, 10.0, 10.0, 270.0, 90.0)
        roundRectPath.closeSubpath()  # 关闭当前子路径，开启下一个路径

        # 画椭圆形
        ellipsePath = QPainterPath()
        ellipsePath.moveTo(80.0, 50.0)
        ellipsePath.arcTo(20.0, 30.0, 60.0, 40.0, 0.0, 360.0)
        ellipsePath.closeSubpath()

        # 画
        piePath = QPainterPath()
        piePath.moveTo(50.0, 50.0)
        piePath.lineTo(65.0, 32.6795)
        piePath.arcTo(20.0, 30.0, 60.0, 40.0, 60.0, 240.0)
        piePath.closeSubpath()

        # 画多边形
        polygonPath = QPainterPath()
        polygonPath.moveTo(10.0, 80.0)
        polygonPath.lineTo(20.0, 10.0)
        polygonPath.lineTo(80.0, 30.0)
        polygonPath.lineTo(90.0, 70.0)
        polygonPath.closeSubpath()

        # 画群组
        groupPath = QPainterPath()
        groupPath.moveTo(60.0, 40.0)
        groupPath.arcTo(20.0, 20.0, 40.0, 40.0, 0.0, 360.0)
        groupPath.moveTo(40.0, 40.0)
        groupPath.lineTo(40.0, 80.0)
        groupPath.lineTo(80.0, 80.0)
        groupPath.lineTo(80.0, 40.0)
        groupPath.closeSubpath()

        textPath = QPainterPath()
        timesFont = QFont("Times", 50)
        timesFont.setStyleStrategy(QFont.ForceOutline)
        textPath.addText(10, 70, timesFont, "Qt")

        bezierPath = QPainterPath()
        bezierPath.moveTo(20, 30)
        bezierPath.cubicTo(80, 0, 50, 50, 80, 80)

        starPath = QPainterPath()
        starPath.moveTo(90, 50)
        for i in range(1, 5):
            starPath.lineTo(50 + 40 * cos(0.8 * i * pi),
                            50 + 40 * sin(0.8 * i * pi))
        starPath.closeSubpath()

        self.renderAreas = [RenderArea(rectPath), RenderArea(roundRectPath),
                            RenderArea(ellipsePath), RenderArea(piePath),
                            RenderArea(polygonPath), RenderArea(groupPath),
                            RenderArea(textPath), RenderArea(bezierPath),
                            RenderArea(starPath)]
        assert len(self.renderAreas) == 9

        self.fillRuleComboBox = QComboBox()
        self.fillRuleComboBox.addItem("Odd Even", Qt.OddEvenFill)
        self.fillRuleComboBox.addItem("Winding", Qt.WindingFill)

        fillRuleLabel = QLabel("Fill &Rule:")
        fillRuleLabel.setBuddy(self.fillRuleComboBox)

        self.fillColor1ComboBox = QComboBox()
        self.populateWithColors(self.fillColor1ComboBox)
        self.fillColor1ComboBox.setCurrentIndex(
            self.fillColor1ComboBox.findText("mediumslateblue"))

        self.fillColor2ComboBox = QComboBox()
        self.populateWithColors(self.fillColor2ComboBox)
        self.fillColor2ComboBox.setCurrentIndex(
            self.fillColor2ComboBox.findText("cornsilk"))

        fillGradientLabel = QLabel("&Fill Gradient:")
        fillGradientLabel.setBuddy(self.fillColor1ComboBox)

        fillToLabel = QLabel("to")
        fillToLabel.setSizePolicy(QSizePolicy.Fixed,
                                  QSizePolicy.Fixed)

        self.penWidthSpinBox = QSpinBox()
        self.penWidthSpinBox.setRange(0, 20)

        penWidthLabel = QLabel("&Pen Width:")
        penWidthLabel.setBuddy(self.penWidthSpinBox)

        self.penColorComboBox = QComboBox()
        self.populateWithColors(self.penColorComboBox)
        self.penColorComboBox.setCurrentIndex(
            self.penColorComboBox.findText('darkslateblue'))

        penColorLabel = QLabel("Pen &Color:")
        penColorLabel.setBuddy(self.penColorComboBox)

        self.rotationAngleSpinBox = QSpinBox()
        self.rotationAngleSpinBox.setRange(0, 359)
        self.rotationAngleSpinBox.setWrapping(True)
        self.rotationAngleSpinBox.setSuffix('\xB0')

        rotationAngleLabel = QLabel("&Rotation Angle:")
        rotationAngleLabel.setBuddy(self.rotationAngleSpinBox)

        self.fillRuleComboBox.activated.connect(self.fillRuleChanged)
        self.fillColor1ComboBox.activated.connect(self.fillGradientChanged)
        self.fillColor2ComboBox.activated.connect(self.fillGradientChanged)
        self.penColorComboBox.activated.connect(self.penColorChanged)

        for i in range(Window.NumRenderAreas):
            self.penWidthSpinBox.valueChanged.connect(self.renderAreas[i].setPenWidth)
            self.rotationAngleSpinBox.valueChanged.connect(self.renderAreas[i].setRotationAngle)

        topLayout = QGridLayout()
        for i in range(Window.NumRenderAreas):
            topLayout.addWidget(self.renderAreas[i], i / 3, i % 3)

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 4)
        mainLayout.addWidget(fillRuleLabel, 1, 0)
        mainLayout.addWidget(self.fillRuleComboBox, 1, 1, 1, 3)
        mainLayout.addWidget(fillGradientLabel, 2, 0)
        mainLayout.addWidget(self.fillColor1ComboBox, 2, 1)
        mainLayout.addWidget(fillToLabel, 2, 2)
        mainLayout.addWidget(self.fillColor2ComboBox, 2, 3)
        mainLayout.addWidget(penWidthLabel, 3, 0)
        mainLayout.addWidget(self.penWidthSpinBox, 3, 1, 1, 3)
        mainLayout.addWidget(penColorLabel, 4, 0)
        mainLayout.addWidget(self.penColorComboBox, 4, 1, 1, 3)
        mainLayout.addWidget(rotationAngleLabel, 5, 0)
        mainLayout.addWidget(self.rotationAngleSpinBox, 5, 1, 1, 3)
        self.setLayout(mainLayout)

        self.fillRuleChanged()
        self.fillGradientChanged()
        self.penColorChanged()
        self.penWidthSpinBox.setValue(2)

        self.setWindowTitle("Painter Paths")

    def fillRuleChanged(self):
        rule = Qt.FillRule(self.currentItemData(self.fillRuleComboBox))

        for i in range(Window.NumRenderAreas):
            self.renderAreas[i].setFillRule(rule)

    def fillGradientChanged(self):
        color1 = QColor(self.currentItemData(self.fillColor1ComboBox))
        color2 = QColor(self.currentItemData(self.fillColor2ComboBox))

        for i in range(Window.NumRenderAreas):
            self.renderAreas[i].setFillGradient(color1, color2)

    def penColorChanged(self):
        color = QColor(self.currentItemData(self.penColorComboBox))

        for i in range(Window.NumRenderAreas):
            self.renderAreas[i].setPenColor(color)

    def populateWithColors(self, comboBox):
        colorNames = QColor.colorNames()
        for name in colorNames:
            comboBox.addItem(name, name)

    def currentItemData(self, comboBox):
        return comboBox.itemData(comboBox.currentIndex())


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
