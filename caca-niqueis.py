import random

MAX_LINHAS = 3
MAX_APOSTA = 100
MIN_APOSTA = 1

LINE = 3
COLUMN = 3

contador_simbol = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

contador_valor = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def verificar_ganhos(colunas, linhas, aposta):
    ganhos = 0
    ganhos_linhas = []
    for line in range(linhas):
        simbol = colunas[0][line]
        for column in colunas:
            simbol_a_verificar = column[line]
            if simbol != simbol_a_verificar:
                break
        else:
            ganhos += contador_valor[simbol] * aposta
            ganhos_linhas.append(line + 1)
    return ganhos, ganhos_linhas

def giro_niquel(linhas, colunas, simbolos):
    simbolos_gerais = []
    for simbol, contador in simbolos.items():
        simbolos_gerais.extend([simbol] * contador)
    
    resultado = []
    for _ in range(colunas):
        coluna = []
        simbolos_atual = simbolos_gerais[:]
        for _ in range(linhas):
            if simbolos_atual:
                valor = random.choice(simbolos_atual)
                simbolos_atual.remove(valor)
                coluna.append(valor)
        resultado.append(coluna)
    
    return resultado

def vizu_caca_niquel(colunas):
    for i in range(len(colunas[0])):
        for j, coluna in enumerate(colunas):
            if j != len(colunas) - 1:
                print(coluna[i], end="|")
            else:
                print(coluna[i], end="|")
        print()

def deposit():
    while True:
        valor = input("Quanto você gostaria de depositar? R$ ")
        if valor.isdigit():
            valor = int(valor)
            if valor > 0:
                return valor
            else:
                print("O valor deve ser maior que 0.")
        else:
            print("Entre com um número.")

def numero_de_linhas():
    while True:
        linhas = input(f"Digite o número de linhas que você deseja apostar (1-{MAX_LINHAS}): ")
        if linhas.isdigit():
            linhas = int(linhas)
            if 1 <= linhas <= MAX_LINHAS:
                return linhas
            else:
                print(f"Digite uma quantidade de linhas válida entre 1 e {MAX_LINHAS}.")
        else:
            print("Entre com um número.")

def apostar():
    while True:
        valor = input("Quanto você gostaria de apostar? R$ ")
        if valor.isdigit():
            valor = int(valor)
            if MIN_APOSTA <= valor <= MAX_APOSTA:
                return valor
            else:
                print(f"O valor tem que ser entre R$ {MIN_APOSTA} - R$ {MAX_APOSTA}.")
        else:
            print("Entre com um número.")

def giro(saldo):
    linhas = numero_de_linhas()
    
    while True:
        aposta = apostar()
        aposta_total = aposta * linhas

        if aposta_total > saldo:
            print(f"Você não tem uma quantidade suficiente para apostar, o seu saldo atual é de: R$ {saldo}")
            return saldo  # Retorna o saldo inalterado
        else:
            break
    
    print(f"Você está apostando R$ {aposta} em {linhas} linhas. A aposta total é de: R$ {aposta_total}")
    print(f"Saldo inicial: R$ {saldo}")
    saldo -= aposta_total
    print(f"Saldo restante após a aposta: R$ {saldo}")

    slot = giro_niquel(LINE, COLUMN, contador_simbol)
    vizu_caca_niquel(slot)
    ganhos, ganhos_linhas = verificar_ganhos(slot, linhas, aposta)
    print(f"Você ganhou R$ {ganhos}.")
    print(f"O ganho foi nas linhas: {', '.join(map(str, ganhos_linhas))}")

    return saldo

def main():
    saldo = deposit()
    
    while True:
        print(f"O valor atual é R$ {saldo}")
        giro_opcao = input("Pressione Enter para o giro (ESC para sair): ")
        if giro_opcao.upper() == "ESC":
            print(f"Saindo do jogo. O seu saldo final é de R$ {saldo}")
            break

        saldo = giro(saldo)
        
        if saldo <= 0:
            print("Seu saldo acabou. O jogo terminou.")
            break

if __name__ == "__main__":
    main()
