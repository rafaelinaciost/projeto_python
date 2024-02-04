menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
 
=> """
 
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
 
    opcao = input(menu)
    
    if opcao == "d":
        valor = float(input("informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor :.2f}\n"

        else:
            print("operação falhou! o valor informado é inválido.")    

    elif opcao == "s":
        valor = float(input("informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite 

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("operação falhou! você não tem saldo sufuciente.")

        elif excedeu_limite:
            print("opção falhou! o valor do saque excede o limite!")    
        
        elif excedeu_saques:
            print("operação falhou! numeros de saques excedido.")

        elif valor > 0: 
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1 

    elif opcao == "e":
        print("\n========== EXTRATO ==========")    
        print("não foram realizadas movimentaÇões." if not extrato else extrato)  
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===============================")

    elif opcao == "q":
        break

    else:
        print("operação invalida, por favor selecione a operação desejada")































