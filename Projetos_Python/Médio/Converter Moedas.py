cotacoes = {"USD": 5.13, "EUR": 5.53, "JPY": 0.037}

def converter_moeda(valor, moeda_origem, moeda_destino):
    if moeda_origem == "BRL":
        return valor / cotacoes[moeda_destino]
    elif moeda_destino == "BRL":
        return valor * cotacoes[moeda_origem]
    else:
        valor_em_brl = valor * cotacoes[moeda_origem]
        return valor_em_brl / cotacoes[moeda_destino]

valor = float(input("Digite o valor a converter: "))
moeda_origem = input("Digite a moeda de origem (USD, EUR, JPY, BRL): ").upper()
moeda_destino = input("Digite a moeda de destino (USD, EUR, JPY, BRL): ").upper()

print(f"Valor convertido: {converter_moeda(valor, moeda_origem, moeda_destino)} {moeda_destino}")
