print(f"{'*'*10}Desafio 027 - Ultimo e primeiro nome{'*'*10}")
nome = input("Digite um nome: ")
print(f"Primeiro nome: {nome.split()[0]}")
print(f"Último nome: {nome.split()[len(nome.split())-1]}")