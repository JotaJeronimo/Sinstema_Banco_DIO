menu = """
..........BEM VINDO AO SEU BANCO..........

Escolha as opções abaixo;

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

"""

saldo = 0
limite = 500
numero_de_saque = 0
limite_de_saque = 3
Texto_Extrato = "EXTRATO"
Texto_Ivalido = "VALOR INVÁLIDO!"
Texto_Atencao = "ATENÇÃO!"

while True:
    opcao = input(menu)

    if opcao == "1":
        print("OPÇÃO 01 - DEPÓSITO".center(50, "."))
        valor = float(input("informe o valor que deseja depositar:__R$"))

        if valor > 0:
            saldo += valor 
            print(Texto_Extrato.center(50, "."))
            print(f"\nValor Depositato.....R${valor:.2f}")
            print(f"Saldo Atual..........R${saldo:.2f}") 
            print(".".center(50, "."))         
        else:
            print(Texto_Extrato.center(30, "."))
    elif opcao == "2":
        print("OPÇÃO 02 - SAQUE".center(50, "."))
        valor = float(input("Qual valor deseja sacar?"))

        saque_maior_saldo = valor > saldo
        saque_maior_limite = valor > limite
        saque_maior_que_num_permitido = numero_de_saque > limite_de_saque

        if  saque_maior_saldo:
            print(Texto_Atencao.center(50, "."))
            print("Você não tem saldo suficiente pra realizar essa operação!") 
        elif saque_maior_limite:
            print(Texto_Atencao.center(50, "."))
            print(f"Seu limite diario é de R${limite:.2f}, operação falhou!")
        elif saque_maior_que_num_permitido:
            print(Texto_Atencao.center(50, "."))
            print(f"Você pode realizar {limite_de_saque} saques, operação falhou!")
        elif valor > 0:
            saldo -= valor
            numero_de_saque += 1
            print(Texto_Extrato.center(50, "."))
            print(f"\nValor Sacado.......R${valor:.2f}")
            print(f"Saldo Atual..........R${saldo:.2f}") 
            print(".".center(50, "."))    
        else:
            print(Texto_Atencao.center(50, "."))
    elif opcao == "3":
        print(Texto_Extrato.center(50, "."))
        print(f"Saldo Atual..........R${saldo:.2f}") 
    elif opcao == "0":
         break
    else:
        print(Texto_Atencao.center(50, "."))
        print(Texto_Ivalido.center(50, "."))




        
    
    



