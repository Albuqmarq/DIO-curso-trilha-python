from datetime import date, datetime
dia=date.today().strftime("%d/%m/%Y")


def sacar(valor,saldo,extrato,limite_atual,limite):
   
    if 0>valor>limite:
        print("Valor inválido.")
    elif valor>saldo:
        print("Saldo insuficiente.")
    else:  
        saldo -= valor
                    
        extrato += f"Saque: Valor R$ {valor:.2f} (data: {dia})\n"
        limite_atual+=1
        print("Saldo realizado com sucesso.") 
    return saldo,extrato,limite_atual

def depositar(saldo,deposito,extrato,limite_atual,/):
    if deposito>0:
        saldo+=deposito
        extrato += f"Depósito: Valor R$ {deposito:.2f} (data: {dia})\n"
        limite_atual+=1
        print("Deposito realizado com sucesso.")
    else:
        print("Valor inválido. Tente novamente.")
    return saldo,extrato,limite_atual

def exibir_extrato(saldo,/,*,extrato):
    print("-------- EXTRATO --------" )
    print("Nenhuma movimentação realizada no momento" if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
   
def criar_usuario(usuarios):
    cpf = input("Digite seu CPF: ")
    usuario = filtra_usuario(cpf, usuarios) 
    if usuario:
        print("CPF já cadastrado. Por favor, tente novamente.")
        return

    nome = input("Digite seu nome: ")
    nascimento = input("Digite sua data de nascimento: ")
    
    print("Digite seu endereço: ")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")
    
    endereco = f"{logradouro} - {numero} - {bairro} - {cidade}/{estado}"
    
    usuarios.append({
        "nome": nome,
        "nascimento": nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("Usuário cadastrado com sucesso!")


def filtra_usuario(cpf,usuarios):
    usuarios_filtrados=[usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia,num_contas,usuarios):
    cpf=input("Digite seu CPF: ")
    usuario=filtra_usuario(cpf,usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia,"numero_conta": num_contas,"usuario": usuario}
    print("Usuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta['agencia']}\nC/C: {conta['numero_conta']}\nTitular: {conta['usuario']['nome']}")
        print("-"*50)

def main():
    saldo=0
    extrato=""
    limite = 500
    LIMITE_TRANSACAO=10
    LIMITE_ATUAL=0
    AGENCIA="0001"
    usuarios=[]
    contas=[]
    numero_contas=1

    while True:
        print("======== MENU ========")
        opcao=int(input("[1] Sacar\n[2] Depositar\n[3] Extrato\n[4] Criar usuário\n[5] Criar conta\n[6] Listar contas\n[0] Sair\n=> "))
        print()
    
        if LIMITE_ATUAL<LIMITE_TRANSACAO:
            if opcao==1:   
                valor=float(input("Quanto deseja sacar: "))           
                saldo,extrato,LIMITE_ATUAL=sacar(saldo=saldo,valor=valor,extrato=extrato,limite_atual=LIMITE_ATUAL,limite=limite)

            elif opcao==2:
                deposito=float(input("Quanto deseja depositar: "))
                saldo,extrato,LIMITE_ATUAL=depositar(saldo,deposito,extrato,LIMITE_ATUAL)
                      
            elif opcao==3:
                exibir_extrato(saldo,extrato=extrato)
            
            elif opcao==4:
                criar_usuario(usuarios)
                
            elif opcao==5:
                conta= criar_conta(AGENCIA,numero_contas,usuarios)
                if conta:
                    contas.append(conta)
                    numero_contas+=1
            elif opcao==6:
                listar_contas(contas)

            elif opcao==0:
                break
            else:
                print("Opção inválida. tente novamente.")
            
        else:
            print("Limite diário atingido.")
            break

main()
      