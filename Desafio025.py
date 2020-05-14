print(f"{'*'*10}Desafio 025 - silva no nome{'*'*10}")
nome_alvo = input("Digite o nome da pessoa: ")
nome_busca = input("Digite o nome da busca: ")
print(f"Tem {nome_busca} no nome?",nome_busca.lower() in nome_alvo.lower() )