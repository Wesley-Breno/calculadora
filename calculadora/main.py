
from PyQt5.QtWidgets import QMainWindow  # Responsavel por configurar a janela
from PyQt5.QtWidgets import QApplication  # Responsavel por executar a janela
from PyQt5.QtWidgets import QPushButton  # Responsavel pela criacao dos botoes
from PyQt5.QtWidgets import QLineEdit  # Responsavel pela criacao da caixa de texto


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()  # Herdando da classe para configurar janela

        self.digitou = ''  # Oque o usuario digitou
        self.resultado = 0  # Resultado do calculo

        # Tamanho, largura e titulo da janela
        self.topo = 450
        self.esquerda = 120
        self.altura = 240
        self.largura = 250
        self.titulo = 'Calculadora'

        # Criando cada botao e colocando na tela, cada botao chama uma funcao...
        self.numero0 = QPushButton('0', self)  # Botao 0
        self.numero0.move(60, 200)  # Posicao do botao na janela
        self.numero0.resize(60, 50)  # Altura e largura do botao
        self.numero0.clicked.connect(self.numero0_clicado)  # Funcao que o botao chama a ser clicado

        self.numero1 = QPushButton('1', self)
        self.numero1.move(0, 150)
        self.numero1.resize(60, 50)
        self.numero1.clicked.connect(self.numero1_clicado)

        self.numero2 = QPushButton('2', self)
        self.numero2.move(60, 150)
        self.numero2.resize(60, 50)
        self.numero2.clicked.connect(self.numero2_clicado)

        self.numero3 = QPushButton('3', self)
        self.numero3.move(120, 150)
        self.numero3.resize(60, 50)
        self.numero3.clicked.connect(self.numero3_clicado)

        self.numero4 = QPushButton('4', self)
        self.numero4.move(0, 100)
        self.numero4.resize(60, 50)
        self.numero4.clicked.connect(self.numero4_clicado)

        self.numero5 = QPushButton('5', self)
        self.numero5.move(60, 100)
        self.numero5.resize(60, 50)
        self.numero5.clicked.connect(self.numero5_clicado)

        self.numero6 = QPushButton('6', self)
        self.numero6.move(120, 100)
        self.numero6.resize(60, 50)
        self.numero6.clicked.connect(self.numero6_clicado)

        self.numero7 = QPushButton('7', self)
        self.numero7.move(0, 50)
        self.numero7.resize(60, 50)
        self.numero7.clicked.connect(self.numero7_clicado)

        self.numero8 = QPushButton('8', self)
        self.numero8.move(60, 50)
        self.numero8.resize(60, 50)
        self.numero8.clicked.connect(self.numero8_clicado)

        self.numero9 = QPushButton('9', self)
        self.numero9.move(120, 50)
        self.numero9.resize(60, 50)
        self.numero9.clicked.connect(self.numero9_clicado)

        self.clear = QPushButton('C', self)
        self.clear.move(0, 200)
        self.clear.resize(60, 50)
        self.clear.clicked.connect(self.clear_clicado)

        self.igual = QPushButton('=', self)
        self.igual.move(120, 200)
        self.igual.resize(60, 50)
        self.igual.clicked.connect(self.igual_clicado)

        self.mais = QPushButton('+', self)
        self.mais.move(180, 200)
        self.mais.resize(60, 50)
        self.mais.clicked.connect(self.mais_clicado)

        self.menos = QPushButton('-', self)
        self.menos.move(180, 150)
        self.menos.resize(60, 50)
        self.menos.clicked.connect(self.menos_clicado)

        self.x = QPushButton('X', self)
        self.x.move(180, 100)
        self.x.resize(60, 50)
        self.x.clicked.connect(self.x_clicado)

        self.dividir = QPushButton('÷', self)
        self.dividir.move(180, 50)
        self.dividir.resize(60, 50)
        self.dividir.clicked.connect(self.dividir_clicado)

        # Caixa de texto onde aparecera os numeros digitados
        self.digitados = QLineEdit(self)
        self.digitados.move(0, 0)
        self.digitados.resize(239, 50)
        self.digitados.setStyleSheet('font-size: 40px; font-family: Arial, Helvetica, sans-serif')  # Personalizando com css

        self.carregar_janela()  # Carregando a janela

    def numero0_clicado(self):  # Funcao do botao ao ser clicado
        self.digitou += '0'
        self.digitados.setText(self.digitou)  # Mostrando na janela o valor do botao

    def numero1_clicado(self):
        self.digitou += '1'
        self.digitados.setText(self.digitou)

    def numero2_clicado(self):
        self.digitou += '2'
        self.digitados.setText(self.digitou)

    def numero3_clicado(self):
        self.digitou += '3'
        self.digitados.setText(self.digitou)

    def numero4_clicado(self):
        self.digitou += '4'
        self.digitados.setText(self.digitou)

    def numero5_clicado(self):
        self.digitou += '5'
        self.digitados.setText(self.digitou)

    def numero6_clicado(self):
        self.digitou += '6'
        self.digitados.setText(self.digitou)

    def numero7_clicado(self):
        self.digitou += '7'
        self.digitados.setText(self.digitou)

    def numero8_clicado(self):
        self.digitou += '8'
        self.digitados.setText(self.digitou)

    def numero9_clicado(self):
        self.digitou += '9'
        self.digitados.setText(self.digitou)

    def mais_clicado(self):
        self.digitou += '+'
        self.digitados.setText(self.digitou)

    def menos_clicado(self):
        self.digitou += '-'
        self.digitados.setText(self.digitou)

    def x_clicado(self):
        self.digitou += 'x'
        self.digitados.setText(self.digitou)

    def dividir_clicado(self):
        self.digitou += '÷'
        self.digitados.setText(self.digitou)

    def clear_clicado(self):
        self.digitou = ''
        self.digitados.setText(self.digitou)

    def igual_clicado(self):  # Se o botao igual foi clicado para ver o resultado do calculo
        valor = ''  # Variavel onde ira ficar cada valor digitado
        calculo = []

        for p, c in enumerate(self.digitou):
            if c.isdigit():  # Se o caractere da vez for um numero
                valor += c  # Concatenando
                if p == len(self.digitou) - 1:  # Se o caractere da vez for o ultimo
                    calculo.append(valor)  # Adicionando valor
                    valor = ''  # Limpando variavel para o proximo valor

            else:
                calculo.append(valor)
                calculo.append(c)  # Adicionando sinal
                valor = ''

        resultado = 0  # Variavel que aparecera o resultado

        if len(calculo) > 3:  # Se o usuario digitou mais de um calculo ao mesmo tempo
            self.digitou = ''
            self.digitados.setStyleSheet('font-size: 15px')  # Diminuindo tamanho da fonte
            self.digitados.setText('So fazemos um calculo por vez.')  # Mostrando uma mensagem

        else:
            for i, e in enumerate(calculo):
                if e == '+':
                    resultado = int(calculo[i - 1]) + int(calculo[i + 1])
                if e == '-':
                    resultado = int(calculo[i - 1]) - int(calculo[i + 1])
                if e == '*':
                    resultado = int(calculo[i - 1]) * int(calculo[i + 1])
                if e == '/':
                    resultado = int(calculo[i - 1]) / int(calculo[i + 1])

            self.digitou = str(resultado)
            self.digitados.setStyleSheet('font-size: 40px')
            self.digitados.setText(self.digitou)

    def carregar_janela(self):
        self.setGeometry(self.topo, self.esquerda, self.altura, self.largura)  # Aplicando tamanho e largura colocados
        self.setWindowTitle(self.titulo)  # Colocando titulo da janela
        self.show()  # Mostrando janela


if __name__ == '__main__':
    app = QApplication([])
    janela = Janela()
    app.exec_()
