#  Ativando o módulo para fazer os passos de forma sincronizada com o navegador (faz e espera)
from playwright.sync_api import sync_playwright

#  módulo de geração de log
import logging

#  módulo de tempo de espera
import time

# módulo para controlar o teclado
import pyautogui as pyg

# arquivo com logins e senhas
import credenciais

# **************************** Inicio ****************************

#  log config básico.
logging.basicConfig(filename='Bot.log', filemode='a', format='%(asctime)s; - %(message)s')

#  preparando o loop eterno
inf = 2

while inf:

    #  Função de busca, pra não precisar repetir código. Visa consultar o chat de outros setores da empresa também!
    def procurar(login, senha, chat):

        # abrindo o navegador
        with sync_playwright() as p:
            navegador = p.chromium.launch(headless=False, slow_mo=1000)  #  Abrindo o navegador

            #  configurações finais do navegador
            pagina1 = navegador.new_page(ignore_https_errors=True)  #  ignorar erro de certificado

            try:
                pagina1.goto('Link do Chat da empresa - Sistema interno')

                #  Logar no R2D2
                pagina1.locator('xpath=//*[@id="fieldIdentifier"]').fill(login)
                pagina1.locator('xpath=//*[@id="password"]').fill(senha)
                pagina1.locator('xpath=//*[@id="root"]/view-sign-in/component-card/form/div[2]/button').click()
                time.sleep(10)

                # aguardando 10 segundos para carregar os atendimentos
                atendimento1 = pagina1.locator('xpath=//*[@id="root"]/view-core/view-core-content/div[1]/div[1]/div/div').inner_text()
                logging.warning('Numero de atendimentos obtido com sucesso.')
                atendimento = int(atendimento1)

            except:
                logging.warning('Erro ao obter o numero de atendimentos')
            atendimento = 1
            try:
                if atendimento > 0:  # se tiver atendimento
                    pagina = navegador.new_page(ignore_https_errors=True)
                    # entra no email, e loga
                    pagina.goto('https://accounts.google.com/v3/signin/identifier?dsh=S-217789724%3A1664222336908852&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWoOQyqx-GG7Cm3itImCGz6eevc4r9ctVZN09yqY0H1T0QEFsgwOB6xgs1LX91kxd6oZj5D_Cg')
                    pagina.locator('xpath=//*[@id="identifierId"]').fill(credenciais.email)
                    pagina.locator('xpath=//*[@id="identifierNext"]/div/button/div[3]').click()
                    pagina.locator('xpath=//*[@id="password"]/div[1]/div/div[1]/input').fill(credenciais.passmail)
                    pagina.locator('xpath=//*[@id="passwordNext"]/div/button/span').click()
                    pagina.goto('https://mail.google.com/chat/u/0/#chat/welcome')
                    time.sleep(4)
                    # entrando no chat do time
                    pagina.goto(chat)
                    time.sleep(5)
                    
                    # dando tab ate chegar no texto para avisar
                    i = 0
                    while i < 6:
                        pyg.press('tab')
                        time.sleep(0.7)
                        i = i + 1

                    time.sleep(1)
                    pyg.press('space')
                    # avisando no chat (controlando o teclado)
                    time.sleep(2)
                    pyg.write(f'Ola, temos um total de {atendimento} chamado(s) aguardando atendimento.')
                    time.sleep(1)
                    pyg.press('enter')
                    navegador.close()
                    logging.warning(f'Chat {login} informado com sucesso.')

                elif atendimento == 0:  # caso nao tenha nenhum chamado para o momento
                    navegador.close()
                    logging.warning(f'Sem chamados para o momento {login}.')

                else:
                    navegador.close()  # em casos de erro ou não previstos
                    logging.warning('Erro ao tentar entrar no gmail.')

            except:
                logging.warning('Erro após obter os atendimentos.')


# ------- Buscas individuais em loop ------

    # Time de Gestão
    try:
        gestao = credenciais.gestao
        pgestao = credenciais.pgestao
        cgestao = credenciais.cgestao
        procurar(gestao, pgestao, cgestao)
        logging.warning("Sucesso ao buscar atendimentos do Gestão")
        time.sleep(5)
    except:
        logging.warning("Erro ao buscar dados do Gestão")
        time.sleep(5)


    # aguardando 20 minutos antes de iniciar as buscas novamente
    time.sleep(1200) # 1800, 30 minutos

#salvando no log,informando que finalizou o bot
logging.warning('Bot finalizado, não está mais execução!')
