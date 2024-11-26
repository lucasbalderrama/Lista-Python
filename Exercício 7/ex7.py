#Gabriel Reis de Brito, Kauâ de Albuquerque Almeida e Lucas Randal Abreu Balderrama
def cadastra_produto(nome, preco, quant):
    return{
        "nome": nome,
        "preco": preco,
        "quantidade": quant
    }

produtos = []

for i in range(5):
    nome = input(f"\nInsira o nome do produto {i+1}: ")
    preco = float(input(f"Insira o preço do produto {i+1}: "))
    quant = int(input(f"Insira a quantidade do produto {i+1}: "))

    produto = cadastra_produto(nome, preco, quant)
    produtos.append(produto)

    if i < 4:
        continuar = int(input('\nDigite 1 para continuar adicionando produtos. Digite 0 para encerrar: '))

    if continuar == 0:
        break

print("\nProdutos:")
for produto in produtos:
    print(f"-> Nome: {produto['nome']}; Preço: {produto['preco']}; Quantidade: {produto['quantidade']}")
