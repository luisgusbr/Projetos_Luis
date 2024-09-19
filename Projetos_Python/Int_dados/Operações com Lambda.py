# Lista de números
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Função lambda para calcular o quadrado de cada número
quadrados = list(map(lambda x: x**2, numeros))
print(f"Quadrado dos números: {quadrados}")

# Função lambda para calcular o cubo de cada número
cubos = list(map(lambda x: x**3, numeros))
print(f"Cubo dos números: {cubos}")

# Função lambda para filtrar apenas os números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}")
