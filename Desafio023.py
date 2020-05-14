print(f"{'*'*10}Desafio 023 - Separa um numero em algarismos{'*'*10}")
numero = input("Digite um numero entre 0 e 9999: ")
print(f"Unidade: {numero[3]}\nDezena: {numero[2]:>2}\nCentena: {numero[1]}\nMilhar: {numero[0]:>2}")
print('\n')
#Matematicamente:
numero = int(numero)
milhar = (numero//1000)*1000
centena = ((numero - milhar)//100)*100
dezena = ((((numero-milhar)-centena))//10)*10
unidade = ((numero - milhar)-centena)-dezena
print(f"Milhar: {milhar//1000}\nCentena: {centena//100}\nDezena: {dezena//10}\nUnidade: {unidade}")
