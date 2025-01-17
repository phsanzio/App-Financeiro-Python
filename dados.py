from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import math

#Configurando web-driver
options = Options()
options.add_argument("--headless")  # Ativa o modo headless
options.add_argument("--disable-gpu")  # Desativa a GPU (opcional, mas recomendado)
options.add_argument("--no-sandbox")  # Necessário em alguns ambientes Linux
options.add_argument("--disable-dev-shm-usage")  # Evita problemas de memória compartilhada
options.add_argument("--enable-unsafe-swiftshader")
driver = webdriver.Chrome(options=options) 

list_stocks = [
    "BBAS3", "VALE3", "ISAE4", "PETR4", "ITUB3", 
    "TAEE3", "TASA4", "GOAU4", "KLBN3", "ITSA4", 
    "FESA4", "RAPT4", "SAPR4", "CMIG4", "GGBR3",
    "BRAP4", "BBSE3", "RECV3", "BEES3", "USIM5",
    "VLID3"
]

def txt(infos):
  with open("ativos_web.txt", "w") as arquivo:
    for ativo, infos in infos.items():
        arquivo.write(f"{ativo}: {infos} \n")

def get_infos(list_stocks):
  infos = {}
  for stock in list_stocks:
    url = f"https://www.fundamentus.com.br/detalhes.php?papel={stock}"
    driver.get(url)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    preco = float(soup.find(string="Cotação").find_next().text.replace(',', '.'))
    LPA = soup.find(string="LPA").find_next().text 
    VPA = soup.find(string="VPA").find_next().text 
    preco_justo = math.sqrt(22.5 * float(LPA.replace(',', '.')) * float(VPA.replace(',', '.')))
    infos[stock] = {'Valor': f'R${preco:.2f}', 'LPA': LPA, 'VPA': VPA, 'Valor-Alvo': f'R${preco_justo:.2f}'}
    time.sleep(1)
  driver.quit()
  return infos


