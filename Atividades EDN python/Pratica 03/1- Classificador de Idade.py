idade = int(input("Digite sua idade: "))

if idade >= 0 and idade <= 12:
    classificacao = "Criança"
elif idade <= 17:
    classificacao = "Adolescente"
elif idade <= 59:
    classificacao = "Adulto"
else:
    classificacao = "Idoso"

print(f"Você tem {idade} anos e é classificado como: {classificacao}")
