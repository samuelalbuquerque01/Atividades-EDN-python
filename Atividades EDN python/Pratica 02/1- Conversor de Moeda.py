valor_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_dolar = valor_reais / taxa_dolar
valor_euro = valor_reais / taxa_euro

print("Valor em Reais: R$ {:.2f}".format(valor_reais))
print("Convertido para Dólares: US$ {:.2f}".format(valor_dolar))
print("Convertido para Euros: € {:.2f}".format(valor_euro))
