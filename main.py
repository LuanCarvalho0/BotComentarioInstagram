from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import instaloader
import random
import os.path

navegador = webdriver.Chrome()


def sorteioInstagram():
    abrindo_instagram('Usuário', 'Senha', 'Link do pôster')

    if os.path.isfile('seguidores.txt'):
        print('Arquivo de seguidores já carregado...')
    else:
        pegar_seguidores('Usuário')

    comentandoPost()


def abrindo_instagram(usuario, senha, url):
    navegador.get('https://www.instagram.com/')
    sleep(2)
    navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(usuario)
    navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(senha)
    navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
    sleep(10)
    navegador.get(url)


def pegar_seguidores(conta):
    L = instaloader.Instaloader()

    PROFILE = conta
    USER = 'Usuário'
    PASSWORD = 'Senha'

    L.login(USER, PASSWORD)

    profile = instaloader.Profile.from_username(L.context, PROFILE)

    Arquivo = open('seguidores.txt', 'a+')
    seguidoresTeste = (profile.get_followees())

    for seguidor in seguidoresTeste:
        seguidor = str(seguidor).split()
        seguidor = '@' + seguidor[1]
        Arquivo.write(seguidor + '\n')

    Arquivo.close()


def comentandoPost():
    cont = 0
    x = 0
    while 1 == 1:
        comentario1 = lerArquivos()
        comentario2 = lerArquivos()
        sleep(2)
        cmt = navegador.find_element(
            By.XPATH, r'//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea')
        cmt.click()
        sleep(2)
        navegador.find_element(
            By.XPATH,
            r'//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').send_keys(
            comentario1)
        navegador.find_element(
            By.XPATH,
            r'//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').send_keys(
            Keys.SPACE)
        sleep(2)
        navegador.find_element(
            By.XPATH,
            r'//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/textarea').send_keys(
            comentario2)
        sleep(2)
        navegador.find_element(
            By.XPATH,
            r'//*[@id="react-root"]/section/main/div/div[1]/article/div/div[2]/div/div[2]/section[3]/div/form/button/div').click()
        cont += 1
        print(f'Comentarios: {cont}')
        sleep(time(cont))


def lerArquivos():
    with open('seguidores.txt', 'r') as file:
        allText = file.read()
        words = list(map(str, allText.split()))
        return random.choice(words)


def time(cont):
    if cont % 3 == 0:
        return random.uniform(210, 300)
    else:
        return random.uniform(60, 100)


sorteioInstagram()
