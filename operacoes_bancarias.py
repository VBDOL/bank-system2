def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Função de saque que recebe argumentos apenas por nome (keyword-only)."""
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("Operação falhou! Valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato.append(f"Saque: R$ {valor:.2f}")
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! Valor inválido.")

    return saldo, extrato

def deposito(saldo, valor, extrato, /):
    """Função de depósito que recebe argumentos apenas por posição (positional-only)."""
    if valor > 0:
        saldo += valor
        extrato.append(f"Depósito: R$ {valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! Valor inválido.")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    """Função de extrato que recebe saldo como posicional e extrato como keyword-only."""
    print("\n================ EXTRATO ================")
    if extrato:
        for operacao in extrato:
            print(operacao)
    else:
        print("Nenhuma movimentação registrada.")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")
