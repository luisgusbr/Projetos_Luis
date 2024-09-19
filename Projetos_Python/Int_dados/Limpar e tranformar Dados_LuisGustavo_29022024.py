# Dataset fictício com inconsistências
dados_clientes = [
    ["Ana", "São Paulo", "ana123@email.com", None],
    ["Carlos", "rio de janeiro", None, "1985-04-10"],
    ["Maria", "SÃO PAULO", "maria@email.com", "1992-08-25"],
    ["José", None, "jose@email.com", "1990-11-14"],
    ["Julia", "Recife", "julia@domain", "1995-06-30"]
]

# Função para limpar e padronizar os dados
def limpar_dados(dados):
    dados_limpos = []
    for cliente in dados:
        nome = cliente[0]
        cidade = cliente[1].title() if cliente[1] else "Desconhecido"
        email = cliente[2] if cliente[2] and "@" in cliente[2] else "Email inválido"
        nascimento = cliente[3] if cliente[3] else "Data desconhecida"
        
        dados_limpos.append([nome, cidade, email, nascimento])
    
    return dados_limpos

# Função para exibir os dados
def exibir_dados(dados):
    for cliente in dados:
        print(f"Nome: {cliente[0]}, Cidade: {cliente[1]}, Email: {cliente[2]}, Nascimento: {cliente[3]}")

# Limpeza dos dados
dados_tratados = limpar_dados(dados_clientes)

# Exibindo dados limpos
print("Dados dos clientes após limpeza:")
exibir_dados(dados_tratados)
