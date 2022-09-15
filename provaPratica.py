#questão 1

valorA = float(input("Digite o primeiro número: "))
valorB = float(input("Digite o segundo número: "))
valorC = float(input("Digite o terceiro número: "))
if valorA > valorB and valorA > valorC:
    print("O primeiro valor é maior.")
elif valorB > valorA and valorB > valorC:
    print("O segundo valor é maior.")
else:
    print("O terceiro valor é maior.")

#questão 2

idade = int(input("Digite sua idade: "))
tempoTrabalho = int(input("Digite por quantos anos você trabalhou: "))
if idade >= 65 or tempoTrabalho >= 30:
    print("Você pode se aposentar.")
elif idade >= 60 and tempoTrabalho >= 25:
    print("Você pode se aposentar.")
else:
    print("Você não pode se aposentar.")

#questão 3

print("Olá! Este é o jogo da forca, de uma letra só, você tem 5 tentativas")
letra = "m"
contador = 0

while contador <=5:
    letraUsuario = input("escolha uma letra: ")
    if letra != letraUsuario:
        contador += 1
        print("Você errou, tente de novo")
    else:
        break
    if letra == letraUsuario:
        print("Você ganhou")
    else:
        break


#questão 4

print("Digite se quer - 1: ver seu saldo, 2: fazer um saque, 3: fazer um depósito ou 4: sair.")
saldo = input(1)
saque = input(2)
deposito =  input(3)
sair = input()


