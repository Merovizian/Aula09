print(f"{'*'*10}Desafio 022 - Lendo Nomes{'*'*10}")
nome = input("Informe um nome: ")
print(f"{nome} com todas as letras maisculas: {nome.upper()}")
print(f"{nome} com todas as letras minusculas: {nome.lower()}")
print(f"{nome} possui {len(''.join(nome.split()))} letras")
print(f"{nome} tem como primeiro nome '{nome.split()[0]}' que possui {len(nome.split()[0])} letras")