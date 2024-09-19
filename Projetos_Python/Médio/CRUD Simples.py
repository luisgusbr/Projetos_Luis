usuarios = {}

def cadastrar_usuario(username, senha):
    if username in usuarios:
        return "Usuário já cadastrado!"
    usuarios[username] = senha
    return "Usuário cadastrado com sucesso."

def alterar_senha(username, senha):
    if username not in usuarios:
        return "Usuário não encontrado!"
    usuarios[username] = senha
    return "Senha alterada com sucesso."

def deletar_usuario(username):
    if username in usuarios:
        del usuarios[username]
        return "Usuário deletado com sucesso."
    return "Usuário não encontrado."

def listar_usuarios():
    if not usuarios:
        return "Nenhum usuário cadastrado."
    return "\n".join(usuarios.keys())

# Testando o sistema CRUD
print(cadastrar_usuario("usuario1", "senha123"))
print(cadastrar_usuario("usuario2", "senha456"))
print(alterar_senha("usuario1", "nova_senha"))
print(deletar_usuario("usuario2"))
print(listar_usuarios())
