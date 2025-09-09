#calculadora
def somar (num1, num2):
    somar= num1 + num2
    return somar

def subtrair (num1, num2):
    subtrair= num1 - num2
    return subtrair

def multiplicar (num1, num2):
    multiplicar= num1 * num2
    return multiplicar

def dividir (num1, num2):
    try:
        divisao = num1 / num2
        return divisao
    # Tratamento de erro
    except ZeroDivisionError:
        return "Nenhum número pode ser dividido por 0"
    


opcao= input("Escolha uma opção (+, -, *, /): ")
num1= float(input("Insira primeiro número: "))
num2= float(input("Insira segundo número: "))

if opcao == "+":
    equacao = "soma"
    resultado = somar(num1, num2)
    print(resultado)
elif opcao == "-":
    equacao = "subtração"
    resultado = subtrair(num1, num2)
    print(resultado)
elif opcao == "*":
    equacao = "multiplicação"
    resultado = multiplicar(num1, num2)
    print(resultado)
else:
    equacao = "/"
    resultado = dividir(num1, num2)
    print(resultado)