import random

print("-- Sorteador de números --")

opcao = int(input("Digite 1 para sortear ou 2 para sair: "))

match opcao:
    case 1:
        quantidade = int(input("Digite a quantidade de números a serem sorteado: "))
        minimo = int(input("Digite o valor mínimo a ser sorteado: "))
        maximo = int(input("Digite o valor máximo a ser sorteado: "))

        resultado = []

        for i in range(quantidade):
            sorteados = random.randint(minimo, maximo)
            resultado.append(sorteados)

        print(sorted(set(resultado)))
    case 2:
        print("Encerrando o sorteador!")
    
