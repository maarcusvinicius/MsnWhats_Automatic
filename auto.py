#!/usr/bin/env python
# coding: utf-8

# In[20]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import urllib

contatos = [
    {"numero": "numero2", "cidade": "cidade2", "nome": "nome2"},
    # Adicione mais pares nome-número conforme necessário
]


mensagens = [
  "Mensagem1",
  "Mensagem2",
  "Mensagem3",
  "Mensagem4",
  "Mensagem5"
]


navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")

while len(navegador.find_elements(By.ID, "side")) < 1:
    time.sleep(1)

for contato in contatos:
    nome = contato["nome"]
    numero = contato["numero"]
    cidade = contato["cidade"]

    for mensagem in mensagens:
        texto = urllib.parse.quote(mensagem.format(nome=nome, cidade=cidade))
        link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
        navegador.get(link)

        while len(navegador.find_elements(By.ID, "side")) < 1:
            time.sleep(25)

        try:
            elemento_mensagem = navegador.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p/span')
            elemento_mensagem.send_keys(Keys.ENTER)
        except NoSuchElementException:
            print(f"Erro ao enviar mensagem para {nome}. Número incorreto: {numero}")
            continue

        time.sleep(10)

navegador.quit()

# %%
