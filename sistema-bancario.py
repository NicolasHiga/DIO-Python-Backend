menu = """
++++++++++ MENU ++++++++++
|                        |
| [d] Depositar          |
| [s] Sacar              |
| [e] Extrato            |
| [q] Sair               |
|                        |
++++++++++++++++++++++++++
=> """

saldo = 0
limite = 500
extrato = ""
numeros_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depóstio: R${valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 's':
        valor = float(input("Informe o valor de saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numeros_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máxinmo de saques excedidos.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numeros_saques += 1
            
        else:
            print("Operação falhou! O valor informado é inválido.")
            
    elif opcao == "e":
        print(f"\n{'=' * 10} EXTRATO {'=' * 10}")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo:.2f}")
        print(f"{'=' * 29}")
        
    elif opcao == "q":
        print("\n\nSaindo...")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")