qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor:"))

while valor > 0:
    soma = soma + valor
    qtd = qtd + 1
    #entrada de valores
    valor = float(input("Digite um valor:"))

#caso digite um valor negativo o laço encerra
media = soma / qtd
print(" total de soma: ", soma)
print(" quantidade de valores digitados:", qtd)
print(" média dos valores:", media)
print("Fim do programa")
