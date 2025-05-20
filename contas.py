contas = []
AGENCIA = "0001"

def criar_conta(cpf):
    """Cria uma nova conta bancária e vincula a um usuário existente."""
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    
    if not usuario:
        print("Erro: Usuário não encontrado!")
        return None

    numero_conta = len(contas) + 1
    conta = {
        "agencia": AGENCIA,
        "numero_conta": numero_conta,
        "usuario": usuario
    }
    contas.append(conta)
    print("Conta criada com sucesso!")
    return conta

def listar_contas():
    """Lista todas as contas bancárias cadastradas."""
    for conta in contas:
        print(f"Agência: {conta['agencia']} - Conta: {conta['numero_conta']} - Titular: {conta['usuario']['nome']}")
