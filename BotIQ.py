from iqoptionapi.stable_api import IQ_Option
import time
import json

### preencha seu email e senha aqui abaixo ###
email = ''
senha = ''

API = IQ_Option(email, senha)


### Função para conectar na IQOPTION ###
check, reason = API.connect()
if check:
    print('Conectado com sucesso')
else:
    if reason == '{"code":"invalid_credentials","message":"You entered the wrong credentials. Please ensure that your login/password is correct."}':
        print('Email ou senha incorreta')

    else:
        print('Houve um problema na conexão')

        print(reason)

### Função para Selecionar demo ou real ###
while True:
    escolha = input(
        'Selecione a conta em que deseja conectar: demo ou real  - ')
    if escolha == 'demo':
        conta = 'PRACTICE'
        print('Conta demo selecionada')
        break
    if escolha == 'real':
        conta = 'REAL'
        print('Conta real selecionada')
        break
    else:
        print('Escolha incorreta! Digite demo ou real')

API.change_balance(conta)

### Função abrir ordem e checar resultado ###


def compra(ativo, valor, direcao, exp, tipo):
    if tipo == 'digital':
        check, id = API.buy_digital_spot_v2(ativo, valor, direcao, exp)
    else:
        check, id = API.buy(valor, ativo, direcao, exp)

    if check:
        print('Ordem executada ', id)

        while True:
            time.sleep(0.1)
            status, resultado = API.check_win_digital_v2(
                id) if tipo == 'digital' else API.check_win_v4(id)

            if status:
                if resultado > 0:
                    print('WIN', round(resultado, 2))
                elif resultado == 0:
                    print('EMPATE', round(resultado, 2))
                else:
                    print('LOSS', round(resultado, 2))
                break

    else:
        print('erro na abertura da ordem,', id)


ativo = 'EURUSD-OTC'
valor = 10.50
direcao = 'call'
exp = 1
tipo = 'digital'


### chamada da função de compra ###
compra(ativo, valor, direcao, exp, tipo)

# pip install websock-client=1.5.0.1
