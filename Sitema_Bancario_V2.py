
def menu():
    menu = """
..........BEM VINDO AO SEU BANCO..........

Escolha uma das as opções abaixo;

[1] 💸 Depositar
[2] 💰 Sacar
[3] 🧾 Extrato
[4] 👤 Criar Novo Usuário
[5] 📑 Criar Nova Conta
[6] 🏸 Consultar Usuários
[0] ❌ Sair

...........ESCOLHA UMA DAS OPÇÕES..........

"""
    return input(menu)
 
def criar_novo_usuario(dados_user):
    apenas_numeros = "Use apenas numeros, sem (.)❗"
    Texto_Atencao = "ATENÇÃO!"
    print(apenas_numeros.center(50, "."))
    cpf_usuario = int(input("Informe o CPF para iniciara operação \n"))
    
    validar_user_cpf = validar_cpf(cpf_usuario, dados_user)
    
    if validar_user_cpf:
       print(Texto_Atencao.center(50, "."))
       print(".........Numero de CPF já cadastrado.........")
       print("\n⛔.........Operação cancelada!.........⛔")
       return
       
    nome_usuario = str(input("Informe o nome do usurio: \n"))
    endereço_usuario = str(input("Informe o endereço do usurio: \n"))
    data_nacimento_usuario = str(input("Informe o data de nascimento do usurio (dd/mm/aaaa): \n"))

    dados_user.append({"CPF": cpf_usuario,"nome": nome_usuario, "endereço": endereço_usuario, "Data_nacimento": data_nacimento_usuario})
    print("✅Usuario, cadastrado com sucesso")

def validar_cpf(cpf_usuario, dados_user):
    validar_cpf = [validar_user_cpf for validar_user_cpf in dados_user if validar_user_cpf ["CPF"] == cpf_usuario]
    return validar_cpf[0] if validar_cpf else None

def criar_conta(contas_cadastradas, gerador_contas, dados_user):
    apenas_numeros = "Use apenas numeros, sem (.)❗"
    Texto_Atencao = "ATENÇÃO!"
    print(apenas_numeros.center(50, "."))
    cpf_usuario = int(input("Informe o CPF para iniciara operação \n"))

    validar_user_cpf = validar_cpf(cpf_usuario, dados_user)
       

    if validar_user_cpf:
       contas_cadastradas.append({"Agencia": "0001", "Conta": gerador_contas, "CPF": cpf_usuario})
       print("✅ Conta, cadastrado com sucesso")

       return
    else:
       Texto_Atencao = "ATENÇÃO"
       print(Texto_Atencao.center(50, "."))
       print("\n.............Usuário não encontrado............")
       print("\n.........Por favor, cadastre o usuario!........")
       print("\n⛔............Operação cancelada!...........⛔")
       return contas_cadastradas
   
def consultar_dados(contas_cadastradas):
           
           cabecario = "RELATORIO GERAL"

           print(cabecario.center(50, "."))
           for linha in contas_cadastradas:               
                print("Agencia:", linha["Agencia"])
                print("Conta:", linha["Conta"])
                print("CPF:", linha["CPF"])                                                   
                print("-" * 50)
                
def deposito(saldo, valor):
    Texto_Extrato = "EXTRATO"
    if valor > 0:
        saldo += valor 
        print(Texto_Extrato.center(50, "."))
        print(f"\nValor Depositato.....R${valor:.2f}")
        print(f"Saldo Atual..........R${saldo:.2f}") 
        print(".".center(50, "."))         
    else:
        print(Texto_Extrato.center(30, "."))
    return saldo, valor

def saque(saldo, valor, limite, numero_de_saque, limite_de_saque):
    Texto_Atencao = "ATENÇÃO!"
    Texto_Extrato = "EXTRATO"
    print("OPÇÃO 02 - SAQUE".center(50, "."))
    valor = float(input("Qual valor deseja sacar?"))

    saque_maior_saldo = valor > saldo
    saque_maior_limite = valor > limite
    saque_maior_que_num_permitido = numero_de_saque > limite_de_saque

    if  saque_maior_saldo:
        print(Texto_Atencao.center(50, "."))
        print("⛔Você não tem saldo suficiente pra realizar essa operação!⛔") 
    elif saque_maior_limite:
        print(Texto_Atencao.center(50, "."))
        print(f"Seu limite diario é de R${limite:.2f}, ⛔...operação falhou!⛔...")
    elif saque_maior_que_num_permitido:
        print(Texto_Atencao.center(50, "."))
        print(f"Você pode realizar {limite_de_saque} saques, ⛔...operação falhou!⛔...")
    elif valor > 0:
        saldo -= valor
        
        print(Texto_Extrato.center(50, "."))
        print(f"\nValor Sacado...........R${valor:.2f}")
        print(f"Saldo Atual..........R${saldo:.2f}") 
        print(".".center(50, "."))    
    else:
        print(Texto_Atencao.center(50, "."))
    return saldo, valor

def extrato(saldo):
    Texto_Extrato = "EXTRATO"    
    print(Texto_Extrato.center(50, "."))
    print(f"Saldo Atual..........R${saldo:.2f}")

def op_invalida():
    Texto_Ivalido = "⛔VALOR INVÁLIDO!⛔"
    Texto_Atencao = "ATENÇÃO!"
    print(Texto_Atencao.center(50, "."))
    print(Texto_Ivalido.center(50, "."))

def main():
    saldo = 0
    valor = 0
    limite = 500
    numero_de_saque = 0
    limite_de_saque = 3
    gerador_contas = 1000
    dados_user = []
    contas_cadastradas = []
 
    while True:
        opcao = menu()
            
        if opcao == "1":
            print("OPÇÃO 01 - DEPÓSITO".center(50, "."))
            valor = float(input("informe o valor que deseja depositar:__R$"))
            
            saldo, valor = deposito(saldo, valor) 
            
        elif opcao == "2":
            numero_de_saque += 1        
            saldo, valor = saque(saldo, valor, limite, numero_de_saque, limite_de_saque)
        elif opcao == "3":
            extrato(saldo) 
        elif opcao == "4":
            criar_novo_usuario(dados_user)
        elif opcao == "5":
            gerador_contas += 1
            criar_conta(contas_cadastradas, gerador_contas, dados_user)
            contas_cadastradas = contas_cadastradas
        elif opcao == "6":
            consultar_dados(contas_cadastradas)
        elif opcao == "0":
         break
        else:
            op_invalida()

main()



        
   