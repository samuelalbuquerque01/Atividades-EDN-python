while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Escolha a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 == 0:
                print("Erro: divisão por zero.")
                continue
            resultado = num1 / num2
        else:
            print("Operação inválida.")
            continue

        print(f"Resultado: {resultado}")
        break
    except ValueError:
        print("Entrada inválida. Tente novamente.")
