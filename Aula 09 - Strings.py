#Fatiamento
print("Fatiamento:")
fatiamento = "Curso em Video Python"
print(fatiamento[3]) #vai mostrar a str que está no indice 2 do texto fatiamento
print(fatiamento[:5]) #Vai mostrar todas as str do indice 0 até o indice desejado
print(fatiamento[5:12]) #Vai mostrar todas as str pertencentes ao intervalo desejado
print(fatiamento[::2]) #Vai mostrar as str pertencentes ao intervalo desejado pulando de 2 em 2.
print("Curso" in fatiamento) #True or False
print("\n\n")


# Para a criação de menus: utilize print(""" TEXTO GIGANTE """)
print("Utilizando texto grande:")
print ("""Bolchevique (russo: большевик;  francesa: "bolchevik";  inglesa: "bolshevik") 
é uma palavra da língua russa, e significa "maioritário".
Assim foram chamados os integrantes do Partido Operário Social-Democrata Russo liderada por Lenin. """)
print("\n\n")

#Outras Funçoes:
print ("Outras Funçoes:")
funcoes = "Aprendendo a Programar"
#len(obj) -  retorna a quantidade de indices do texto
print(len(funcoes))

#obj.count('') - retorna a quantidade de str indicadas existem destro do texto (Pode ser usada entre um intervalo utilizando ':')
print(funcoes.count('n'))

#obj.find('') - retorna a posição do primeiro str encontrado e retorna -1 se não encontrar.
print(funcoes.find('n'))

#obj.strip() - remove os espaços indesejados antes e depois do objeto [ tem as variaçoes: lstrip() e rstrip()
print(f"   {funcoes}    ".strip())

#obj.replace('','') - Troca a frase original por uma outra
print(funcoes.replace('Aprendendo', 'Ensinando'))
funcoes = funcoes.replace('Aprendendo','Ensinando')
print(funcoes)

#obj.split() - Cria uma lista de str utilizando como separador um objeto desejado
print(funcoes.split())
print(funcoes.split('a'))
print(funcoes.split()[0][0]) #Dentro da lista criada acha a posição.

#''.join(obj) - Pega uma lista e junta em uma unica str colocando um objeto entre as listas
print('_'.join(funcoes.split()))

