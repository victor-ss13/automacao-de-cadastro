# Importando biblioteca p/ automatizar tarefas
import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.85 #  Tempo de espera entre ações (em segundos) da biblioteca de automação

    # pyautogui.click -> clicar em algum lugar da tela
    # pyautogui.write -> escrever um texto
    # pyautogui.press -> pressionar 1 tecla do teclado

# Passo a passo do projeto:

# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login" # armazenamos  o link na variavel 'link'

    # abrir navegador (chrome)
pyautogui.press("win") # Abre o menu de janelas do Windows
pyautogui.write("chrome") # Escreve "chrome" no campo de pesquisa do windows para abrir o Google Chrome
pyautogui.press("enter") # Pressiona Enter para executar a busca  e abrir o Google Chrome

    # entrar no site
pyautogui.write(link)                           # Escreve o link que esta armazenado na variavel 'link'
pyautogui.press("enter")                        #  Pressiona Enter para acessar o site
time.sleep(1.5)                                 # O programa espera 1.5 segundos para dar continuidade ao código


# Passo 2: Fazer login
pyautogui.click(x=690, y=508)                   # Clica no campo de inserção do e-mail
pyautogui.write("victor.sampaio2003@gmail.com") # Escreve seu email
pyautogui.press("tab")                          # Avança para o próximo campo do formulário
   # pyautogui.click(x=700, y=631)              # Clica no campo de inserção da senha
pyautogui.write("password")                     # Escreve sua senha
pyautogui.press("tab")                          # Clica no botão de login
pyautogui.press("enter")
time.sleep(1.5)                                 # O programa espera 1.5 segundos para dar continuidade ao código

# Passo 3: Importar a base de dados
tabela = pandas.read_csv("produtos.csv")


# Passo 4: Cadastrar 1 produto
# para cada linha da minha tabela
for linha in tabela.index:
        # clicando no 1° campo
    pyautogui.click(x=1012, y=374)                             # Poderia utilizar o '.click()' com as coordenadas do campo
        # cadastrar código do produto
    codigo = tabela.loc[linha, "codigo"]            # acessamos a base de dados e pegamos o código do produto, baseado na posição que o index está
    pyautogui.write(codigo)            # Escrevemos o código do produto
    pyautogui.press("tab")                          # Passamos para o próximo campo
        # cadastrar marca do produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")
        # cadastrar tipo do produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")
        # cadastrar categoria do produto
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
        # cadastrar preço do produto
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
        # cadastrar custo do produto
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")
        # cadastrar obs do produto
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):                        # Verifica se a observação não está vazia
        pyautogui.write(obs)
    pyautogui.press("tab")
        # enviar o cadastro
    pyautogui.press("enter")
        # voltar para o topo da página
    pyautogui.scroll(5000)                          #  Scroll para cima na página (para chegar ao topo novamente)


# Passo 5: Repetir o processo de cadastro até acabar

