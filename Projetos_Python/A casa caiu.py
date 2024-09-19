def contar_palavras(frase):
    palavras = frase.split()
    return len(palavras)

frase = input("Digite uma frase: ")
print("Número de palavras:", contar_palavras(frase))
