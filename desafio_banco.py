Menu = """

    ############# BANCO AJB #############

     Por favor informa a opção desejada

                 [e] Extrato
                 [d] Depositar
                 [s] Sacar
                 [q] Sair

    #####################################              

> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True: 
    opcao = input(Menu)

    if opcao == "d":
        valor = float(input("informe um valor: "))
        
        if valor < 0:
            print("Valor inválido, tente novamente")
        else: 
            saldo += valor
            print("Depósito realizado com sucesso")
            extrato = f"Saldo: R$ {saldo:.2f}"
        
    elif opcao == "s":
        valor = float(input("informe um valor: "))

        excedeu_saldo = valor > saldo 

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"\nSaque: R$ {valor: .2f}\n"
            numero_saques += 1
        else:
            print("O valor informado é inválido") 

    elif opcao == "e":
        print("\n################ EXTRATO ################")
        print("NÃO FORAM REALIZADAS MOVIMENTAÇÕES." if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("#########################################")
   
    elif opcao == "q":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida. Tente novamente")