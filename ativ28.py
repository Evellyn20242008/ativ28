# Crie um programa que receba uma lista com o nome de 5 produtos e outra lista com as quantidades em estoque de cada um desses produtos. O programa deve exibir os produtos que estão com o estoque zerado.

# Exemplo de entrada:
# Produtos: ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
# Estoque: [10, 0, 5, 0, 20]

# Exemplo de saída:
# Produtos com estoque zerado: Feijão, Açúcar
produtos = ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
estoque = [10, 0, 5, 0, 20]

# Inicializa uma lista para produtos com estoque zerado
produtos_zerados = []

# Verifica quais produtos estão com estoque zerado
for i in range(len(produtos)):
    if estoque[i] == 0:
        produtos_zerados.append(produtos[i])

# Exibe os produtos com estoque zerado
if produtos_zerados:
    print("Produtos com estoque zerado:", ', '.join(produtos_zerados))
else:
    print("Nenhum produto está com estoque zerado.")
