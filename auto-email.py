#!/usr/bin/env python
# coding: utf-8

# In[20]:import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Configurações de e-mail
email_envio = "goalclick.business79@gmail.com"
senha_email = "wXjwc2K;"
smtp_servidor = "smtp.gmail.com"
smtp_porta = 587

# Lista de contatos
contatos = [
    {"nome": "Marcus Pistola", "email": "malucodapistola66@gmail.com"},
    {"nome": "Editor Marc0s", "email": "marcus.editor77@gmail.com"},
    # Adicione mais contatos conforme necessário
]

# Lista de mensagens
mensagens = [
    "Olá, {nome}! Esta é uma mensagem de teste para o e-mail {email}.",
    "Outra mensagem para {nome}. E-mail: {email}.",
    # Adicione mais mensagens conforme necessário
]

# Configuração do navegador
navegador = webdriver.Chrome()
navegador.get("https://mail.google.com/mail/u/2/#inbox?compose=new")

while len(navegador.find_elements(By.ID, "elemento")) < 1:
    time.sleep(1)

# Loop através dos contatos e envio de e-mail
for contato in contatos:
    nome = contato["nome"]
    email_destino = contato["email"]

    for mensagem in mensagens:
        texto = mensagem.format(nome=nome, email=email_destino)

        # Configuração da mensagem de e-mail
        assunto = f"Mensagem de {nome}"
        corpo_email = f"Olá {nome},\n\n{text}"
        msg = MIMEMultipart()
        msg['From'] = email_envio
        msg['To'] = email_destino
        msg['Subject'] = assunto
        msg.attach(MIMEText(corpo_email, 'plain'))

        # Envio do e-mail
        try:
            with smtplib.SMTP(smtp_servidor, smtp_porta) as server:
                server.starttls()
                server.login(email_envio, senha_email)
                server.sendmail(email_envio, email_destino, msg.as_string())
                print(f"E-mail enviado para {email_destino}")
        except Exception as e:
            print(f"Erro ao enviar e-mail para {email_destino}: {str(e)}")

# Fechar o navegador após o envio dos e-mails
navegador.quit()

# %%
