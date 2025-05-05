

print("Bem-vindo à Calculadora de Gorjeta")
total = int(input("Qual o valor final gasto? "))
gorjeta = int(input("Qual o valor da gorjeta? 10, 12 ou 15? "))
numPessoas = int(input("A conta será divida em quantas pessoas? "))

#print("***")
#print(total)
#print(gorjeta)
#print(numPessoas)
#print("***")

totalFinal = round(((total + gorjeta) / numPessoas))
print("O valor final para cada um pagar será de: " + str(totalFinal))

