#!/usr/bin/env python
# coding: utf-8

# In[20]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
import time


lista = [
    {"numero": "551235190237", "cidade": "São José dos Campos", "nome": "HDF Veículos"},
    {"numero": "551239362080", "cidade": "São José dos Campos", "nome": "DuVale Veículos"},
    {"numero": "551239426677", "cidade": "São José dos Campos", "nome": "Sobarato Multimarcas"},
    {"numero": "551239210101", "cidade": "São José dos Campos", "nome": "Viva Veículos"},
    {"numero": "551239171314", "cidade": "São José dos Campos", "nome": "Gutierrez Veículos"},
    {"numero": "551239119701", "cidade": "São José dos Campos", "nome": "Roger Car"},
    {"numero": "5512991108025", "cidade": "São José dos Campos", "nome": "Vidoca Shopping do Carro"},
    {"numero": "5512997255436", "cidade": "São José dos Campos", "nome": "Capital Veículos"},
    {"numero": "551239399757", "cidade": "São José dos Campos", "nome": "Rodolfo Veículos"},
    {"numero": "551239123400", "cidade": "São José dos Campos", "nome": "Autobem Veículos"},
    {"numero": "551232097470", "cidade": "São José dos Campos", "nome": "Morais Autocar"},
    {"numero": "5512991915081", "cidade": "São José dos Campos", "nome": "Villa Norte"},
    {"numero": "5512996341549", "cidade": "São José dos Campos", "nome": "Super Shopping do Carro"},
    {"numero": "5512997721955", "cidade": "São José dos Campos", "nome": "Caldardo Veiculos"},
    {"numero": "5512991515100", "cidade": "São José dos Campos", "nome": "Toninho Motors"},
    {"numero": "551239391410", "cidade": "São José dos Campos", "nome": "DEVILLE Veículos"},
    {"numero": "5512996710060", "cidade": "São José dos Campos", "nome": "Mega Veículos"},
    {"numero": "551239297099", "cidade": "São José dos Campos", "nome": "Guedes Veículos"},
    {"numero": "551239163465", "cidade": "São José dos Campos", "nome": "A+ veículos"},
    {"numero": "551239061400", "cidade": "São José dos Campos", "nome": "Veibras"},
    {"numero": "5512992235522", "cidade": "São José dos Campos", "nome": "Connect Car"},
    {"numero": "5512982223508", "cidade": "São José dos Campos", "nome": "Podiumm Veículos"},
    {"numero": "5512991407100", "cidade": "São José dos Campos", "nome": "Michelly Vendas"},
    {"numero": "551239343512", "cidade": "São José dos Campos", "nome": "Luciano Automóveis"},
    {"numero": "551239164861", "cidade": "São José dos Campos", "nome": "Unicar Multimarcas"},
    {"numero": "551232096144", "cidade": "São José dos Campos", "nome": "Luxy Car Automóveis"},
    {"numero": "551232068979", "cidade": "São José dos Campos", "nome": "Vision Veículos"},
    {"numero": "5512997555222", "cidade": "São José dos Campos", "nome": "Qi Motors"},
    {"numero": "551239392552", "cidade": "São José dos Campos", "nome": "Villa Norte Veículos"},
    {"numero": "551239123100", "cidade": "São José dos Campos", "nome": "Ribeiro Veículos"},
    {"numero": "551239136143", "cidade": "São José dos Campos", "nome": "Aliança Motors"},
    {"numero": "5512974067900", "cidade": "São José dos Campos", "nome": "Automil"},
    {"numero": "5512982434000", "cidade": "São José dos Campos", "nome": "SIGA MULTIMARCAS"},
    {"numero": "551239165214", "cidade": "São José dos Campos", "nome": "CT Veículos"},
    {"numero": "5512974045408", "cidade": "São José dos Campos", "nome": "Kn Automóveis"},
    {"numero": "5512996671484", "cidade": "São José dos Campos", "nome": "Carros Qualidades"},
    {"numero": "551239135151", "cidade": "São José dos Campos", "nome": "Taipan Veículos"},
    {"numero": "5512997793880", "cidade": "São José dos Campos", "nome": "P3 Automóveis"},
    {"numero": "5512996245086", "cidade": "São José dos Campos", "nome": "JDS Veículos"},
    {"numero": "5512982667630", "cidade": "São José dos Campos", "nome": "Rico Motors"},
    {"numero": "551232048248", "cidade": "São José dos Campos", "nome": "F José B"},
    {"numero": "551239330016", "cidade": "São José dos Campos", "nome": "Autoshopping Visual"},
    {"numero": "5512981380061", "cidade": "São José dos Campos", "nome": "Galpão Multimarcas"},
    {"numero": "5512974014647", "cidade": "São José dos Campos", "nome": "Biavale Veículos"},
    {"numero": "551239092400", "cidade": "São José dos Campos", "nome": "Localiza Seminovos"},
    {"numero": "5512996887758", "cidade": "São José dos Campos", "nome": "D-Car Veículos"},
    {"numero": "551233026115", "cidade": "São José dos Campos", "nome": "Valle Multimarcas"},
    {"numero": "551232022300", "cidade": "São José dos Campos", "nome": "Localiza Seminovos"},
    {"numero": "5512997741269", "cidade": "São José dos Campos", "nome": "Multimarcas"},
    {"numero": "551232069252", "cidade": "São José dos Campos", "nome": "Supremo Automóveis"},
    {"numero": "5512982017777", "cidade": "São José dos Campos", "nome": "RD I MOTORS"},
]

# Lista de contatos
contatos = [
    {"nome": "Nome1", "numero": "5524235562374", "mensagem": "Primeira mensagem para {nome}."},
    {"nome": "Nome2", "numero": "558387625237", "mensagem": "Segunda mensagem para {nome}."},
    {"nome": "Nome3", "numero": "4354353453", "mensagem": "Terceira mensagem diferente para {nome}."},
    {"nome": "Nome4", "numero": "558387625237", "mensagem": "Quarta mensagem diferente para {nome}."},
    {"nome": "Nome5", "numero": "12393244439", "mensagem": "Quinta mensagem diferente para {nome}.LOREMIMPUSLALorem ipsum vel interdum rutrum consequat eget elit ac lobortis, habitant vivamus tortor orci cursus sagittis amet lacus congue feugiat, netus scelerisque etiam est habitasse ante facilisis adipiscing. platea nullam fermentum porttitor tempus platea tristique massa, aptent hendrerit quis sociosqu mollis diam ullamcorper tincidunt, etiam dapibus sem sociosqu volutpat placerat. molestie cras aliquet aenean tempor eleifend duis fringilla pharetra nibh, habitant tempus tincidunt nam augue vulputate enim ipsum litora fames, lacinia rhoncus non hac in rhoncus nostra elementum. purus fusce turpis venenatis vulputate dapibus ut massa lacinia aliquam, nibh dictumst aptent pulvinar praesent tortor varius lectus volutpat, quis integer condimentum faucibus pellentesque aliquam odio eleifend."},
    {"nome": "Nome6", "numero": "regenerregoi", "mensagem": "Sexta mensagem diferente para {nome}."},
    # Adicione mais contatos conforme necessário
]

# Configuração do navegador
navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(1)

# Lista para armazenar números já processados
numeros_processados = set()

# Loop através dos contatos e envio de mensagens
for contato in contatos:
    nome = contato["nome"]
    numero = contato["numero"]
    mensagem = contato["mensagem"]

    # Verifica se o número já foi processado
    if numero in numeros_processados:
        print(f"Número {numero} já foi enviado. Pulando para o próximo.")
        continue

    # Adiciona o número à lista de números processados
    numeros_processados.add(numero)

    # Substitui o marcador {nome} na mensagem pelo nome correspondente
    texto = mensagem.format(nome=nome)

    # Configuração do navegador para WhatsApp
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)

    # Espera até que o elemento de mensagem esteja presente
    try:
        elemento_mensagem = WebDriverWait(navegador, 20).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span')
            )
        )

        # Aguarda até que o elemento de mensagem esteja interagível
        WebDriverWait(navegador, 30).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span')
            )
        ).send_keys(Keys.ENTER)

        print(f"Mensagem enviada para {nome} ({numero})")
    except (NoSuchElementException, TimeoutException):
        print(f"Erro ao enviar mensagem para {nome} ({numero}). Número incorreto ou não encontrado.")
        continue

    # Aguarda 1 minuto antes de prosseguir para o próximo número
    time.sleep(60)

# Fechar o navegador após o envio das mensagens
navegador.quit()

# %%
