import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtCore import QCoreApplication

from tela_inicio import Tela_Inicio
from tela_cadastro import Tela_Cadastro
from tela_busca import Tela_Busca

from pessoa import Pessoa
from cadastro import Cadastro

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()

        self.tela_inicio = Tela_Inicio()
        self.tela_inicio.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_busca = Tela_Busca()
        self.tela_busca.setupUi(self.stack2)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)

class Main(QMainWindow, Ui_Main):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)

        self.cad = Cadastro()
        self.tela_inicio.pushButton.clicked.connect(self.abrirTelaCadastro)
        self.tela_inicio.pushButton_2.clicked.connect(self.abrirTelaBuscar)

        self.tela_cadastro.pushButton.clicked.connect(self.botaoCadastrar)
        self.tela_busca.pushButton.clicked.connect(self.botaoBuscar)
        self.tela_busca.pushButton_2.clicked.connect(self.abrirTelaInicio)

    def abrirTelaCadastro(self):
        self.QtStack.setCurrentIndex(1)

    def abrirTelaBuscar(self):
        self.QtStack.setCurrentIndex(2)

    def abrirTelaInicio(self):
        self.QtStack.setCurrentIndex(0)

    def botaoCadastrar(self):
        nome = self.tela_cadastro.lineEdit.text()
        cpf = self.tela_cadastro.lineEdit_2.text()
        end = self.tela_cadastro.lineEdit_3.text()
        dataNasc = self.tela_cadastro.lineEdit_4.text()
        if (nome != '' and cpf != '' and end != '' and dataNasc != ''):
            p = Pessoa(nome, cpf, end, dataNasc)
            if (self.cad.cadastrar(p)):
                QMessageBox.information(None, 'POO2', 'Cadastro realizado!')
                self.tela_cadastro.lineEdit.setText('')
                self.tela_cadastro.lineEdit_2.setText('')
                self.tela_cadastro.lineEdit_3.setText('')
                self.tela_cadastro.lineEdit_4.setText('')
            else:
                QMessageBox.information(None, 'POO2','O CPF informado já esta cadastrado!')
        else:
            QMessageBox.information(None, 'POO2', 'Não podem existir campos vazios!')

        self.QtStack.setCurrentIndex(0)

    def botaoBuscar(self):
        cpf = self.tela_busca.lineEdit.text()
        p = self.cad.buscar(cpf)
        if (p != None):
            self.tela_busca.lineEdit_2.setText(p.nome)
            self.tela_busca.lineEdit_3.setText(p.end)
            self.tela_busca.lineEdit_4.setText(p.dataNasc)
        else:
            QMessageBox.information(None, 'POO2', 'CPF não cadastrado!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    show_main = Main()
    sys.exit(app.exec_())


