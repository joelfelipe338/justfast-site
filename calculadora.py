def soma(a, b):
    return a + b


def subtracao(a, b):
    return a - b


def main():
    print("=== Calculadora ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("0 - Sair")

    while True:
        opcao = input("\nEscolha uma opção: ")

        if opcao == "0":
            print("Até logo!")
            break

        if opcao not in ("1", "2"):
            print("Opção inválida.")
            continue

        a = float(input("Primeiro número: "))
        b = float(input("Segundo número: "))

        if opcao == "1":
            print(f"Resultado: {soma(a, b)}")
        elif opcao == "2":
            print(f"Resultado: {subtracao(a, b)}")


if __name__ == "__main__":
    main()
