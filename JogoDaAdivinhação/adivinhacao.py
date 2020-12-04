import random


def jogar():
    print("---------------------------------")
    print("Bem vindo ao jogo da Adivinhação.")
    print("---------------------------------")

    vida = 0
    numero_secreto = random.randrange(1, 100)
    pontos = 1000

    print("Escolha um nível: (1) Fácil, (2) Normal, (3) Difícil.")
    nível = int(input("Escolha um nível: "))

    if(nível == 1):
        vida = 20
    elif(nível == 2):
        vida =10
    elif(nível == 3):
        vida = 5


    for rodada in range(1, vida + 1 ):

        print('Tentantiva {} vidas {}\n' .format(rodada, vida))
        chute_str = input("Chute um número 1 entre 100: ")
        chute_int = int(chute_str)

        if chute_int < 1 or chute_int > 100:
            print("Número digitado fora 1 e 100.")
            continue

        acertou = numero_secreto == chute_int
        menor = numero_secreto < chute_int
        maior = numero_secreto > chute_int

        pontos_perdidos = abs(numero_secreto - chute_int)
        pontos = pontos - pontos_perdidos
        if (acertou):
            print(" Parabéns você acertou. Sua pontuação foi {}\n" .format(pontos))
            break
        else:
            if(menor):
                print(" Errou, número secreto é menor")
                if(rodada == vida):
                    print("Número secreto era {}. você fez {} pontos" .format(numero_secreto, pontos))
            elif(maior):
                print(" Errou, número secreto é maior")
                if(rodada == vida):
                    print("Número secreto era {}. você fez {} pontos" .format(numero_secreto, pontos))           
                

    print("\nFim de Jogo.")

if __name__ == "__main__":
    jogar()
