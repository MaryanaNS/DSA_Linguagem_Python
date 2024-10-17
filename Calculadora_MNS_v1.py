# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos até aqui no curso. 
# A solução será apresentada no próximo capítulo!

print("\n******************* Calculadora em Python *******************\n")
print("Selecione a opção desejada:\n\n 1 - Soma\n 2 - Subtração\n 3 - Multiplicação\n 4 - Divisão\n 5 - Quadrado\n 6 - Porcentagem\n")

opcao = input("Digite sua opção (1/2/3/4/5/6): \n")


def somar (num1, num2):
    soma = num1 + num2
    print("\n%d + %d = %d \n" %(numero1, numero2, soma))

def subtrair (num1, num2):
    sub = num1 - num2
    print("\n%d - %d = %d \n" %(numero1, numero2, sub))

def multiplicar (num1, num2):
    multi = num1 * num2
    print("\n%d x %d = %d \n" %(numero1, numero2, multi))

def dividir (num1, num2):
    div = float(num1 / num2)
    print("\n%d / %d = %.1f \n" %(numero1, numero2, div))

def elevar (num1):
    quad = num1 ** 2
    print("\n%d elevado ao quadrado é %d \n" %(numero1, quad))

def porcentagem (num1):
    percent = float(num1 / 100)
    print("\n%d%% = %.2f \n" %(numero1, percent))

for i in opcao:
    if opcao == '1':
        numero1 = int(input("\nDigite um número inteiro: "))
        numero2 = int(input("\nDigite outro número inteiro: "))
        somar(numero1, numero2)
    elif opcao == '2':
        numero1 = int(input("\nDigite um número inteiro: "))
        numero2 = int(input("\nDigite outro número inteiro: "))
        subtrair(numero1, numero2)
    elif opcao == '3':
        numero1 = int(input("\nDigite um número inteiro: "))
        numero2 = int(input("\nDigite outro número inteiro: "))
        multiplicar(numero1, numero2)
    elif opcao == '4':
        numero1 = int(input("\nDigite um número inteiro: "))
        numero2 = int(input("\nDigite outro número inteiro: "))
        dividir(numero1, numero2)     
    elif opcao == '5':
        numero1 = int(input("\nDigite um número inteiro: "))
        elevar(numero1)
    elif opcao == '6':
        numero1 = int(input("\nDigite um número inteiro: "))
        porcentagem(numero1)
    else:
        print('Opção inválida!')	
