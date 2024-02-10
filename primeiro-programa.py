usuarios = []
contas_correntes = []
numero_conta_sequencial = 1
conta_corrente = None  # Variável  para a conta corrente do usuário atual

def saque(*, saldo, valor, extrato, limite, num_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = num_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        num_saques += 1
        print("Saque efetuado com sucesso.")  # Mensagem de sucesso adicionada

    return saldo, extrato

def depositar(conta):
    if conta:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            conta["saldo"] += valor
            conta["extrato"] += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso.")
        else:
            print("Operação falhou! O valor informado é inválido.")
    else:
        print("Erro: Você precisa criar uma conta antes de realizar um depósito.")

def extrato(conta):
    print("\n========== EXTRATO ==========")
    print("Não foram realizadas movimentações." if not conta["extrato"] else conta["extrato"])
    print(f"\nSaldo: R$ {conta['saldo']:.2f}")
    print("===============================")

def cadastrar_usuario():
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento do usuário (DD/MM/AAAA): ")
    cpf = input("Informe o CPF do usuário: ")
    endereco = input("Informe o endereço do usuário (logradouro - bairro - cidade/estado): ")

    # Armazenar apenas os números do CPF
    cpf_numeros = ''.join(filter(str.isdigit, cpf))

    # Verificar se já existe um usuário com o mesmo CPF
    if any(usuario['cpf'] == cpf_numeros for usuario in usuarios):
        print("Erro: Já existe um usuário com esse CPF.")
        return None

    usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf_numeros, "endereco": endereco}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso.")
    return usuario

def criar_conta_corrente(usuario):
    global numero_conta_sequencial, conta_corrente

    conta_corrente = {"agencia": "0001", "numero_conta": numero_conta_sequencial, "usuario": usuario, "saldo": 0, "limite": 1000, "extrato": "", "num_saques": 0}
    contas_correntes.append(conta_corrente)

    # Incrementar o número da conta sequencial para a próxima criação
    numero_conta_sequencial += 1

    print(f"Conta corrente criada com sucesso. Número da conta: {conta_corrente['numero_conta']}")
    return conta_corrente

def listar_contas():
    print("\n========== LISTA DE CONTAS ==========")
    for conta in contas_correntes:
        print(f"Número da Conta: {conta['numero_conta']}, Saldo: R$ {conta['saldo']:.2f}")
    print("=====================================")

menu = """
[n] Nova Conta
[l] Listar Contas
[u] Novo Usuário
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

while True:
    opcao = input(menu)

    if opcao == "n":
        novo_usuario = cadastrar_usuario()
        if novo_usuario:
            conta_corrente = criar_conta_corrente(novo_usuario)

    elif opcao == "l":
        listar_contas()

    elif opcao == "u":
        novo_usuario = cadastrar_usuario()

    elif opcao == "d":
        depositar(conta_corrente)

    elif opcao == "s":
        if conta_corrente:
            saldo, extrato_conta = saque(saldo=conta_corrente['saldo'], valor = float(input("informe o valor do saque: ")),extrato=conta_corrente['extrato'], limite=conta_corrente['limite'], num_saques=conta_corrente['num_saques'], limite_saques=3)
            conta_corrente['saldo'] = saldo
            conta_corrente['extrato'] = extrato_conta
           
            
        else:
         print("Erro: Você precisa criar uma conta antes de sacar.")

    elif opcao == "e":
        extrato(conta_corrente)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor, selecione a operação desejada.")








