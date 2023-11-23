from testeVelocidade import *
from traceroute import *
from ping import *
from ipPython import *


def mainBenchmark():

    print("1 - Lista de Ip´s da Rede.\n2 - Teste de Velocidade\n3 - Ping´s\n4 - Traceroute")

    opcao = int(input("Escolha uma das opções: "))

    if opcao == 1:
        mainScan()
        mainBenchmark()
    elif opcao == 2:
        mainVelocidade()
        mainBenchmark()
    elif opcao == 3:
        mainPing()
        mainBenchmark()
    elif opcao == 4:
        maintracer()
        mainBenchmark()
    else:
        print('Opção invalida')
        mainBenchmark()

if __name__ == "__main__":
    mainBenchmark()
