import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from design import Ui_main_window  # Arquivo gerado pelo Qt Designer
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import yfinance as yf
import dados


list_stocks = [
    "BBAS3", "VALE3", "ISAE4", "PETR4", "ITUB3", 
    "TAEE3", "TASA4", "GOAU4", "KLBN3", "ITSA4", 
    "FESA4", "RAPT4", "SAPR4", "CMIG4", "GGBR3",
    "BRAP4", "BBSE3", "RECV3", "BEES3", "USIM5",
    "VLID3"
]


# Função para calcular a valorização/desvalorização da carteira
def calcular_variacao(ativos):
    total_investido = 0
    total_atual = 0

    for ativo in ativos:
        quantidade = ativo['quantidade']
        preco_medio = ativo['preco_medio']
        preco_atual = ativo['preco_atual']

        total_investido += quantidade * preco_medio
        total_atual += quantidade * preco_atual

    variacao_percentual = ((total_atual - total_investido) / total_investido) * 100
    return total_investido, total_atual, variacao_percentual

# Classe principal da aplicação
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main_window()
        self.ui.setupUi(self)

        # Configurar a tabela
        self.configurar_tabela()
        dados_ativos = dados.get_infos(list_stocks)
        print(dados_ativos)
        # Preencher a tabela com os dados dos ativos
        self.preencher_tabela(dados_ativos)

        # Calcular e exibir o gráfico de valorização/desvalorização da carteira
        self.exibir_grafico()

    def configurar_tabela(self):
        """Configura as colunas e cabeçalhos da tabela."""
        self.ui.tableWidget.setColumnCount(6)  # Número de colunas
        self.ui.tableWidget.setHorizontalHeaderLabels(["Ativo", "Quantidade", "Preço Médio", "Preço Atual", "Variação (%)", "Saldo"])
        self.ui.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

    def preencher_tabela(self, ativos):
        """Preenche a tabela com os dados fornecidos."""
        self.ui.tableWidget.setRowCount(len(ativos))  # Define o número de linhas

        for row_idx, ativo in enumerate(ativos):
            # Cálculo da variação e saldo
            variacao = ((ativo["preco_atual"] - ativo["preco_medio"]) / ativo["preco_medio"]) * 100
            saldo = ativo["quantidade"] * ativo["preco_atual"]

            # Adicionar os itens na tabela
            self.ui.tableWidget.setItem(row_idx, 0, QTableWidgetItem(ativo["nome"]))
            self.ui.tableWidget.setItem(row_idx, 1, QTableWidgetItem(str(ativo["quantidade"])))
            self.ui.tableWidget.setItem(row_idx, 2, QTableWidgetItem(f"R$ {ativo['preco_medio']:.2f}"))
            self.ui.tableWidget.setItem(row_idx, 3, QTableWidgetItem(f"R$ {ativo['preco_atual']:.2f}"))
            self.ui.tableWidget.setItem(row_idx, 4, QTableWidgetItem(f"{variacao:+.2f}%"))
            self.ui.tableWidget.setItem(row_idx, 5, QTableWidgetItem(f"R$ {saldo:.2f}"))

    def exibir_grafico(self):

    # Baixar os dados do Ibovespa (ticker: ^BVSP)
        dados_ibov = yf.download('^BVSP', start='2024-01-01', end='2025-01-01')

        # Criar o gráfico com Matplotlib
        fig = Figure()
        fig.set_facecolor("#212529")  # Fundo do gráfico no modo escuro
        ax = fig.add_subplot(111)

        # Plotar os dados de fechamento do Ibovespa
        ax.plot(dados_ibov.index, dados_ibov['Close'], label='Ibovespa', color='#6CC644')

        # Configurar o estilo do gráfico
        ax.set_title("Ibovespa", color="white")
        ax.xaxis.set_visible(False)  # Remove a legenda do eixo x
        ax.yaxis.set_visible(False)  # Remove a legenda do eixo y

    # Remover linhas de grade
        ax.grid(False)  # Remove as linhas de grade

    # Remover a legenda do gráfico
        ax.legend().set_visible(False)  # Remove a legenda

    # Remover bordas do gráfico
        for spine in ax.spines.values():
            spine.set_visible(False)
            ax.grid(color='#444', linestyle='--', linewidth=0.5)
            ax.legend(facecolor="#212529", edgecolor="#444", labelcolor="white")
            
        # Configurar cores dos ticks e fundo do eixo
        ax.tick_params(colors="white")
        ax.set_facecolor("#212529")

        # Adicionar o gráfico à interface usando FigureCanvas
        canvas = FigureCanvas(fig)

        # Limpar qualquer widget anterior no graphicsView e adicionar o novo canvas
        for child in self.ui.graphicsView.children():
            child.deleteLater()

        canvas.setParent(self.ui.graphicsView)
        canvas.setGeometry(self.ui.graphicsView.rect())
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
