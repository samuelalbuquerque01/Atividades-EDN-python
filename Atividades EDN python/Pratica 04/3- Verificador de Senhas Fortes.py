import re

while True:
    senha = input("Digite a senha (ou 'sair' para encerrar): ")
    if senha.lower() == "sair":
        break

    if len(senha) < 8:
        print("Senha fraca: menos de 8 caracteres.")
        continue

    if not re.search(r'\d', senha):
        print("Senha fraca: deve conter pelo menos um número.")
        continue

    print("Senha forte.")
    break
