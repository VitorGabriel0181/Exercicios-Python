notaA =  float(input("Digite a primeira nota: "))
notaB = float(input("Digite a segunda nota: "))

#calcular media
mediafinal = (notaA + notaB) / 2

#verificação
if notaA < 0 or notaA > 10 or notaB < 0 or notaB > 10:
    print("Nota inválida")
else:
    if mediafinal >= 7:
        print("Média: %.1f - Aprovado" % mediafinal)
    else:
        print("Média: %.1f - Reprovado" % mediafinal)


