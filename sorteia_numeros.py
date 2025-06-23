import random

print("-- Sorteador de números --")

while True:
    opcao = int(input("Digite:\n1 - Sortear\n2 - Sair: "))
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
            print("Encerrando sorteador de número")
            break
        case _:
            print("Opção inválida!")