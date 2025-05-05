#print("Bem-vindo a Montanha-Russa do Gordão")
#altura = int(input("Qual a sua altura em centímetros? "))
#idade = int(input("Qual sua idade? "))
#contaTotal = 0

#if altura > 120:
    #if idade >= 18:
        #contaTotal += 12
        #print("Você pode andar na Montanha-Russa do Gordão, o ingresso adulto é 12")
    #elif idade < 12:
        #contaTotal += 5
        #print("Você pode andar na Montanha-Russa do Gordão, o ingresso de criança é 5")
    #else:
        #contaTotal += 7
        #print("Você pode andar na Montanha-Russa do Gordão, o ingresso de adolescente é 7")

    #querFoto = input("Você quer pagar pelas fotos? Digite 'S' para sim ou 'N' para não ")
    #if querFoto == "S":
        #contaTotal += 3
    #print("Obrigado por andar na Montanha-Russa do Gordão, você deve pagar ao total: " + str(contaTotal))
#else:
    #print("Desculpe, você não tem altura suficiente para andar na Montanha-Russa do Gordão")



#var = int(input("Digite um número aleatório: "))

#if var % 2 == 0:
    #print("Par")
#else:
    #print("Ímpar")



# print("Bem-vindo ao Delivery de Pizzas Gordão")
# tamanhoPizza = input("Qual será o tamanho da pizza? Digite 'P' para pequena, 'M' para média, 'G' para grande ")
# calabresaAdd = input("Quer adicional de Calabresa? Digite 'S' para sim ou 'N' ")
# queijoAdd = input("Quer adicional de Queijo? Digite 'S' para sim ou 'N' para não ")
# total = 0
#
# if tamanhoPizza == "P":
#     total += 15
#     if calabresaAdd == "S":
#         total += 2
#     if queijoAdd == "S":
#         total += 1
#
# if tamanhoPizza == "M":
#     total += 20
#     if calabresaAdd == "S":
#         total += 3
#     if queijoAdd == "S":
#         total += 1
#
# if tamanhoPizza == "G":
#     total += 25
#     if calabresaAdd == "S":
#         total += 3
#     if queijoAdd == "S":
#         total += 1
#
# print("Seu total ficou: " + str(total))

print("Bem-vindo a Ilha do Tesouro!")
print("Sua missão é achar o tesouro!")
print("Você se depara com dois caminhos, um lago para atravessar nadando na esquerda e uma floresta densa e escura na direita")
var = input("Você vai para a direita ou esquerda? Digite 'D' para direita e 'E' para esquerda ")

if var == "D":
    print("Você caiu em um buraco e morreu")
    print("Game Over")
else:
    var = input("Você vai atravessar o lago nadando ou esperar? 'N' para nadar ou 'E' para esperar ")
    if var == "N":
        print("Você foi atacado por uma piranha")
        print("Game over")
    else:
        print("Um barco magicamente aparece minutos depois e você consegue atravessar o lago")
        print("Agora você se depara com uma casa com três portas diferentes")
        var = input("Qual porta você escolhe? 'V' para vermelha, 'P' para preta e 'A' para azul ")
        if var == "V":
            print("Você pegou fogo e morreu")
            print("Game over")
        elif var == 'P':
            print("Parabéns, você achou o tesouro!")
        elif var == 'A':
            print("Você foi comido por bestas")
            print("Game over")
        else:
            print("Game over")