import random
lista_palavras = ["pardal", "babuino", "chupacabra"]

#* TODO-1 - Aleatoriamente escolher uma palavra da lista_palavras e colocar ela na variável chamada 'palavra_escolhida' e 'print' ela
# TODO-2 - Perguntar ao usuário para adivinhar uma letra e assimilar o seu chute para a variável 'chute'. Fazer o chute ser lowercase
# TODO-3 - Checar se a letra que o usuário chutou (chute) é uma das letras da 'palavra_escolhida'. Printar 'CERTO' caso for, 'ERRADO' caso não.
# TODO-4 - Criar um placeholder com o mesmo número de 'brancos' para as 'letras'
# TODO-5 - Criar um display que coloca as letras escolhidas nas posições corretas

# MINHA VERSÃO

# bot escolhe uma das palavras aleatórias
escolha_palavra = random.choice(lista_palavras)

# criação de variáveis
lista_palavra_final = []
vidas = 6
palavra_final = ""

# for para substituir cada letra da palavra por '_'
for letras in escolha_palavra:
    lista_palavra_final += "_"

print("Bem-vindo ao Jogo da Forca do Gordão!")

# loop do jogo
while "_" in lista_palavra_final:
    # caso você erre 6 vezes, você perde
    if vidas == 0:
        print("Você perdeu :(")
        print(f"A palavra era: '{escolha_palavra}'!")
        break
    chute = input(f"Chute uma letra!\n")
    if chute in escolha_palavra:
        for i, letra in enumerate(escolha_palavra):
            if letra == chute:
                lista_palavra_final[i] = chute
                palavra_final = ''.join(lista_palavra_final)
                print("Você acertou uma das letras! A palavra está assim agora: " + str(palavra_final))
    else:
        vidas -= 1
        palavra_final = ''.join(lista_palavra_final)
        print(f"Você errou a letra, restam {vidas} vidas")
        print(f"Palavra atual: {palavra_final}")

    if "_" not in palavra_final:
        print("Parabéns você ganhou!")