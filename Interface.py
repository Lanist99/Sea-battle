import sys
import os
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import *
import Model as md
class UI(QWidget):
    def __init__(self):
        super(UI,self).__init__()
        '''Functions that initializing the UI class'''
        self.image = 'resourses\\Background.jpg'
        self.user_field = md.Field()
        self.ui = uic.loadUi('resourses\\fields.ui')
        self.Start()
        self.step = 1

        self.ui.setFixedSize(1261,761)
        self.rotation = 0
    def Start(self):
        '''Function that activate first window'''
        self.ui.stackedWidget.setCurrentIndex(1)
        self.ui.pushButton.clicked.connect(self.Prepare)
        self.ui.pushButton_2.clicked.connect(self.Rules)
        self.ui.pushButton_3.clicked.connect(self.Exit)
        self.ui.label_2.setPixmap(QtGui.QPixmap('resourses\\background.jpg'))
        self.ui.show()
    def Rules(self):
        '''Function that show instructions'''
        self.ui.stackedWidget.setCurrentIndex(2)
        self.ui.pushButton_back.clicked.connect(self.__init__)
        self.ui.label_3.setPixmap(QtGui.QPixmap('resourses\\background.jpg'))
        self.ui.label_5.setPixmap(QtGui.QPixmap('resourses\\instructions.jpg'))
    def Exit(self):
        '''Exit function'''
        sys.exit(app.exec_())
    def Prepare(self):
        '''Function that activate preparing window. Here user puts ships on his field'''
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.background.setPixmap(QtGui.QPixmap(self.image))
        self.ui.port.setPixmap(QtGui.QPixmap('resourses\\4.jpg'))

        self.ui.continue_button.hide()
        self.ui.continue_button.clicked.connect(self.Battle)
        for i in range(0, 10):
            for x in range(0,10):
                a = self.ui.findChild(QPushButton, 'pushButton_'+str(i)+'_'+str(x))
                a.clicked.connect(self.Put_Ship)


        self.ui.rotat_button.clicked.connect(self.Rotate)
        self.ui.rotat_button_2.clicked.connect(self.__init__)
    def Rotate(self):
        '''Function to rotatr ships. It's change self.rotation. 0 - horizontal 1 0 vertical'''
        if self.rotation == 0:
            self.rotation = 1
            self.ui.label.setText("Корабель буде встановлено: Вертикально")
        else:
            self.rotation = 0
            self.ui.label.setText("Корабель буде встановлено: Горизонтально")
    def Put_Ship(self):
        '''Function that putsh ships on the field. Ships puts in matrix in Model. Function has 10 steps'''
        crds = self.sender().objectName()
        crds = crds.split('_')
        crds = [int(crds[1]), int(crds[2])]

        if self.step == 1:


            if self.rotation == 0 and crds[1]+3 <= 9:
                a = self.user_field.put_ship(4, crds, self.rotation)
                if a != 1:
                    self.ui.s.setGeometry(self.sender().x(),self.sender().y(),40*4,40)
                    self.ui.s.setPixmap(QtGui.QPixmap('resourses\\4.png'))
                    self.step += 1


                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\3.jpg'))
            elif self.rotation == 1 and crds[0]+3 <= 9:
                a = self.user_field.put_ship(4, crds, self.rotation)
                if a != 1:
                    self.ui.s.setGeometry(self.sender().x(), self.sender().y(), 40, 40*4)
                    self.ui.s.setPixmap(QtGui.QPixmap('resourses\\4v.png'))
                    self.step += 1
                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\3.jpg'))

        elif self.step == 2:


            if self.rotation == 0 and crds[1]+2 <= 9:
                a = self.user_field.put_ship(3, crds, self.rotation)
                if a != 1:
                    self.ui.s_2.setGeometry(self.sender().x(),self.sender().y(),40*3,40)
                    self.ui.s_2.setPixmap(QtGui.QPixmap('resourses\\3.png'))
                    self.step += 1


                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\3.jpg'))
            elif self.rotation == 1 and crds[0]+2 <= 9:
                a = self.user_field.put_ship(3, crds, self.rotation)
                if a != 1:
                    self.ui.s_2.setGeometry(self.sender().x(), self.sender().y(), 40, 40*3)
                    self.ui.s_2.setPixmap(QtGui.QPixmap('resourses\\3v.png'))
                    self.step += 1
                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\3.jpg'))

        elif self.step == 3:


            if self.rotation == 0 and crds[1]+2 <= 9:
                a = self.user_field.put_ship(3, crds, self.rotation)
                if a != 1:
                    self.ui.s_3.setGeometry(self.sender().x(),self.sender().y(),40*3,40)
                    self.ui.s_3.setPixmap(QtGui.QPixmap('resourses\\3.png'))
                    self.step += 1


                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\2.jpg'))
            elif self.rotation == 1 and crds[0]+2 <= 9:
                a = self.user_field.put_ship(3, crds, self.rotation)
                if a != 1:
                    self.ui.s_3.setGeometry(self.sender().x(), self.sender().y(), 40, 40*3)
                    self.ui.s_3.setPixmap(QtGui.QPixmap('resourses\\3v.png'))
                    self.step += 1
                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\2.jpg'))

        elif self.step == 4:


            if self.rotation == 0 and crds[1]+1 <= 9:
                a = self.user_field.put_ship(2, crds, self.rotation)
                if a != 1:
                    self.ui.s_4.setGeometry(self.sender().x(),self.sender().y(),40*2,40)
                    self.ui.s_4.setPixmap(QtGui.QPixmap('resourses\\2.png'))
                    self.step += 1


                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\2.jpg'))
            elif self.rotation == 1 and crds[0]+1 <= 9:
                a = self.user_field.put_ship(2, crds, self.rotation)
                if a != 1:
                    self.ui.s_4.setGeometry(self.sender().x(), self.sender().y(), 40, 40*2)
                    self.ui.s_4.setPixmap(QtGui.QPixmap('resourses\\2v.png'))
                    self.step += 1
                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\2.jpg'))

        elif self.step == 5:


            if self.rotation == 0 and crds[1]+1 <= 9:
                a = self.user_field.put_ship(2, crds, self.rotation)
                if a != 1:
                    self.ui.s_5.setGeometry(self.sender().x(),self.sender().y(),40*2,40)
                    self.ui.s_5.setPixmap(QtGui.QPixmap('resourses\\2.png'))
                    self.step += 1


                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\2.jpg'))
            elif self.rotation == 1 and crds[0]+1 <= 9:
                a = self.user_field.put_ship(2, crds, self.rotation)
                if a != 1:
                    self.ui.s_5.setGeometry(self.sender().x(), self.sender().y(), 40, 40*2)
                    self.ui.s_5.setPixmap(QtGui.QPixmap('resourses\\2v.png'))
                    self.step += 1
                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\2.jpg'))

        elif self.step == 6:


            if self.rotation == 0 and crds[1]+1 <= 9:
                a = self.user_field.put_ship(2, crds, self.rotation)
                if a != 1:
                    self.ui.s_6.setGeometry(self.sender().x(),self.sender().y(),40*2,40)
                    self.ui.s_6.setPixmap(QtGui.QPixmap('resourses\\2.png'))
                    self.step += 1


                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\1.jpg'))
            elif self.rotation == 1 and crds[0]+1 <= 9:
                a = self.user_field.put_ship(2, crds, self.rotation)
                if a != 1:
                    self.ui.s_6.setGeometry(self.sender().x(), self.sender().y(), 40, 40*2)
                    self.ui.s_6.setPixmap(QtGui.QPixmap('resourses\\2v.png'))
                    self.step += 1
                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\1.jpg'))

        elif self.step == 7:


            if self.rotation == 0 and crds[1] <= 9:
                a = self.user_field.put_ship(1, crds, self.rotation)
                if a != 1:
                    self.ui.s_7.setGeometry(self.sender().x(),self.sender().y(),40,40)
                    self.ui.s_7.setPixmap(QtGui.QPixmap('resourses\\1.png'))
                    self.step += 1


                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\1.jpg'))
            elif self.rotation == 1 and crds[0] <= 9:
                a = self.user_field.put_ship(1, crds, self.rotation)
                if a != 1:
                    self.ui.s_7.setGeometry(self.sender().x(), self.sender().y(), 40, 40)
                    self.ui.s_7.setPixmap(QtGui.QPixmap('resourses\\1v.png'))
                    self.step += 1
                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\1.jpg'))

        elif self.step == 8:


            if self.rotation == 0 and crds[1] <= 9:
                a = self.user_field.put_ship(1, crds, self.rotation)
                if a != 1:
                    self.ui.s_8.setGeometry(self.sender().x(),self.sender().y(),40,40)
                    self.ui.s_8.setPixmap(QtGui.QPixmap('resourses\\1.png'))
                    self.step += 1


                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\1.jpg'))
            elif self.rotation == 1 and crds[0] <= 9:
                a = self.user_field.put_ship(1, crds, self.rotation)
                if a != 1:
                    self.ui.s_8.setGeometry(self.sender().x(), self.sender().y(), 40, 40)
                    self.ui.s_8.setPixmap(QtGui.QPixmap('resourses\\1v.png'))
                    self.step += 1
                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\1.jpg'))

        elif self.step == 9:


            if self.rotation == 0 and crds[1] <= 9:
                a = self.user_field.put_ship(1, crds, self.rotation)
                if a != 1:
                    self.ui.s_9.setGeometry(self.sender().x(),self.sender().y(),40,40)
                    self.ui.s_9.setPixmap(QtGui.QPixmap('resourses\\1.png'))
                    self.step += 1


                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\1.jpg'))
            elif self.rotation == 1 and crds[0] <= 9:
                a = self.user_field.put_ship(1, crds, self.rotation)
                if a != 1:
                    self.ui.s_9.setGeometry(self.sender().x(), self.sender().y(), 40, 40)
                    self.ui.s_9.setPixmap(QtGui.QPixmap('resourses\\1v.png'))
                    self.step += 1
                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\1.jpg'))

        elif self.step == 10:


            if self.rotation == 0 and crds[1] <= 9:
                a = self.user_field.put_ship(1, crds, self.rotation)
                if a != 1:
                    self.ui.s_10.setGeometry(self.sender().x(),self.sender().y(),40,40)
                    self.ui.s_10.setPixmap(QtGui.QPixmap('resourses\\1.png'))
                    self.step += 1


                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\1.jpg'))
            elif self.rotation == 1 and crds[0] <= 9:
                a = self.user_field.put_ship(1, crds, self.rotation)
                if a != 1:
                    self.ui.s_10.setGeometry(self.sender().x(), self.sender().y(), 40, 40)
                    self.ui.s_10.setPixmap(QtGui.QPixmap('resourses\\1v.png'))
                    self.step += 1
                    self.ui.port.setPixmap(QtGui.QPixmap('resourses\\1.jpg'))

            self.ui.continue_button.show()


    def Battle(self):
        '''Function to activate Battle window. Here the opponent is generating his ships'''
        self.ui.port.hide()
        self.ui.rotat_button.hide()
        self.ui.continue_button.hide()
        self.ui.label.hide()
        self.opp = md.Opponent()
        x = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]

        for i in x:
            self.opp.prepare_ships(i)
        for i in range(0, 10):
            for x in range(0,10):
                a = self.ui.findChild(QPushButton, 'pushButton2_'+str(i)+'_'+str(x))
                a.clicked.connect(self.Shoot)

    def Shoot(self):
        '''Functions that allows users shooting'''
        crds = self.sender().objectName()
        crds = crds.split('_')
        crds = [int(crds[1]), int(crds[2])]
        if self.opp.opfield.field[crds[0]][crds[1]] != 1:
            self.sender().setStyleSheet('background-color: rgb(6, 51, 157);')
            self.sender().setEnabled(False)

            self.OpShoot()

            self.checkFinish()
        else:
            self.sender().setStyleSheet('background-color: rgb(255, 153, 11);')
            self.sender().setEnabled(False)
            self.opp.opfield.field[crds[0]][crds[1]] = 2
            self.OpShoot()
            self.checkFinish()
    def OpShoot(self):
        '''Functions that allows opponent shooting'''
        crd = self.opp.shoot()

        if crd == None:
            return
        if self.user_field.field[crd[0]][crd[1]] != 1:
            for i in range(0, 10):
                for x in range(0, 10):
                    a = self.ui.findChild(QPushButton, 'pushButton_' + str(i) + '_' + str(x))
                    if a.objectName() == 'pushButton_'+str(crd[0])+'_'+str(crd[1]):
                        a.setStyleSheet('background-color: rgb(6, 51, 157);')
                        a.setEnabled(False)
                        self.checkFinish()
        elif self.user_field.field[crd[0]][crd[1]] == 1:
            for i in range(0, 10):
                for x in range(0, 10):
                    a = self.ui.findChild(QPushButton, 'pushButton_' + str(i) + '_' + str(x))
                    if a.objectName() == 'pushButton_' + str(crd[0]) + '_' + str(crd[1]):
                        a.setStyleSheet('background-color: rgb(255, 153, 11);')
                        a.setEnabled(False)
                        self.user_field.field[crd[0]][crd[1]] = 2
                        self.checkFinish()
        else:
            self.checkFinish()
            self.OpShoot()
    def checkFinish(self):
        '''Function that check fields for win or lose.'''
        res1 = 0
        res2 = 0
        for i in self.user_field.field:
            for x in i:
                if x == 1:
                    res1 += 1

        for i in self.opp.opfield.field:
            for x in i:
                if x == 1:
                    res2 += 1

        if res1 == 0:
            self.Rules()
            self.ui.label_4.setPixmap(QtGui.QPixmap('resourses\\Lose.jpg'))
            self.ui.label_5.hide()
            self.ui.label_4.setGeometry(80, 60, 1121, 541)
        if res2 == 0:
            self.Rules()
            self.ui.label_4.setPixmap(QtGui.QPixmap('resourses\\Win.jpg'))
            self.ui.label_5.hide()
            self.ui.label_4.setGeometry(80, 60, 1121, 541)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    sys.exit(app.exec_())
