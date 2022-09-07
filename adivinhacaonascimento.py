print("......................................")
print("Bem vindo à adivinhação da minha idade")
print("......................................")

numero_secreto = 1983

chute_str = input("Digite o ano de nascimento: ")
print("Voce digitou ", chute_str)

suposicao = int(chute_str)

acertou = suposicao == numero_secreto
maior  =  suposicao > numero_secreto
menor  =  suposicao < numero_secreto

if(acertou):
    print("Você acertou!! Muito bem!!!")
else:
    if(maior):
        print("Você errou! O seu chute foi maior e espero que você acerte na próxima tentativa")
    if(menor):
        print("Você errou! O seu chute foi menor e espero que você acerte na próxima tentativa")


print("Good Luck!!!")