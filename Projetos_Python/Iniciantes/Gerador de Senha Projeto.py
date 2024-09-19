import random

def gerar_senha(tamanho):
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    senha = ""
    for i in range(tamanho):
        senha += random.choice(caracteres)
    return senha

tamanho_senha = int(input("Digite o tamanho da senha: "))
print("Senha gerada:", gerar_senha(tamanho_senha))