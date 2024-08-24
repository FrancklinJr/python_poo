from frota import *

if __name__ == "__main__":
    print('Cadastre o carro 1')
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    cm = float(input('Qual é o consumo médio do carro? '))
    litros = float(input('Quantos litros tem o tanque do carro? '))


    carro1 = Carro(nm_modelo, nm_marca, nm_cor, 0.0, False, litros, cm)

    print("Cadastre o carro 2")
    nm_modelo = input('Digite o modelo: ')
    nm_marca = input('Digite a marca: ')
    nm_cor = input('Digite a cor: ')
    cm = float(input('Qual é o consumo médio do carro? '))
    litros = float(input('Quantos litros tem o tanque do carro? '))

    carro2 = Carro(nm_modelo, nm_marca, nm_cor, 0.0, False, litros, cm)

    '''
    Controlando o carro até ele atingir 10000 Km
    '''
    while carro1.odometro < 600 and carro2.odometro < 600 and (carro1.tanque > 0 or carro2.tanque > 0):
        try:
            print('1- Ligar motor')
            print('2- Desligar motor')
            print('3- Acelerar')

            op = 0
            while op not in (1,2,3):
                op = int(input("Digite as opcoes[1-3]: "))

            if op == 1:
                carro1.ligar()
                carro2.ligar()
            elif op == 2:
                carro1.desligar()
                carro2.desligar()
            elif op == 3:
                v1 = float(input("Informe a velocidade do primeiro carro: "))
                t1 = float(input("Informe o tempo do primeiro carro: "))
                carro1.acelerar(v1, t1)
                v2 = float(input("Informe a velocidade do segundo carro: "))
                t2 = float(input("Informe o tempo do segundo carro: "))
                carro2.acelerar(v2, t2)


            print('Infos atuais do carro')
            print(carro1)
            print(carro2)
        except Exception as e:
            print("Erro!")
            print(e)


    carro1.desligar()
    carro2.desligar()
    if carro1.odometro > carro2.odometro:
        print("o carro 1 ganhou!")
    elif carro2.odometro > carro1.odometro:
        print("o carro 2 ganhou!")
    else:
        print("empate!")
    print(carro1)
    print(carro2)


