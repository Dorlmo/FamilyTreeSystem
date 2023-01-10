# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import FamilyTree


class Ui_FamilyManegeSystem(object):
    def setupUi(self, FamilyManegeSystem):
        FamilyManegeSystem.setObjectName("FamilyManegeSystem")
        FamilyManegeSystem.resize(800, 600)
        self.verticalWidget = QtWidgets.QWidget(FamilyManegeSystem)
        self.verticalWidget.setGeometry(QtCore.QRect(0, 0, 200, 601))
        self.verticalWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.verticalWidget.setStyleSheet("background-color: rgb(29, 40, 58);")
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.addButton = QtWidgets.QPushButton(self.verticalWidget)
        self.addButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.addButton.setStyleSheet("font: 14pt \"宋体\";\n"
                                     "color: rgb(240, 240, 240);\n"
                                     "background-color: rgb(67, 80, 98);\n"
                                     "")
        self.addButton.setObjectName("addButton")
        self.verticalLayout.addWidget(self.addButton)
        self.manegeButton = QtWidgets.QPushButton(self.verticalWidget)
        self.manegeButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.manegeButton.setStyleSheet("font: 14pt \"宋体\";\n"
                                        "color: rgb(240, 240, 240);\n"
                                        "background-color: rgb(67, 80, 98);\n"
                                        "")
        self.manegeButton.setObjectName("manegeButton")
        self.verticalLayout.addWidget(self.manegeButton)
        self.genealogyButton = QtWidgets.QPushButton(self.verticalWidget)
        self.genealogyButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.genealogyButton.setStyleSheet("font: 14pt \"宋体\";\n"
                                           "color: rgb(240, 240, 240);\n"
                                           "background-color: rgb(67, 80, 98);\n"
                                           "")
        self.genealogyButton.setObjectName("genealogyButton")
        self.verticalLayout.addWidget(self.genealogyButton)
        self.exitButton = QtWidgets.QPushButton(self.verticalWidget)
        self.exitButton.setMaximumSize(QtCore.QSize(16777215, 50))
        self.exitButton.setStyleSheet("font: 14pt \"宋体\";\n"
                                      "color: rgb(240, 240, 240);\n"
                                      "background-color: rgb(67, 80, 98);\n"
                                      "")
        self.exitButton.setObjectName("exitButton")
        self.verticalLayout.addWidget(self.exitButton)
        self.stackedWidget = QtWidgets.QStackedWidget(FamilyManegeSystem)
        self.stackedWidget.setGeometry(QtCore.QRect(200, 0, 600, 600))
        self.stackedWidget.setStyleSheet("background-color: rgb(145, 217, 217);")
        self.stackedWidget.setObjectName("stackedWidget")
        self.addPage = QtWidgets.QWidget()
        self.addPage.setStyleSheet("")
        self.addPage.setObjectName("addPage")
        self.label1 = QtWidgets.QLabel(self.addPage)
        self.label1.setGeometry(QtCore.QRect(60, 120, 100, 50))
        self.label1.setStyleSheet("font: 14pt \"宋体\";")
        self.label1.setObjectName("label1")
        self.label2 = QtWidgets.QLabel(self.addPage)
        self.label2.setGeometry(QtCore.QRect(60, 190, 100, 50))
        self.label2.setStyleSheet("font: 14pt \"宋体\";")
        self.label2.setObjectName("label2")
        self.label3 = QtWidgets.QLabel(self.addPage)
        self.label3.setGeometry(QtCore.QRect(60, 260, 100, 50))
        self.label3.setStyleSheet("font: 14pt \"宋体\";")
        self.label3.setObjectName("label3")
        self.saveButton = QtWidgets.QPushButton(self.addPage)
        self.saveButton.setGeometry(QtCore.QRect(170, 400, 200, 50))
        self.saveButton.setStyleSheet("font: 14pt \"宋体\";\n"
                                      "background-color: rgb(240, 240, 240);")
        self.saveButton.setObjectName("saveButton")
        self.nameLineEdit = QtWidgets.QLineEdit(self.addPage)
        self.nameLineEdit.setGeometry(QtCore.QRect(190, 120, 300, 50))
        self.nameLineEdit.setStyleSheet("font: 14pt \"宋体\";\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(255, 255, 255);")
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.fatherLineEdit = QtWidgets.QLineEdit(self.addPage)
        self.fatherLineEdit.setGeometry(QtCore.QRect(190, 190, 300, 50))
        self.fatherLineEdit.setStyleSheet("font: 14pt \"宋体\";\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(255, 255, 255);")
        self.fatherLineEdit.setObjectName("fatherLineEdit")
        self.motherLineEdit = QtWidgets.QLineEdit(self.addPage)
        self.motherLineEdit.setGeometry(QtCore.QRect(190, 260, 300, 50))
        self.motherLineEdit.setStyleSheet("font: 14pt \"宋体\";\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(255, 255, 255);")
        self.motherLineEdit.setText("")
        self.motherLineEdit.setObjectName("motherLineEdit")
        self.loadDataButton = QtWidgets.QPushButton(self.addPage)
        self.loadDataButton.setGeometry(QtCore.QRect(470, 45, 110, 30))
        self.loadDataButton.setStyleSheet("font: 9pt \"宋体\";\n"
                                          "background-color: rgb(200, 200, 200);")
        self.loadDataButton.setObjectName("loadDataButton")
        self.label = QtWidgets.QLabel(self.addPage)
        self.label.setGeometry(QtCore.QRect(60, 320, 161, 21))
        self.label.setStyleSheet("font: 10pt \"宋体\";\n"
                                 "color: rgb(243, 243, 243);")
        self.label.setObjectName("label")
        self.stackedWidget.addWidget(self.addPage)
        self.manegePage = QtWidgets.QWidget()
        self.manegePage.setObjectName("manegePage")
        self.label5 = QtWidgets.QLabel(self.manegePage)
        self.label5.setGeometry(QtCore.QRect(50, 60, 100, 50))
        self.label5.setStyleSheet("font: 14pt \"宋体\";")
        self.label5.setObjectName("label5")
        self.findTextEdit = QtWidgets.QLineEdit(self.manegePage)
        self.findTextEdit.setGeometry(QtCore.QRect(180, 60, 300, 50))
        self.findTextEdit.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.findTextEdit.setStyleSheet("font: 14pt \"宋体\";\n"
                                        "color: rgb(0, 0, 0);\n"
                                        "background-color: rgb(255, 255, 255);")
        self.findTextEdit.setObjectName("findTextEdit")
        self.plainText = QtWidgets.QPlainTextEdit(self.manegePage)
        self.plainText.setGeometry(QtCore.QRect(50, 140, 501, 301))
        self.plainText.setStyleSheet("font: 14pt \"宋体\";\n"
                                     "color: rgb(0, 0, 0);\n"
                                     "background-color: rgb(240, 240, 240);")
        self.plainText.setObjectName("plainText")
        self.deleteButton = QtWidgets.QPushButton(self.manegePage)
        self.deleteButton.setGeometry(QtCore.QRect(460, 490, 93, 28))
        self.deleteButton.setStyleSheet("font: 12pt \"宋体\";\n"
                                        "background-color: rgb(200, 200, 200);")
        self.deleteButton.setObjectName("deleteButton")
        self.findButton = QtWidgets.QPushButton(self.manegePage)
        self.findButton.setGeometry(QtCore.QRect(60, 470, 200, 50))
        self.findButton.setStyleSheet("font: 14pt \"宋体\";\n"
                                      "background-color: rgb(240, 240, 240);")
        self.findButton.setObjectName("findButton")
        self.stackedWidget.addWidget(self.manegePage)
        self.genealogyPage = QtWidgets.QWidget()
        self.genealogyPage.setObjectName("genealogyPage")
        self.genealogyText = QtWidgets.QTextEdit(self.genealogyPage)
        self.genealogyText.setGeometry(QtCore.QRect(40, 140, 541, 371))
        self.genealogyText.setStyleSheet("font: 14pt \"宋体\";\n"
                                         "color: rgb(0, 0, 0);\n"
                                         "background-color: rgb(240, 240, 240);")
        self.genealogyText.setObjectName("genealogyText")
        self.label5_2 = QtWidgets.QLabel(self.genealogyPage)
        self.label5_2.setGeometry(QtCore.QRect(40, 40, 100, 50))
        self.label5_2.setStyleSheet("font: 14pt \"宋体\";")
        self.label5_2.setObjectName("label5_2")
        self.findTextEdit_2 = QtWidgets.QLineEdit(self.genealogyPage)
        self.findTextEdit_2.setGeometry(QtCore.QRect(140, 40, 300, 50))
        self.findTextEdit_2.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.findTextEdit_2.setStyleSheet("font: 14pt \"宋体\";\n"
                                          "color: rgb(0, 0, 0);\n"
                                          "background-color: rgb(255, 255, 255);")
        self.findTextEdit_2.setObjectName("findTextEdit_2")
        self.findButton_2 = QtWidgets.QPushButton(self.genealogyPage)
        self.findButton_2.setGeometry(QtCore.QRect(450, 40, 100, 50))
        self.findButton_2.setStyleSheet("font: 14pt \"宋体\";\n"
                                        "background-color: rgb(240, 240, 240);")
        self.findButton_2.setObjectName("findButton_2")
        self.stackedWidget.addWidget(self.genealogyPage)

        self.retranslateUi(FamilyManegeSystem)
        self.stackedWidget.setCurrentIndex(0)

        self.loadDataButton.clicked.connect(self.loadDefaultData)  # type: ignore
        self.addButton.clicked.connect(self.actionSwitchPage1)  # type: ignore
        self.manegeButton.clicked.connect(self.actionSwitchPage2)  # type: ignore
        self.genealogyButton.clicked.connect(self.actionSwitchPage3)  # type: ignore
        self.exitButton.clicked.connect(self.actionExit)  # type: ignore
        self.saveButton.clicked.connect(self.actionSaveMember)  # type: ignore
        self.findButton.clicked.connect(self.actionFindMember)  # type: ignore
        self.deleteButton.clicked.connect(self.actionDeleteMember)  # type: ignore
        self.findButton_2.clicked.connect(self.actionGetGenelogy)  # type: ignore

        QtCore.QMetaObject.connectSlotsByName(FamilyManegeSystem)

    def retranslateUi(self, FamilyManegeSystem):
        _translate = QtCore.QCoreApplication.translate
        FamilyManegeSystem.setWindowTitle(_translate("FamilyManegeSystem", "家庭管理系统"))
        self.addButton.setText(_translate("FamilyManegeSystem", "添加成员"))
        self.manegeButton.setText(_translate("FamilyManegeSystem", "成员管理"))
        self.genealogyButton.setText(_translate("FamilyManegeSystem", "查看族谱"))
        self.exitButton.setText(_translate("FamilyManegeSystem", "退出"))
        self.label1.setText(_translate("FamilyManegeSystem", "名字："))
        self.label2.setText(_translate("FamilyManegeSystem", "父亲："))
        self.label3.setText(_translate("FamilyManegeSystem", "母亲："))
        self.saveButton.setText(_translate("FamilyManegeSystem", "保存"))
        self.loadDataButton.setText(_translate("FamilyManegeSystem", "加载默认数据"))
        self.label.setText(_translate("FamilyManegeSystem", "注：缺省输入则为空"))
        self.label5.setText(_translate("FamilyManegeSystem", "名字："))
        self.deleteButton.setText(_translate("FamilyManegeSystem", "删除"))
        self.findButton.setText(_translate("FamilyManegeSystem", "查找"))
        self.label5_2.setText(_translate("FamilyManegeSystem", "名字："))
        self.findButton_2.setText(_translate("FamilyManegeSystem", "查找"))

    def actionSwitchPage1(self):
        self.stackedWidget.setCurrentIndex(0)

    def actionSwitchPage2(self):
        self.stackedWidget.setCurrentIndex(1)

    def actionSwitchPage3(self):
        self.stackedWidget.setCurrentIndex(2)

    def actionExit(self):
        exit(0)

    def loadDefaultData(self):
        FamilyTree.loadDefaultData()
        self.showPopup("载入成功")

    def actionSaveMember(self):
        name = self.nameLineEdit.text()
        father = self.fatherLineEdit.text()
        mother = self.motherLineEdit.text()
        booleanTest = FamilyTree.add_member(name, father, mother)
        if booleanTest:
            self.showPopup("保存成功")
        else:
            self.showPopup("保存失败")

    def actionFindMember(self):
        name = self.findTextEdit.text()
        output = FamilyTree.getMessage(name)
        self.plainText.setPlainText(output)

    def actionDeleteMember(self):
        name = self.findTextEdit.text()
        FamilyTree.remove(name)
        self.showPopup("删除成功")

    def actionGetGenelogy(self):
        name = self.findTextEdit_2.text()
        output = FamilyTree.getGenology(name)
        self.genealogyText.setPlainText(output)

    def showPopup(self, text):
        popUp = QtWidgets.QMessageBox()
        popUp.setText(text)
        popUp.setWindowTitle("消息")
        popUp.exec()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    FamilyManegeSystem = QtWidgets.QWidget()
    ui = Ui_FamilyManegeSystem()
    ui.setupUi(FamilyManegeSystem)
    FamilyManegeSystem.show()
    sys.exit(app.exec_())
