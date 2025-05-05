import random
# #import meu_Modulo
#
# #randomInt = random.randint(1, 10)
#
# #print(randomInt)
#
# #print(meu_Modulo.meuNumFav)
#
# # numAleatorioEntre0e1 = random.random() * 10
# # print(numAleatorioEntre0e1)
#
# # floatAleatorio = random.uniform(1, 10)
# # print(floatAleatorio)



# escolha = input("Você escolhe cara ou coroa? Digite '0' para CARA e '1' para COROA ")
#
# var = random.randint(0,1)
# print(var)
#
# if var == 0 and escolha == "0":
#     print("Deu cara, você ganhou!")
# elif var == 0 and escolha == "1":
#     print("Deu cara, você perdeu :(")
# elif var == 1 and escolha == "0":
#     print("Deu coroa, você perdeu :(")
# else:
#     print("Deu coroa, você ganhou!")


# estados_do_brasil = ["sao paulo", "rio de janeiro", "minas gerais"]
#
# estados_do_brasil.append("ceara")
#
# estados_do_brasil.extend(["acre", "rio grande do sul"])
#
# print(estados_do_brasil)



# amigos = ["buda", "braga", "simo", "salgado", "costa", "felps"]
#
# numRandom = random.randint(0,5)
# print(amigos[numRandom])
#
# #outra solução
# print(random.choice(amigos))



# estados_do_sudeste = ["rio", "sp", "mg" "es"]
# estados_do_sul = ["pr", "sc", "rs"]
#
# estados_do_brasil = [estados_do_sudeste, estados_do_sul]
# print(estados_do_brasil)



escolha = input("Pedra, Papel ou Tesoura? Digite '1', '2' ou '3', respectivamente à escolha ")
escolhaBot = random.randint(1,3)
escolhaBot = str(escolhaBot)

if escolha == "1" and escolhaBot == "2":
    print("Você escolheu Pedra ")
    print("Ele escolheu Papel")
    print("Você perdeu...")
elif escolha == "1" and escolhaBot == "3":
    print("Você escolheu Pedra ")
    print("Ele escolheu Tesoura")
    print("Você ganhou!!!")
elif escolha == "2" and escolhaBot == "1":
    print("Você escolheu Papel ")
    print("Ele escolheu Pedra")
    print("Você ganhou!!!")
elif escolha == "2" and escolhaBot == "3":
    print("Você escolheu Papel ")
    print("Ele escolheu Tesoura")
    print("Você perdeu...")
elif escolha == "3" and escolhaBot == "1":
    print("Você escolheu Tesoura ")
    print("Ele escolheu Pedra")
    print("Você perdeu...")
elif escolha == "3" and escolhaBot == "2":
    print("Você escolheu Tesoura ")
    print("Ele escolheu Papel")
    print("Você ganhou!!!")
else:
    if escolha == "1":
        print("Ambos escolheram Pedra, empate!")
    if escolha == "2":
        print("Ambos escolheram Papel, empate!")
    if escolha == "3":
        print("Ambos escolheram Tesoura, empate!")