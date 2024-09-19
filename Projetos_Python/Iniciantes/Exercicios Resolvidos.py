#Exercício 1
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

soma = numero1 + numero2 + numero3

print("O resultado da soma é: ", soma)

#Exercício 2
ano_atual = float(input("Digite o ano atual: "))
ano_nascimento = float(input("Digite o ano de nascimento da pessoa: "))

idade_pessoa = ano_atual - ano_nascimento

print("A idade da pessoa em anos é: ", idade_pessoa)

#Exercício 3
metragem_lado = float(input("Digite a metragem de um dos lados: "))

metro_quadrado = metragem_lado * metragem_lado

print("A metragem da área é: ", metro_quadrado)

#Exercício 4
metragem1 = float(input("Digite a metragem de um dos lados: "))
metragem2 = float(input("Digite a metragem do outro lado: "))

metro_quadrado = metragem1 * metragem2

print("A metragem da área é: ", metro_quadrado, "m2")

#Exercício 5
metragem_quadrado = float(input("Digite a metragem de um dos lados: "))

perimetro_quadrado = metragem_quadrado * 4

print("O perímetro do quadrado é: ",perimetro_quadrado,"em metros")

#Exercício 6
metragem1 = float(input("Digite o lado maior: "))
metragem2 = float(input("Digite o lado menor: "))

perimetro_retangulo = (metragem1*2) + (metragem2*2)

print("O perimetro do retangulo é: ", perimetro_retangulo,"em metros")

#Exercício 7
numero = float(input("Digite o número que deseja o dobro: "))

dobro = numero*2

print("O dobro do número ", numero, "é:", dobro)

#Exercício 8
preco_produto = float(input("Digite o valor do produto: "))

preco_desconto = preco_produto - (preco_produto * 10/100)

print("O preço do produto com desconto é: R$", preco_desconto)

#Exercício 9
angulo1 = float(input("Digite o ângulo do primeiro lado do triângulo: "))
angulo2 = float(input("Digite o ângulo do segundo lado do triângulo: "))

angulo3 = 180 - angulo1 - angulo2

print("O ângulo do terceiro lado do triângulo é: ", angulo3)

#Exercício 10
valor_minimo = float(input("Digite o valor do salário mínimo atual: "))
salario_funcionario = float(input("Digite o salário do funcionário: "))

qtd_salario = salario_funcionario / valor_minimo

print("O funcionário recebe", qtd_salario,"salários mínimos")

#Exercício 11
salario_fixo = float(input("Digite o salário fixo do funcionário: "))
valor_vendas = float(input("Digite o valor total das vendas: "))

comissao = valor_vendas * (4/100)

salario_final = salario_fixo + comissao

print("A comissão do vendedor é: R$", comissao, ", o seu salário final é: R$", salario_final)

#Exercício 12
num_horas = float(input("Digite o número de horas trabalhadas: "))
salario_minimo = float(input("Digite o valor do salário mínimo: "))

#a
hora_trabalhada = salario_minimo / 2

#b
salario_bruto = num_horas * hora_trabalhada

#c
imposto = salario_bruto * (3/100)

#d
salario_receber = salario_bruto - imposto

print("O funcionário tem a receber: ", salario_receber)

#Exercício 13
custo = float(input("Qual foi o custo do espetáculo?: "))
valor_convite = float(input("Qual o valor do convite?: "))

vendas_necessarias = custo/valor_convite

print("A quantidade de venda necessária para ficar no 0 à 0 é: ", vendas_necessarias)

#Exercício 14
salario_base = float(input("Digite o valor base do funcionário: "))

gratificacao = salario_base * 5/100
imposto = salario_base * 7/100

salario_receber = salario_base - imposto + (gratificacao)

print("O salário a receber do funcionário é: R$", salario_receber)

#Exercício 15 - É a mesma questão do exercício 13

#Exercício 16
salario_minimo = float(input("Digite o valor do salário mínimo: "))
consumo_kw = float(input("Digite a quantidade de KW consumida: "))

#a
valor_kw = salario_minimo * 20/100

#b
fatura = valor_kw * consumo_kw

#c
desconto = fatura * 15/100

valor_pagar = fatura - desconto

print("O valor para pagar é: R$", valor_pagar)

#Exercício 17
ano_nascimento = float(input("Digite o ano do nascimento: "))
ano_atual = float(input("Digite o ano atual: "))

#a
idade_anos = ano_atual - ano_nascimento

#b
idade_meses = idade_anos * 12

#c
idade_dias = idade_meses * 30

#d
idade_horas = idade_dias * 24

#e
idade_min = idade_horas * 60

#f
idade_seg = idade_min * 60

print("A idade da pessoa é: \n Em anos é: ", idade_anos, "anos" "\n Em meses é: ", idade_meses, "meses" "\n Em dias é: ", idade_dias, "dias" "\n Em horas é ", idade_horas, "horas" "\n Em minutos é: ", idade_min, "minutos" "\n Em segundo é: ", idade_seg, "segundos")

#Exercício 18
dim1 = float(input("Digite a metragem do primeiro lado: "))
dim2 = float(input("Digite a metragem do segundo lado: "))

metro_quadrado = dim1 * dim2
potencia = metro_quadrado * 18

print("A poteênica à ser utilizada para a iluminação em Watts em um cômodo de ",metro_quadrado, "é de: ", potencia)

#Exercício 19
num_horas_trabalhadas = float(input("Digite o número de horas trabalhadas: "))
salario_minimo = float(input("Digite o valor do salário mínimo atual: "))
horas_extras = float(input("Digite o número de horas extras: "))

#a
valor_trabalhada = salario_minimo / 8

#b
valor_extra = salario_minimo / 4

#b
salario_bruto = num_horas_trabalhadas * valor_trabalhada

#d
receber_extra = horas_extras * valor_extra

#e
receber_total = receber_extra + salario_bruto

print("O valor que o funcionário irá receber é de: R$", receber_total)

#Exercício 20
av1 = float(input("Digite a nota da avaliação 1: "))
av2 = float(input("Digite a nota da avaliação 2: "))

media_final = (av1 + av2) / 2

print("A média final é: ", media_final)

#13 - Faça um programa para ordenar dois números.

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 < numero2:
  print("A ordem do menor para maior é:", numero1,",", numero2)

else:
  print("A ordem do menor para maior é:", numero2,",", numero1)

#14 - Elabore um programa que leia um número e, se ele for positivo, apresente a metade desse número, caso contrário apresente o número ao quadrado.

numero = float(input("Digite o número: "))

if numero >= 1:
  metade = numero / 2
  print("A metade do número positivo", numero,"é", metade)

else:
  quadrado = numero * numero
  print("O número negativo", numero,"ao quadrado é", quadrado)

#15 - Elabore um programa que leia um valor e escrever a mensagem É MAIOR QUE 10! se o valor lido for maior que 10, caso contrário escrever NÃO É MAIOR QUE 10!

valor = float(input("Digite o valor: "))

if valor > 10:
  print("É MAIOR QUE 10!")

else:
  print("NÃO É MAIOR QUE 10!")

#16 - Faça um programa que receba quatro notas de um aluno, calcule e apresente a média aritmética das notas e a mensagem “aprovado” ou “reprovado”, considerando para aprovação média 8,0.

av1 = float(input("Digite a 1ª nota: "))
av2 = float(input("Digite a 2ª nota: "))
av3 = float(input("Digite a 3ª nota: "))
av4 = float(input("Digite a 4ª nota: "))

media_ari = (av1 + av2 + av3 + av4) / 4

if media_ari >= 8.0:
  print("APROVADO")

else:
  media_ari < 8.0
  print("REPROVADO")

#17 - As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia, e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o número de maçãs compradas, calcule e escreva o custo total da compra.

n_macas = int(input("Digite o número de maças compradas: "))

if n_macas >= 12:
  preco1 = n_macas * 1.0
  print("O custo total da compra é: R$",preco1)

else:
  preco2 = n_macas * 1.30
  print("O custo total da compra é: R$",preco2)

#18 - Escreva um programa que leia um número inteiro e escreva se é múltiplo de 9.

n_inteiro = int(input("Digite o número inteiro: "))

if (n_inteiro%9==0):
  print("O número é múltiplo de 9")

else:
  print("O número não é múltiplo de 9")

#19 - O sistema de avaliação de uma determinada disciplina é composto por três provas. A primeira prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5.
#Considerando que a média para aprovação é 9.0, faça um programa para calcular a média final de um aluno desta disciplina e dizer se o aluno foi aprovado ou não.

av1 = int(input("Digite a nota 1: "))
av2 = int(input("Digite a nota 2: "))
av3 = int(input("Digite a nota 3: "))

peso_av1 = av1 * (20/100)
peso_av2 = av2 * (30/100)
peso_av3 = av3 * (50/100)

media_final = peso_av1 + peso_av2 + peso_av3

if media_final >= 9:
    print("Sua média foi de",media_final,",você foi APROVADO!")
else:
    print("Sua média foi de,",media_final,"infelizmente você foi REPROVADO!")

#20 - Faça um programa leia o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano
#(não é necessário considerar o mês em que a pessoa nasceu).

ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = int(input("Digite o ano de nascimento: "))

idade = ano_atual - ano_nascimento

if idade >= 16:
    print("Você tem",idade,", anos e pode votar este ano.")
else:
    print("Você tem",idade,", anos e não pode votar este ano.")

#21 - Faça um programa que leia um número inteiro e imprima o seu antecessor (inteiro anterior) e o seu sucessor (inteiro posterior).

numero = int(input("Digite um número inteiro: "))

antecessor = numero - 1
sucessor = numero + 1

print("O antecessor de",numero,"é",antecessor,)
print("O sucessor de",numero,"é",sucessor,)


#Professor, não encontrei a utilização de if e else, depois se puder me clarear. Obg

#22 - Escreva um programa que leia dois valores inteiros representando, respectivamente, um valor de hora e um de minutos e
#informe quantos minutos se passaram deste o início do dia.

hora = int(input("Digite a hora de 0 à 23: "))
minutos = int(input("Digite os minutos de 0 à 59: "))

# Verifica se os valores estão dentro dos intervalos válidos
if hora <= hora <= 23 and minutos <= 59:
        minutos_dia = (hora * 60) + minutos
        print("Desde o início do dia, se passaram",minutos_dia,"minutos.")

else:
        print("Horas e/ou minutos inválidos. Digite um valor entre 0 e 23 para horas e 0 e 59 para minutos.")
        
        
        #1. De acordo com o artigo 130 da Consolidação das Leis de Trabalhos (CLT), o trabalhador que possui carteira assinada
#tem direito a 30 dias de férias remuneradas, depois de completar 12 meses seguidos na empresa, podendo esse período
#ser menor se houver faltas injustificadas, conforme relação abaixo.

#- 30 dias corridos de férias, quando não houver mais de cinco faltas no serviço;
#- 24 dias corridos de férias, quando houver de 6 a 14 faltas;
#- 18 dias corridos de férias, quando houver de 15 a 23 faltas;
#- 12 dias corridos de férias, quando houver de 24 a 32 faltas;

#Faça um programa que informe a quantidade de dias que um funcionário terá de férias.


qt_faltas = int(input("Digite o número de faltas que o colaborador teve: "))

if qt_faltas <= 5:
  print("O Colaborador terá 30 dias de férias!")

elif (qt_faltas >=6 and qt_faltas <=14):
  print("Colaborador terá 24 dias de férias")

elif (qt_faltas >=15 and qt_faltas <=23):
  print("Colaborador terá 18 dias de férias")

elif (qt_faltas >=24 and qt_faltas <=32):
  print("Colaborador terá 12 dias de férias")

else:
  print("Colaborador não terá férias")

#2. Num certo município, vários proprietários de imóveis estão em atraso com o pagamento do IPTU.
#Quando o pagamento está em atraso o cálculo do valor atualizado e realizado da seguinte forma:

#- O valor da multa é de 5% sobre o valor do IPTU;
#- O valor do juro é calculado conforme a tabela abaixo:

#_________________________________________________________________
#Valor do IPTU             |         % por cada mês em atraso    |
#Até 50,00                 |                 1%                  |
#De 50,01 a 500,00         |                 4%                  |
#De 500,01 a 1200,00       |                 9%                  |
#Acima de 1200,00          |                15%                  |
#-----------------------------------------------------------------

#- O total a ser pago pelo proprietário é a soma do valor do IPTU com o valor da multa e com o valor do juro.
#Faça um programa para calcular o valor total a ser pago pelo proprietário.


valor_iptu = float(input("Digite o valor do IPTU: "))
meses_atrasados = int(input("Digite a quantidade de meses em atrados: "))

if valor_iptu <=50:
   valor_pagar1 = valor_iptu + ((valor_iptu*0.01)*meses_atrasados) + (valor_iptu*0.05)
   print("O valor à pagar é R$",valor_pagar1,)

elif valor_iptu >=51 and valor_iptu <=500:
   valor_pagar2 = valor_iptu + ((valor_iptu*0.04)*meses_atrasados) + (valor_iptu*0.05)
   print("O valor à pagar é R$",valor_pagar2,)

elif valor_iptu >=501 and valor_iptu <=1200:
   valor_pagar3 = valor_iptu + ((valor_iptu*0.09)*meses_atrasados) + (valor_iptu*0.05)
   print("O valor à pagar é R$",valor_pagar3,)

else:
   valor_iptu >=1201
   valor_pagar4 = valor_iptu + ((valor_iptu*0.15)*meses_atrasados) + (valor_iptu*0.05)
   print("O valor à pagar é R$",valor_pagar4,)

#3. Faça um programa que leia cada dígito de um CPF, calcule e apresente o controle do CPF.

#CPF  331.017.749-18

#Cálculo do 1° digito do controle:
#Multiplicar cada número pela sequência 10 a 2

#CPF         Fator
#3     x       10      =     30
#3     x       9       =     27
#1     x       8       =      8
#0     x       7       =      0
#1     x       6       =      6
#7     x       5       =     35
#7     x       4       =     28
#4     x       3       =     12
#9     x       2       =     18

#Calcular o somatório dos resultados.
#30 + 27 + 8 + 0 + 6 + . . .  + 18

#Calcular o resto da divisão do somatório por 11
#O primeiro digito será o resultado da subtração de 11 pelo resto.
#Quando o primeiro dígito for maior que 9, o dígito será 0.

#Cálculo do 2° digito do controle:
#Multiplicar cada número pela sequência 11 a 2

#CPF     Fator
#3     x       11      =    33
#3     x       10      =    30
#1     x       09      =    09
#0     x       08      =    00
#1     x       07      =    07
#7     x       06      =    42
#7     x       05      =    35
#4     x       04      =    16
#9     x       03      =    27
#dig1  x       02      =    X

#Calcular o somatório dos resultados.
#Calcular o resto da divisão do somatório por 11.
#O primeiro digito será o resultado da subtração de 11 pelo resto.
#Quando o primeiro dígito for maior que 9, o dígito será 0.


num1 = int(input("Digite o primeiro número do CPF: "))
num2 = int(input("Digite o segundo número do CPF: "))
num3 = int(input("Digite o terceiro número do CPF: "))
num4 = int(input("Digite o quarto número do CPF: "))
num5 = int(input("Digite o quinto número do CPF: "))
num6 = int(input("Digite o sexto número do CPF: "))
num7 = int(input("Digite o sétimo número do CPF: "))
num8 = int(input("Digite o oitavo número do CPF: "))
num9 = int(input("Digite o nono número do CPF: "))

#Cálculo 1º digito:
primeiro_digito = (num1*10)+(num2*9)+(num3*8)+(num4*7)+(num5*6)+(num6*5)+(num7*4)+(num8*3)+(num9*2)
resto_1 = primeiro_digito % 11

if resto_1 < 2:
   primeiro_digito = 0

else:
  primeiro_digito = 11 - resto_1

#Cálculo 2º digito:
segundo_digito = (num1*11)+(num2*10)+(num3*9)+(num4*8)+(num5*7)+(num6*6)+(num7*5)+(num8*4)+(num9*3)+(primeiro_digito*2)
resto_2 = segundo_digito % 11

if resto_2 < 2:
   segundo_digito = 0

else:
  segundo_digito = 11 - resto_2

print("O primeiro dígito do CPF é:",primeiro_digito, "e opsegundo dígito do CPF é:",segundo_digito,)

#1. Elabore um programa que leia o salário de uma pessoa, calcule e escreva o valor do desconto referente ao INSS seguindo a tabela a seguir:

salario = float(input("Digite o salário: "))

if salario <= 600:
  print("Isento de INSS")

elif salario >= 601 and salario <= 1200:
  inss_20 = (salario * (20/100))
  print("Valor do INSS à descontar do seu salário é",inss_20)

elif salario >= 1201 and salario <= 2000:
  inss_25 = (salario * (25/100))
  print("Valor do INSS à descontar do seu salário é",inss_25)

else:
  salario >= 2001
  inss_30 = (salario * (30/100))
  print("Valor do INSS à descontar do seu salário é",inss_30)

#2. Sabe-se que a direção de uma determinada escolinha faz a distribuição de seus alunos de
#acordo com as idades dos mesmos. Dessa forma, os alunos são distribuídos nas seguintes turmas
#de acordo com a classificação a seguir:

idade_aluno = float(input("Digite a idade do aluno: "))

if (idade_aluno >= 4 and idade_aluno <= 5):
    print("Aluno é da turma A")

elif (idade_aluno >= 6 and idade_aluno <= 8):
    print("Aluno é da turma B")

elif (idade_aluno >= 9 and idade_aluno <= 10):
    print("Aluno é da turma C")

else:
  print("Escola não possui turmas para essa idade")

#3. Considerando o sistema de avaliação das médias a seguir, escreva um programa que leia a
#média de um aluno, e escreva o conceito correspondente e a mensagem: “APROVADO” se o conceito for
#A, B, ou C e “REPROVADO” se o conceito for D ou E.

media_aluno = float(input("Digite a média do aluno: "))

if media_aluno >= 9:
   print("A média do aluno é",media_aluno,"o conceito dele é A, o aluno está APROVADO!")

elif media_aluno >= 7.5 and media_aluno <9:
   print("A média do aluno é",media_aluno,"o conceito dele é B, o aluno está APROVADO!")

elif media_aluno >= 6.0 and media_aluno <7.5:
   print("A média do aluno é",media_aluno,"o conceito dele é C, o aluno está APROVADO!")

elif media_aluno >= 4.0 and media_aluno <6.0:
   print("A média do aluno é",media_aluno,"o conceito dele é D, o aluno está REPROVADO!")

elif media_aluno < 4.0:
   print("A média do aluno é",media_aluno,"o conceito dele é E, o aluno está REPROVADO!")

#4. Faça um programa que leia o ano e escreva se ele é bissexto. Um ano será bissexto se
#for divisível por 400, ou se for divisível por 4 e não for divisível por 100.

ano = float(input("Digite o ano em que deseja saber: "))

if (ano%4==0) or (ano%100==0):
  print("O ano é bissexto")

elif ano % 400 != 0:
  print("O ano não é bissexto")

#5. Escreva um programa para ler o número total de eleitores de um município, o número de votos
#brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação ao
#total de eleitores.

votos_brancos = float(input("Digite o número de votos brancos do município: "))
votos_nulos = float(input("Digite o número de votos nulos do município: "))
votos_validos = float (input("Digite o número de votos válidos do município: "))

eleitores_municipio = votos_brancos + votos_nulos + votos_validos

perc_brancos = round((votos_brancos/eleitores_municipio) *100, 2)
perc_nulos = round((votos_nulos/eleitores_municipio) * 100, 2)
perc_validos = round((votos_validos/eleitores_municipio) * 100, 2)

print("Informações eleitorais do município: \nO total de eleitores do munucípio é:",eleitores_municipio,"\nO percentual de votos brancos é:",perc_brancos,"%\nO percentual de votos nulos é: ",perc_nulos,"%\nO percentual de votos válidos é:",perc_validos,"%")

#6. Faça um programa que leia o número do mês e apresente o nome do mês.

numero_mes = float(input("Digite o número: "))

if numero_mes == 1:
  print("O número é correspondente ao mês de Janeiro")

elif numero_mes == 2:
  print("O número é correspondente ao mês de Fevereiro")

elif numero_mes == 3:
  print("O número é correspondente ao mês de Março")

elif numero_mes == 4:
  print("O número é correspondente ao mês de Abril")

elif numero_mes == 5:
  print("O número é correspondente ao mês de Maio")

elif numero_mes == 6:
  print("O número é correspondente ao mês de Junho")

elif numero_mes == 7:
  print("O número é correspondente ao mês de Julho")

elif numero_mes == 8:
  print("O número é correspondente ao mês de Agosto")

elif numero_mes == 9:
  print("O número é correspondente ao mês de Setembro")

elif numero_mes == 10:
  print("O número é correspondente ao mês de Outubro")

elif numero_mes == 11:
  print("O número é correspondente ao mês de Novembro")

elif numero_mes == 12:
  print("O número é correspondente ao mês de Dezembro")

else:
  print("Número inválido digite um númedo de 1 à 12")

#7. Elabore um programa que leia um número e informe se ele é divisível por 10, por 5, por 2.

numero = float(input("Digite o número: "))

if numero % 10 == 0 and numero % 5 == 0 and numero % 2 == 0:
  print("Número é divisível por 10, 5 e 2")

else:
  print("Número não é divisível por 10, 5 e 2")

#8. Numa certa loja de eletrodomésticos, o comerciário encarregado da seção de televisores recebe mensalmente um salário fixo mais comissão. Essa comissão é calculada em relação a
#marca e ao número de televisores vendidos por mês, obedecendo à tabela abaixo:

salario_fixo = float(input("Digite o valor do salario fixo: "))
marca1 = int(input("Digite a quantidade de televisores vendidos da marca 1: "))
marca2 = int(input("Digite a quantidade de televisores vendidos da marca 2: "))
marca3 = int(input("Digite a quantidade de televisores vendidos da marca 3: "))

def calcular_comissao(marca, quantidade):
    if marca == 1:
        if quantidade >= 10:
            return quantidade * 50.00
        else:
            return quantidade * 5.00
    elif marca == 2:
        if quantidade >= 20:
            return quantidade * 20.00
        else:
            return quantidade * 2.00
    elif marca == 3:
        if quantidade >= 30:
            return quantidade * 30.00
        else:
            return quantidade * 3.00


comissao_marca1 = calcular_comissao(1, marca1)
comissao_marca2 = calcular_comissao(2, marca2)
comissao_marca3 = calcular_comissao(3, marca3)


comissao_total = comissao_marca1 + comissao_marca2 + comissao_marca3


salario_bruto = salario_fixo + comissao_total


desconto_inss = salario_bruto * 0.08


if salario_bruto >= 5000:
    imposto_renda = salario_bruto * 0.15
else:
    imposto_renda = 0.0


descontos_totais = desconto_inss + imposto_renda
salario_liquido = salario_bruto - descontos_totais


print(f"Salário Bruto (com comissão): R$ {salario_bruto:.2f}")
print(f"Comissão Total: R$ {comissao_total:.2f}")
print(f"Desconto INSS: R$ {desconto_inss:.2f}")
print(f"Desconto Imposto de Renda: R$ {imposto_renda:.2f}")
print(f"Salário Líquido: R$ {salario_liquido:.2f}")

#9.Um vendedor precisa de um algoritmo que calcule o preço total devido por um cliente. O programa deve receber o código de um
#produto e a quantidade comprada e calcular o preço total, usando a tabela abaixo. Mostre uma mensagem caso o código seja inválido.

codigo_produto = float(input("Digite o código do produto: "))
quantidade = float(input("Digite a quantidade do produto comprada: "))

if codigo_produto == 90:
  valor_total = quantidade * 5.30
  print("Valor total de: R$",valor_total)

elif codigo_produto == 91:
  valor_total = quantidade * 6.00
  print("Valor total de: R$",valor_total)

elif codigo_produto == 112:
  valor_total = quantidade * 3.20
  print("Valor total de: R$",valor_total)

elif codigo_produto == 321:
  valor_total = quantidade * 2.50
  print("Valor total de: R$",valor_total)

else:
  print("Produto inválido")

#10. Faça um programa que leia “três valores” (considere que não serão informados valores iguais),calcule e escreva a soma dos
#dois maiores.

num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número:"))
num3 = float(input("Digite o terceiro número:"))

if num1 < num2 and num1 < num3:
  soma_maiores = num2 + num3
  print("A soma dos 2 números maiores é: ",soma_maiores,)

elif num2 < num1 and num2 < num3:
  soma_maiores = num1 + num3
  print("A soma dos 2 números maiores é: ",soma_maiores,)

elif num3 < num1 and num3 < num2:
  soma_maiores = num2 + num1
  print("A soma dos 2 números maiores é: ",soma_maiores,)
  
  #11. Faça um programa que coloque três valores em ordem crescente

valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor 2: "))
valor3 = int(input("Digite o valor 3: "))

if valor1 < valor2 and valor1 < valor3:
    if valor2 < valor3:
        print(valor1, valor2, valor3)
    else:
        print(valor1, valor3, valor2)

elif valor2 < valor1 and valor2 < valor3:
    if valor1 < valor3:
        print(valor2, valor1, valor3)
    else:
        print(valor2, valor3, valor1)

else:
    if valor1 < valor2:
        print(valor3, valor1, valor2)
    else:
        print(valor3, valor2, valor1)

#12. A jornada de trabalho semanal de um funcionário é de 40 horas. O funcionário que trabalhar mais de 40 horas receberá hora extra, cujo cálculo é o valor da hora regular
#com um acréscimo de 50%. Escreva um programa que leia o número de horas trabalhadas em um mês, o salário por hora e escreva o salário total do funcionário, que deverá ser
#acrescido das horas extras, caso tenham sido trabalhadas (considere que o mês possua 4 semanas exatas).

horas_trabalhadas = int(input("Digite o número de horas trabalhadas: "))
salario_hora = float(input("Digite o valor da hora regular de trabalho: "))

if horas_trabalhadas > 160:
  salario_total = (salario_hora * 160) + ((horas_trabalhadas - 160) * (salario_hora*0.5))
  print("O salário total é de: R$",salario_total)

else:
  salario_total = (salario_hora*160)
  print("O salário total é de: R$",salario_total)

#13. Faça um programa que leia três valores (considere que não serão informados valores iguais) e apresente o maior deles.

valor1 = int(input("Digite o valor 1: "))
valor2 = int(input("Digite o valor 2: "))
valor3 = int(input("Digite o valor 3: "))

if valor1 > valor2 and valor1 > valor3:
  print("O maior número é",valor1)

elif valor2 > valor1 and valor2 > valor3:
  print("O maior número é",valor2)

elif valor3 > valor1 and valor3 > valor2:
  print("O maior número é",valor3)

#14. Elabore um programa que leia um número e, se ele for positivo, apresente a metade desse número, caso contrário apresente o número ao quadrado.

numero = int(input("Digite um número: "))

if numero > 0:
  resultado = numero/2
  print("O número é POSITIVO, e a metade dele é: ",resultado)

elif numero < 0:
  resultado = numero*numero
  print("O número é NEGATIVO, e ele ao quadrado é: ",resultado)

elif numero == 0:
  print("Digite um número diferente que zero que é um número neutro.")

#15. Numa loja de eletrodomésticos, as compras a vista têm um desconto de 5%,  ou  acréscimo  de  10%  para pagamentos em 2 vezes, ou ainda, acréscimo de 20% para pagamento em 3 vezes.
#Faça um programa que leia o valor da compra e a opção de pagamento, calcule e escreva o valor de cada parcela e o valor total a ser pago.

valor_compra = int(input("Digite o valor da compra: "))
pagamento = int(input("Digite se pagamento é em 1 (à vista), 2 ou 3 vezes: "))

if pagamento == 1:
  total = valor_compra - (valor_compra * 0.05)
  print("O valor total a ser pago é: R$",total)

elif pagamento == 2:
  total = valor_compra + (valor_compra * 0.10)
  valor_parcela = total / 2
  print("O valor total a ser pago é: R$",total,"A parcela será 2 vezes de: R$",valor_parcela)

elif pagamento == 3:
  total = valor_compra + (valor_compra * 0.20)
  valor_parcela = total / 3
  print("O valor total a ser pago é: R$",total,"A parcela será 3 vezes de: R$",valor_parcela)

#16. Faça um programa, que transforme minutos em horas.

minutos = int(input("Digite o número de minutos: "))

em_horas = minutos / 60

print("A quantidade de: ",minutos,"em horas é igual a",em_horas,"horas")

#17. O preço ao consumidor de um carro novo é a soma do preço de fábrica com o percentual de lucro do distribuidor e dos impostos aplicados ao preço de  fábrica.
#Faça um programa que leia o preço de fábrica de um veículo, o percentual de lucro do distribuidor e o percentual de impostos. Calcule e apresente:
#    a.  O valor correspondente ao lucro do distribuidor;
#    b.  O valor correspondente aos impostos;
#    c.  O preço final do veículo.

preco_fabrica = int(input("Digite o valor de preço de fabrica do veículo: "))
percentual_lucro = int(input("Digite o percentual de lucro: "))
percentual_impostos = int(input("Digite o percntual em impostos: "))

#    a.  O valor correspondente ao lucro do distribuidor;
lucro_distribuidor = preco_fabrica * (percentual_lucro/100)
#    b.  O valor correspondente aos impostos;
valor_impostos = preco_fabrica * (percentual_impostos/100)
#    c.  O preço final do veículo.
preco_final = preco_fabrica + lucro_distribuidor + valor_impostos

print("O preço de fábrica é: R$",preco_fabrica,"\nLucro do distribuidor: R$",lucro_distribuidor,"\nValor de impostos é: R$",valor_impostos,"\nE o preço final para o consumidor é: R$",preco_final)

#18. Faça um programa que calcule e mostre a área de um trapézio.
#       Área = (diagonal maior   *  diagonal menor) / 2

diagonal_maior = int(input("Digite o valor da diagonal maior: "))
diagonal_menor = int(input("Digite o valor da diagonal menor: "))

area_trapezio = (diagonal_maior * diagonal_menor) / 2

print("A área do trapézio é de",area_trapezio)

#19. Faça um algoritmo para ajudar a bilheteria do metrô. O operador deve informar o tipo do bilhete (1 - unitário, 2 - duplo ou 3 - 10 viagens) e a quantidade de bilhetes.
#O algoritmo deve calcular e mostrar o total a ser pago.

#Considere a seguinte tabela de preço:

#  Código do Bilhete    |    Valor do bilhete
#  1 – Unitário         |    R$ 2,90
#  2 – Duplo            |    R$ 5,60
#  3 – Dez viagens      |    R$ 27,00

tipo_bilhete = int(input("Digite o tipo de bilhete, 1 para unitário, 2 para duplo e 3 para para 10 viagens: "))
quant_bilhetes = int(input("Digite a quantidade de bilhetes: "))

if tipo_bilhete == 1:
  total = quant_bilhetes * 2.90
  print("O total a ser pago é: R$",total)

elif tipo_bilhete == 2:
  total = quant_bilhetes * 5.60
  print("O total a ser pago é: R$",total)

elif tipo_bilhete == 3:
  total = quant_bilhetes * 27.00
  print("O total a ser pago é: R$",total)

#20. Faça um programa que calcule e escreva a tabuada de um número qualquer.

numero = int(input("Digite o número em que deseja visualizar a tabuada: "))

n1 = numero * 1
n2 = numero * 2
n3 = numero * 3
n4 = numero * 4
n5 = numero * 5
n6 = numero * 6
n7 = numero * 7
n8 = numero * 8
n9 = numero * 9
n10 = numero * 10

print("A tabuada do número solicitado é:\n",numero,"x 1 = ",n1,"\n",numero,"x 2 = ",n2,"\n",numero,"x 3 = ",n3,"\n",numero,"x 4 = ",n4,"\n",numero,"x 5 = ",n5,"\n",numero,"x 6 = ",n6,"\n",numero,"x 7 = ",n7,"\n",numero,"x 8 = ",n8,"\n",numero,"x 9 = ",n9,"\n",numero,"x 10 =",n10)


# 2. Embora mais barato, o etanol é um combustível que é consumido mais rápido pelo motor flex em relação à gasolina. Para saber qual a melhor opção de combustível (Gasolina x Etanol),
# o motorista deve fazer uma conta simples, é preciso dividir o preço do litro do etanol pelo valor do litro da gasolina. Se o resultado da conta for maior que 0.7, vale a pena colocar
# gasolina, se for menor, o melhor é o consumidor abastecer com etanol. Faça um algoritmo para calcular e exibir qual o combustível mais vantajoso.

valor_etanol = float(input("Digite o valor do litro do etanol: "))
valor_gasolina = float(input("Digite o valor do litro do gasolina: "))

gasolina_vs_etanol = valor_etanol / valor_gasolina

if gasolina_vs_etanol > 0.7:
  print("Vale a pena colocar gasolina")

elif gasolina_vs_etanol < 0.7:
  print("Vale a pena colocar etanol")