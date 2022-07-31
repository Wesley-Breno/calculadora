
from PyQt5.QtWidgets import QMainWindow  # Responsavel por configurar a janela
from PyQt5.QtWidgets import QApplication  # Responsavel por executar a janela
from PyQt5.QtWidgets import QPushButton  # Responsavel pela criacao dos botoes
from PyQt5.QtWidgets import QLineEdit  # Responsavel pela criacao da caixa de texto


class Janela(QMainWindow):
    def __init__(self):
        super().__init__()  # Herdando da classe para configurar janela

        # Tamanho, largura e titulo da janela
        self.topo = 450
        self.esquerda = 120
        self.altura = 240
        self.largura = 250
        self.titulo = 'Calculadora'

        # Criando cada botao e colocando na tela em uma posicao especifica.
        self.botao('C', 0, 200, clear=True)  # Informando que é o botao de limpar
        self.botao('0', 60, 200)
        self.botao('=', 120, 200, igual=True)  # Informando que é o botao para ver o resultado
        self.botao('+', 180, 200)

        self.botao('1', 0, 150)
        self.botao('2', 60, 150)
        self.botao('3', 120, 150)
        self.botao('-', 180, 150)

        self.botao('4', 0, 100)
        self.botao('5', 60, 100)
        self.botao('6', 120, 100)
        self.botao('x', 180, 100)

        self.botao('7', 0, 50)
        self.botao('8', 60, 50)
        self.botao('9', 120, 50)
        self.botao('÷', 180, 50)

        # Caixa de texto onde aparecera os numeros digitados
        self.digitados = QLineEdit(self)
        self.digitados.move(0, 0)
        self.digitados.resize(239, 50)
        # Personalizando com css
        self.digitados.setStyleSheet('font-size: 40px; font-family: Arial, Helvetica, sans-serif')

        self.carregar_janela()  # Carregando a janela

    def botao(self, botao, d_esquerda, d_topo, igual=None, clear=None):
        """
        Metodo que ira criar um botao e mostra-lo na janela. Se for criado o botao de igualdade ( = ) ou o botao de
        limpar a tela ( C ), eles devem ser especificados com o parametro igual/clear recebendo True, para o botao que
        foi criado.

        :param botao: Nome do botao
        :param d_esquerda: Quantidade de pixels de distancia que ira ficar do lado esquerdo da janela
        :param d_topo:  Quantidade de pixels de distancia que ira ficar do topo da janela
        :param igual: Parametro para saber se é o botao de mostrar resultado ou nao, se for recebe True
        :param clear: Parametro para saber se é o botao de limpar tela ou nao, se for recebe True
        :return: None
        """
        # Criando botao
        botao_criado = QPushButton(botao, self)
        botao_criado.move(d_esquerda, d_topo)
        botao_criado.resize(60, 50)

        if not igual and not clear:  # Se o botao for um numero
            botao_criado.clicked.connect(lambda: self.digitados.setText(self.digitados.text() + botao))

        else:
            if igual:
                botao_criado.clicked.connect(self.igual_clicado)  # Chamara a funcao 'igual_clicado'

            if clear:
                botao_criado.clicked.connect(lambda: self.digitados.setText(''))  # Limpando tela da calculadora

    def igual_clicado(self):  # Se o botao igual foi clicado para ver o resultado do calculo
        valor = ''  # Variavel onde ira ficar cada valor digitado
        calculo = []

        for p, c in enumerate(self.digitados.text()):
            if c.isdigit():  # Se o caractere da vez for um numero
                valor += c  # Concatenando

                if p == len(self.digitados.text()) - 1:  # Se o caractere da vez for o ultimo
                    calculo.append(valor)  # Adicionando valor
                    valor = ''  # Limpando variavel para o proximo valor

            else:
                calculo.append(valor)
                calculo.append(c)  # Adicionando sinal
                valor = ''

        resultado = 0  # Variavel que aparecera o resultado

        if len(calculo) > 3:  # Se o usuario digitou mais de um calculo ao mesmo tempo
            self.digitados.setStyleSheet('font-size: 15px')  # Diminuindo tamanho da fonte
            self.digitados.setText('Um calculo por vez.')  # Mostrando uma mensagem

        else:
            for i, e in enumerate(calculo):
                if e == '+':
                    resultado = int(calculo[i - 1]) + int(calculo[i + 1])
                if e == '-':
                    resultado = int(calculo[i - 1]) - int(calculo[i + 1])
                if e == 'x':
                    resultado = int(calculo[i - 1]) * int(calculo[i + 1])
                if e == '÷':
                    resultado = int(calculo[i - 1]) / int(calculo[i + 1])

            self.digitados.setStyleSheet('font-size: 40px')
            self.digitados.setText(str(resultado))

    def carregar_janela(self):
        self.setGeometry(self.topo, self.esquerda, self.altura, self.largura)  # Aplicando tamanho e largura colocados
        self.setWindowTitle(self.titulo)  # Colocando titulo da janela
        self.show()  # Mostrando janela


if __name__ == '__main__':
    app = QApplication([])
    janela = Janela()
    app.exec_()
