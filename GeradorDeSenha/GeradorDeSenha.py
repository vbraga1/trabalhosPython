import random
# frutas = ["maçã" , "pêssego" , "pêra"]
# for fruta in frutas:
#     print(fruta)
#     print("torta de " + fruta)
#
# print(frutas)
from itertools import count

# notas_alunos = [150, 300, 200, 120, 115, 210, 145, 100, 90]
#
# total_nota_alunos = sum(notas_alunos)
#
# soma = 0
# for nota in notas_alunos:
#     soma += nota
#
# print(soma)


# i = 0
# maior_nota = 0
# for nota in notas_alunos:
#     if nota > maior_nota:
#         maior_nota = nota
# print(maior_nota)

#-----------------------------------------------------------------------------------------------------------------------

# total = 0
# for num in range(1, 101):
#     total += num
#     print(total)

#-----------------------------------------------------------------------------------------------------------------------

# numAleatorioLetra = random.randint(0 , 52)
# numAleatorioNUM = random.randint(0, 9)
# numAleatorioSimbolo = random.randint(0, 8)

letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '@', '#', '$', '%', '*', '+', '(', ')']
#senha = ""

#abaixo código para criação de uma senha aleatória sem a função de embaralhamento

print("Bem-vindo ao gerador de senha do Gordão!")
num_letras = int(input("Quantas letras você quer na sua senha?\n"))
num_numeros = int(input(f"Quantos números você quer na sua senha?\n"))
num_simbolos = int(input(f"Quantos símbolos você quer na sua senha?\n"))

# for letra in range(0, num_letras):
#     # senha += random.choice(letras)
#     numAleatorioLetra = random.randint(0, len(letras) - 1)
#     senha += letras[numAleatorioLetra]
# # print(senha)
#
# for num in range(0, num_numeros):
#     # senha += random.choice(numeros)
#     numAleatorioNUM = random.randint(0, len(numeros) - 1)
#     senha += numeros[numAleatorioNUM]
# # print(senha)
#
# for sim in range(0, num_simbolos):
#     # senha += random.choice(simbolos)
#     numAleatorioSimbolo = random.randint(0, len(simbolos) - 1)
#     senha += simbolos[numAleatorioSimbolo]
# # print(senha)

# abaixo é uma das formas de fazer a senha ser embaralhada
# senha_embaralhada = ''.join(random.sample(senha, len(senha)))
# print("Sua senha totalmente aleatória é: " + senha_embaralhada)

#-----------------------------------------------------------------------------------------------------------------------
# MODO EMBARALHAMENTO

lista_senha = []

for letra in range(0, num_letras):
    lista_senha.append(random.choice(letras))
    #numAleatorioLetra = random.randint(0, len(letras) - 1)
    #senha += letras[numAleatorioLetra]
# print(senha)

for num in range(0, num_numeros):
    lista_senha.append(random.choice(numeros))
    ##senha += numeros[numAleatorioNUM]
# print(senha)

for sim in range(0, num_simbolos):
    lista_senha.append(random.choice(simbolos))
    #numAleatorioSimbolo = random.randint(0, len(simbolos) - 1)
    #senha += simbolos[numAleatorioSimbolo]

print(lista_senha)
random.shuffle(lista_senha)
print(lista_senha)
senha = ""
for i in lista_senha:
    senha += i
print("Sua senha totalmente aleatória e embaralhada é: " + senha)