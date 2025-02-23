saldo=0
extrato=""
limite = 500
LIMITE_SAQUES = 3
total_saques= 0


while True:
    opcao=int(input("[1] Sacar\n[2] Depositar\n[3] Extrato\n[0] Sair\n=> "))
    if opcao==1:
        if total_saques>=LIMITE_SAQUES:
            print("Limite de saques diários atingido. Por favor, tente outro dia.")
            
        else:
            
            valor=float(input("Quanto deseja sacar: "))
            if 0>valor>=500:
                print("Valor inválido.")
            elif valor>saldo:
                print("Saldo insuficiente.")
            else:
            
                saldo -= valor
                total_saques+=1
                print(total_saques)
                extrato += f"Saque: Valor R$ {valor:.2f}\n"
                print("Saldo realizado com sucesso.")
    elif opcao==2:
        deposito=float(input("Quanto deseja depositar: "))
        if deposito>0:
            saldo+=deposito
            extrato += f"Depósito: Valor R$ {deposito:.2f}\n"
            print("Deposito realizado com sucesso.")
        else:
            print("Valor inválido. Tente novamente.")
    
        
    elif opcao==3:
        print("-------- EXTRATO --------" )
        print("Nenhuma movimentação realizada no momento" if not extrato else extrato)
        print(f"Saldo: R$ {saldo:.2f}")
    elif opcao==0:
        break
    else:
        print("Opção inválida. tente novamente.")

      

