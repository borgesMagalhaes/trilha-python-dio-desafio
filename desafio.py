def main():
    saldo = 0.0
    extrato = []  # lista para registrar cada operação: ("Depósito", valor) ou ("Saque", -valor)
    numero_saques = 0
    LIMITE_SAQUES = 3
    LIMITE_VALOR_SAQUE = 500.0

    while True:
        print("\n========== MENU ==========")
        print("1 - Depositar")
        print("2 - Sacar")
        print("3 - Extrato")
        print("4 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            # DEPÓSITO
            valor = float(input("Valor para depósito: R$ "))
            if valor > 0:
                saldo += valor
                extrato.append(("Depósito", valor))
                print(f"Depósito de R${valor:.2f} realizado com sucesso!")
            else:
                print("Erro: valor de depósito precisa ser positivo.")

        elif opcao == "2":
            # SAQUE
            if numero_saques >= LIMITE_SAQUES:
                print("Você já realizou o número máximo de saques!")
                continue

            valor = float(input("Valor para saque: R$ "))
            if valor <= 0:
                print("Erro: valor de saque precisa ser positivo.")
            elif valor > LIMITE_VALOR_SAQUE:
                print(f"Erro: o valor máximo para saque é R${LIMITE_VALOR_SAQUE:.2f}.")
            elif valor > saldo:
                print("Saldo insuficiente para realizar o saque.")
            else:
                saldo -= valor
                extrato.append(("Saque", -valor))
                numero_saques += 1
                print(f"Saque de R${valor:.2f} realizado com sucesso!")

        elif opcao == "3":
            # EXTRATO
            print("\n========== EXTRATO ==========")
            if not extrato:
                print("Não foram realizadas movimentações.")
            else:
                # Contando depósitos e saques
                quantidade_depositos = sum(1 for op, _ in extrato if op == "Depósito")
                quantidade_saques = sum(1 for op, _ in extrato if op == "Saque")

                # Mostrando cada operação
                for tipo_op, valor_op in extrato:
                    if tipo_op == "Depósito":
                        print(f"{tipo_op} de R${valor_op:.2f}")
                    else:  # tipo_op == "Saque"
                        # valor_op já é negativo, mas exibimos como positivo
                        print(f"{tipo_op} de R${-valor_op:.2f}")

                print("----------------------------")
                print(f"Total de depósitos: {quantidade_depositos}")
                print(f"Total de saques: {quantidade_saques}")

            print(f"Saldo atual: R${saldo:.2f}")

        elif opcao == "4":
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
