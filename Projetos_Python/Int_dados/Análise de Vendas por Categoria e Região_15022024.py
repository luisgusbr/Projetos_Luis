# Dados fictícios de vendas: [categoria, região, valor da venda]
vendas = [
    ["Eletrônicos", "Norte", 1000],
    ["Móveis", "Sul", 1500],
    ["Eletrônicos", "Nordeste", 750],
    ["Vestuário", "Sudeste", 500],
    ["Móveis", "Nordeste", 1200],
    ["Vestuário", "Norte", 700],
    ["Eletrônicos", "Sul", 950],
    ["Vestuário", "Nordeste", 600]
]

# Função para calcular o total de vendas por categoria e por região
def total_por_categoria(vendas):
    total_categoria = {}
    for venda in vendas:
        categoria = venda[0]
        valor = venda[2]
        if categoria not in total_categoria:
            total_categoria[categoria] = 0
        total_categoria[categoria] += valor
    return total_categoria

def total_por_regiao(vendas):
    total_regiao = {}
    for venda in vendas:
        regiao = venda[1]
        valor = venda[2]
        if regiao not in total_regiao:
            total_regiao[regiao] = 0
        total_regiao[regiao] += valor
    return total_regiao

# Função para calcular a média de vendas por categoria
def media_vendas_por_categoria(vendas):
    total_categoria = total_por_categoria(vendas)
    contagem_categoria = {cat: 0 for cat in total_categoria}
    
    for venda in vendas:
        categoria = venda[0]
        contagem_categoria[categoria] += 1
    
    media_por_categoria = {cat: total_categoria[cat] / contagem_categoria[cat] for cat in total_categoria}
    return media_por_categoria

# Relatórios
total_cat = total_por_categoria(vendas)
total_reg = total_por_regiao(vendas)
media_cat = media_vendas_por_categoria(vendas)

# Exibindo resultados
print("Total de vendas por categoria:")
for cat, total in total_cat.items():
    print(f"Categoria {cat}: R${total:.2f}")

print("\nTotal de vendas por região:")
for reg, total in total_reg.items():
    print(f"Região {reg}: R${total:.2f}")

print("\nMédia de vendas por categoria:")
for cat, media in media_cat.items():
    print(f"Categoria {cat}: R${media:.2f}")
