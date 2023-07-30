from Elevador import *

if __name__ == '__main__':

    # Teste do sistema de elevadores
    elevador = Elevador(10)  # Cria um elevador com 10 andares

    # Solicitar andares ao usuário
    andar1 = int(input("Digite o primeiro andar desejado: "))
    andar2 = int(input("Digite o segundo andar desejado: "))
    andar3 = int(input("Digite o terceiro andar desejado: "))

    andares = [andar1, andar2, andar3]
    andares_ordenados = elevador.ordem_proximidade(andares)

    for andar in andares_ordenados:
        elevador.ir_para_andar(andar)