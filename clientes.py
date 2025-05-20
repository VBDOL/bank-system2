usuarios = []

def criar_usuario(nome, data_nascimento, cpf, endereco):
    """Cria um novo usuário e adiciona à lista, garantindo que não haja CPFs duplicados."""
    cpf = "".join(filter(str.isdigit, cpf))  # Mantém apenas números no CPF
    
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Erro: CPF já cadastrado!")
        return None

    usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")
    return usuario

def listar_usuarios():
    """Lista todos os usuários cadastrados."""
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']} - CPF: {usuario['cpf']} - Endereço: {usuario['endereco']}")
