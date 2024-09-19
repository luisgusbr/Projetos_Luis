def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp = float(input("Digite a temperatura: "))
escala = input("Digite a escala (C/F): ").upper()

if escala == 'C':
    print("Fahrenheit:", celsius_para_fahrenheit(temp))
elif escala == 'F':
    print("Celsius:", fahrenheit_para_celsius(temp))
else:
    print("Escala inválida")
