arquivo = open("/convidado/python_class/arquivo.txt", "w")

arquivo.write("Helllo!")

arquivo.close()

arquivo = open("/convidado/python_class/arquivo.txt")

linha_do_arquivo = arquivo.readline()

print(linha_do_arquivo)

arquivo.close()
