nome = input ("Olá, qual o seu nome?")
print ("olá", nome, "seja bem- vindo, vamos calcular seu IMC")
idade = int(input("Qual a sua idade?: "))
peso = float(input("Qual o seu peso?(kg): "))
altura = float(input("Qual a sua altura?(metros): "))

imc=peso / (altura ** 2)
if imc < 18.5:
    print(nome, "você está abaixo do peso")
elif imc >= 18.5 and imc < 24.9:
    print(nome, "você está com o peso normal")
elif imc >= 25 and imc < 29.9:
    print(nome, "você está com sobrepeso")
else:
    print(nome, "você está obeso")  
print(f"seu IMC é: {imc: .2f}")

