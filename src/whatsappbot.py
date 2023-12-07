# Importar as bibliotecas 
from turtle import goto
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui
from random import randrange

# Navegar até o whatsappweb
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://web.whatsapp.com/')
time.sleep(10)

# Definir contatos e grupos e mensagem a ser enviada
contatos = [] 
mensagens = []
arquivos = []

# Buscar contatos/grupos
aleatorio = randrange(1, 3)
def buscar_contato(contato):
    campo_pesquisa = driver.find_element(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
    campo_pesquisa.click()
    campo_pesquisa.send_keys(contato)
    campo_pesquisa.send_keys(Keys.ENTER)

def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_element(By.XPATH, '//p[contains(@class,"selectable-text copyable-text")]')
    pyautogui.click(870, 990)
    #campo_mensagem.click()
    campo_mensagem.send_keys(mensagem)
    pyautogui.hotkey('shift', 'enter')
    #campo_mensagem.send_keys(Keys.ENTER)

def clicar(arquivo):
    pyautogui.click(470, 990)
    time.sleep(aleatorio)
    pyautogui.click(470, 710)
    time.sleep(aleatorio)
    pyautogui.click(80, 180)
    time.sleep(aleatorio)
    pyautogui.click(400, 490)
    time.sleep(aleatorio)
    pyautogui.typewrite(arquivo, interval=0.01)
    pyautogui.press('down')
    pyautogui.press('enter')
    time.sleep(aleatorio)
    pyautogui.press('enter')

for contato in contatos:
    buscar_contato(contato)
    for mensagem in mensagens:
        enviar_mensagem(mensagem)
    for arquivo in arquivos:
        clicar(arquivo)
    pyautogui.press('enter')