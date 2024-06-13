from produto import Produto, Eletronico, Roupa, Alimento
from cliente import Cliente
from venda import Venda

# Crie alguns produtos
produto1 = Eletronico("TV", 1, 1000.0, 5, "Samsung")
produto2 = Roupa("Camisa", 2, 50.0, 10, "M")
produto3 = Alimento("Arroz", 3, 20.0, 20, "2023-02-28")

# Crie um cliente
cliente = Cliente("José", 1)

# Crie uma venda
venda = Venda("2023-01-10", [produto1, produto2, produto3], 1070.0)

# Adicione a venda ao cliente
cliente.add_compra(venda)

# Mostrar tudo!
print(f"Produtos:")
print(f"Nome: {produto1.get_nome()}")
print(f"Código: {produto1.get_codigo()}")
print(f"Preço: {produto1.get_preco()}")
print(f"Quantidade: {produto1.get_quantidade()}")
print(f"Marca: {produto1.get_marca()}")
print()

print(f"Nome: {produto2.get_nome()}")
print(f"Código: {produto2.get_codigo()}")
print(f"Preço: {produto2.get_preco()}")
print(f"Quantidade: {produto2.get_quantidade()}")
print(f"Tamanho: {produto2.get_tamanho()}")
print()

print(f"Nome: {produto3.get_nome()}")
print(f"Código: {produto3.get_codigo()}")
print(f"Preço: {produto3.get_preco()}")
print(f"Quantidade: {produto3.get_quantidade()}")
print(f"Data de validade: {produto3.get_data_validade()}")
print()

print(f"Cliente:")
print(f"Nome: {cliente.get_nome()}")
print(f"ID: {cliente.get_id()}")
print(f"Histórico de compras:")
for venda in cliente.get_historico_compras():
    print(f"Data: {venda.get_data()}")
    print(f"Itens vendidos:")
    for item in venda.get_itens_vendidos():
        print(f"Nome: {item.get_nome()}")
        print(f"Código: {item.get_codigo()}")
        print(f"Preço: {item.get_preco()}")
        print(f"Quantidade: {item.get_quantidade()}")
    print(f"Valor total: {venda.get_valor_total()}")
