from datetime import date, datetime

saldo=0
extrato=""
limite = 500
LIMITE_TRANSACAO=10
LIMITE_ATUAL=0

dia=date.today().strftime("%d/%m/%Y")



while True:
    
    opcao=int(input("[1] Sacar\n[2] Depositar\n[3] Extrato\n[0] Sair\n=> "))
   
    if LIMITE_ATUAL<LIMITE_TRANSACAO:
        if opcao==1:              
            valor=float(input("Quanto deseja sacar: "))
            if 0>valor>=500:
                print("Valor inválido.")
            elif valor>saldo:
                print("Saldo insuficiente.")
            else:  
                saldo -= valor
                
                extrato += f"Saque: Valor R$ {valor:.2f} (data: {dia})\n"
                LIMITE_ATUAL+=1
                print("Saldo realizado com sucesso.")

        elif opcao==2:
            deposito=float(input("Quanto deseja depositar: "))
            if deposito>0:
                saldo+=deposito
                extrato += f"Depósito: Valor R$ {deposito:.2f} (data: {dia})\n"
                LIMITE_ATUAL+=1
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
        
    else:
        print("Limite diário atingido.")
        break
      

      

