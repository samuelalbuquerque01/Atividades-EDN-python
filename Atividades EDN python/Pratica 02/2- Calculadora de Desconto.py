produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

valor_desconto = (percentual_desconto / 100) * preco_original
preco_final = preco_original - valor_desconto

print("Produto:", produto)
print("Preço Original: R$ {:.2f}".format(preco_original))
print("Desconto: {}% (R$ {:.2f})".format(percentual_desconto, valor_desconto))
print("Preço Final: R$ {:.2f}".format(preco_final))
