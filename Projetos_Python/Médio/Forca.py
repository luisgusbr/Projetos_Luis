palavra_secreta = "python"
letras_adivinhadas = ['_' for _ in palavra_secreta]
tentativas = 6

while tentativas > 0 and ''.join(letras_adivinhadas) != palavra_secreta:
    letra = input("Digite uma letra: ").lower()

    if letra in palavra_secreta:
        for idx, l in enumerate(palavra_secreta):
            if l == letra:
                letras_adivinhadas[idx] = letra
    else:
        tentativas -= 1
        print(f"Letra errada! Tentativas restantes: {tentativas}")
    
    print(' '.join(letras_adivinhadas))

if ''.join(letras_adivinhadas) == palavra_secreta:
    print("Parabéns! Você ganhou!")
else:
    print("Você perdeu!")
