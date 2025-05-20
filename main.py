from operacoes_bancarias import saque, deposito, exibir_extrato
from clientes import criar_usuario, listar_usuarios
from contas import criar_conta, listar_contas

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar usuário
[l] Listar usuários
[n] Criar conta
[m] Listar contas
[q] Sair

=> """

saldo = 0
limite = 500
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).lower()

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "c":
        nome = input("Nome: ")
        data_nascimento = input("Data de nascimento: ")
        cpf = input("CPF: ")
        endereco = input("Endereço (Logradouro, número - bairro - cidade/estado): ")
        criar_usuario(nome, data_nascimento, cpf, endereco)

    elif opcao == "l":
        listar_usuarios()

    elif opcao == "n":
        cpf = input("Informe o CPF do titular: ")
        criar_conta(cpf)

    elif opcao == "m":
        listar_contas()

    elif opcao == "q":
        print("Saindo... Obrigado por utilizar nosso sistema bancário!")
        break

    else:
        print("Operação inválida, tente novamente.")
