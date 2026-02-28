arquivo = open("arqText.tcxt", "w")

arquivo.write('Curso Python \n')
arquivo.write("Aula Prática")
arquivo.close()

leitura=open("arqText.tcxt", "r")
print(leitura.read())
leitura.close()