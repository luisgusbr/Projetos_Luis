def calculadora(a, b, operacao):
    if operacao == '+':
        return a + b
    elif operacao == '-':
        return a - b
    elif operacao == '*':
        return a * b
    elif operacao == '/':
        return a / b
    else:
        return "Operação inválida"

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
op = input("Escolha a operação (+, -, *, /): ")

resultado = calculadora(num1, num2, op)
print("Resultado:", resultado)