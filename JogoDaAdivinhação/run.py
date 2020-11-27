print("---------------------------------")
print("Bem vindo ao jogo da Adivinhação.")
print("---------------------------------")

vida = 3
rodada = 1
numero_secreto = 142


while (vida > 0):

    print('vidas {}\n' .format(vida))
    chute = input("Tente adivinhar o número secreto: ")
    chute_int = int(chute)

    acertou = numero_secreto == chute_int
    menor = numero_secreto < chute_int
    maior = numero_secreto > chute_int

    if (acertou):
        print("\n Parabéns você acertou.\n")
        vida = 1
    else:
        if(menor):
            print("\n Errou, número secreto é menor\n")
        elif(maior):
            print("\n Errou, número secreto é maior\n")
    
    
    vida -= 1

print("\nFim de Jogo.")
