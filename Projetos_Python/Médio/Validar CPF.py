def validar_cpf(cpf):
    cpf = [int(digito) for digito in cpf if digito.isdigit()]

    if len(cpf) != 11:
        return False

    for i in range(9, 11):
        soma = sum(cpf[num] * ((i + 1) - num) for num in range(0, i))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != cpf[i]:
            return False
    return True

cpf = input("Digite o CPF (apenas números): ")
if validar_cpf(cpf):
    print("CPF válido.")
else:
    print("CPF inválido.")
