def lernotas():
    n=float(input("Digite uma nota para o aluno(a):"))
    return n


def resultado(n1,n2):

    if n1<0 or n1>10 or n2<0  or n2>10:
        print("Valor invalido")
        return

    media = (n1 + n2) / 2

    print("Nota 1: ", n1)
    print("Nota 2: ", n2)
    print("Média: ", media, ", Resultado: ", end="")
    if media >= 7:
        print("Aprovado")
    else:
        print("Aprovado")



a= lernotas()
b= lernotas()
resultado(a,b)

