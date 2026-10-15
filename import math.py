import math

def calculadora_cientifica():
    print("=" * 50)
    print("     CALCULADORA CIENTÍFICA EM PYTHON")
    print("=" * 50)

    while True:
        print("\n--- OPERAÇÕES DISPONÍVEIS ---")
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("5. Potência (**)")
        print("6. Raiz quadrada (√)")
        print("7. Logaritmo (log)")
        print("8. Seno (sin)")
        print("9. Cosseno (cos)")
        print("10. Tangente (tan)")
        print("11. Fatorial (!)")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print("Encerrando calculadora...")
            break

        # Operações que precisam de 2 números
        if opcao in ["1", "2", "3", "4", "5"]:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("❌ Erro: Digite apenas números válidos!")
                continue

            if opcao == "1":
                resultado = num1 + num2
            elif opcao == "2":
                resultado = num1 - num2
            elif opcao == "3":
                resultado = num1 * num2
            elif opcao == "4":
                if num2 == 0:
                    print("❌ Erro: Divisão por zero!")
                    continue
                resultado = num1 / num2
            elif opcao == "5":
                resultado = num1 ** num2

            print(f"✅ Resultado: {resultado}")

        # Operações que precisam de 1 número
        elif opcao in ["6", "7", "8", "9", "10", "11"]:
            try:
                num = float(input("Digite o número: "))
            except ValueError:
                print("❌ Erro: Digite apenas números válidos!")
                continue

            if opcao == "6":
                if num < 0:
                    print("❌ Erro: Não existe raiz quadrada de número negativo (nos reais)!")
                    continue
                resultado = math.sqrt(num)
            elif opcao == "7":
                if num <= 0:
                    print("❌ Erro: Logaritmo só existe para números positivos!")
                    continue
                resultado = math.log10(num)  # log na base 10
            elif opcao == "8":
                resultado = math.sin(math.radians(num))  # converte para radianos
            elif opcao == "9":
                resultado = math.cos(math.radians(num))
            elif opcao == "10":
                resultado = math.tan(math.radians(num))
            elif opcao == "11":
                if num < 0 or num != int(num):
                    print("❌ Erro: Fatorial só existe para inteiros não negativos!")
                    continue
                resultado = math.factorial(int(num))

            print(f"✅ Resultado: {resultado}")
        else:
            print("❌ Opção inválida!")

# Executa a calculadora
calculadora_cientifica()
