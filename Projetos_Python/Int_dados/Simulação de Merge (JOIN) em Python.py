# Lista 1 de funcionários com IDs e nomes
funcionarios = [
    {'id': 1, 'nome': 'João'},
    {'id': 2, 'nome': 'Maria'},
    {'id': 3, 'nome': 'Pedro'},
    {'id': 4, 'nome': 'Ana'}
]

# Lista 2 de salários com IDs e valores dos salários
salarios = [
    {'id': 1, 'salario': 3000},
    {'id': 2, 'salario': 4000},
    {'id': 4, 'salario': 3500},
    {'id': 5, 'salario': 2800}  # ID sem correspondência na lista de funcionários
]

# Função para simular um "INNER JOIN"
def merge(inner_list1, inner_list2, key):
    resultado = []
    # Percorre a primeira lista
    for item1 in inner_list1:
        # Para cada item da primeira lista, verifica na segunda lista se há correspondência
        for item2 in inner_list2:
            if item1[key] == item2[key]:
                # Se encontrar correspondência, cria um novo dicionário combinando os dados
                novo_item = {**item1, **item2}
                resultado.append(novo_item)
    return resultado

# Realizando o merge (semelhante a um INNER JOIN)
resultado_inner_join = merge(funcionarios, salarios, 'id')

# Exibindo o resultado do "INNER JOIN"
print("Resultado do INNER JOIN:")
for item in resultado_inner_join:
    print(item)
