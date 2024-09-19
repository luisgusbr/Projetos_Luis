# Dados de desempenho por mês: [nome, desempenho_janeiro, desempenho_fevereiro, desempenho_março]
desempenho_funcionarios = [
    ["João", 80, 90, 85],
    ["Maria", 70, 88, 92],
    ["Pedro", 85, 78, 88],
    ["Ana", 90, 95, 92],
    ["Lucas", 60, 65, 70]
]

# Função para calcular a média de desempenho de cada funcionário
def media_desempenho(funcionarios):
    medias = {}
    for funcionario in funcionarios:
        nome = funcionario[0]
        media = sum(funcionario[1:]) / len(funcionario[1:])
        medias[nome] = media
    return medias

# Função para encontrar o melhor e o pior funcionário
def melhor_pior_funcionario(funcionarios):
    medias = media_desempenho(funcionarios)
    melhor = max(medias, key=medias.get)
    pior = min(medias, key=medias.get)
    return melhor, pior

# Gerando o relatório
medias = media_desempenho(desempenho_funcionarios)
melhor, pior = melhor_pior_funcionario(desempenho_funcionarios)

# Exibindo resultados
print("Média de desempenho dos funcionários:")
for nome, media in medias.items():
    print(f"{nome}: {media:.2f}")

print(f"\nMelhor funcionário: {melhor}")
print(f"Pior funcionário: {pior}")
