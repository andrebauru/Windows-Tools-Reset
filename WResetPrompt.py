import subprocess
import tkinter as tk
from tkinter import simpledialog, messagebox

# Dicionário contendo as mensagens em ambos os idiomas
mensagens = {
    'pt': {
        'titulo': "Ferramentas de Administração do Sistema",
        'elevar_usuario': "Elevar Usuário a Administrador",
        'remover_usuario': "Remover Usuário",
        'resetar_sistema': "Resetar Sistema",
        'sair': "Sair",
        'digite_usuario': "Digite o nome do usuário para torná-lo administrador:",
        'sucesso_elevar': "Usuário elevado a administrador com sucesso!",
        'erro': "Erro",
        'falha_elevar': "Não foi possível elevar o usuário:",
        'digite_usuario_remover': "Digite o nome do usuário para removê-lo:",
        'usuario_removido': "Usuário removido com sucesso!",
        'falha_remover': "Não foi possível remover o usuário:",
        'confirmar_reset': "Você realmente deseja restaurar o sistema para configurações de fábrica?",
        'sistema_resetado': "Sistema sendo restaurado para configurações de fábrica.",
        'escolha_idioma': "Escolha o idioma: 1 para Português, 2 para Inglês"
    },
    'en': {
        'titulo': "System Administration Tools",
        'elevar_usuario': "Elevate User to Administrator",
        'remover_usuario': "Remove User",
        'resetar_sistema': "Reset System",
        'sair': "Exit",
        'digite_usuario': "Enter the username to make them an administrator:",
        'sucesso_elevar': "User successfully elevated to administrator!",
        'erro': "Error",
        'falha_elevar': "Failed to elevate user:",
        'digite_usuario_remover': "Enter the username to remove them:",
        'usuario_removido': "User successfully removed!",
        'falha_remover': "Failed to remove user:",
        'confirmar_reset': "Do you really want to reset the system to factory settings?",
        'sistema_resetado': "System is being reset to factory settings.",
        'escolha_idioma': "Choose language: 1 for Portuguese, 2 for English"
    }
}

def main():
    idioma = input(mensagens['pt']['escolha_idioma'])
    lang = 'pt' if idioma == '1' else 'en'
    
    msg = mensagens[lang]
    print(msg['titulo'])
    print(f"1. {msg['elevar_usuario']}\n2. {msg['remover_usuario']}\n3. {msg['resetar_sistema']}\n4. {msg['sair']}")
    
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        usuario = input(msg['digite_usuario'])
        try:
            subprocess.run(f"net localgroup administradores {usuario} /add", shell=True)
            print(msg['sucesso_elevar'])
        except Exception as e:
            print(f"{msg['erro']} {msg['falha_elevar']} {e}")
    elif opcao == "2":
        usuario = input(msg['digite_usuario_remover'])
        try:
            subprocess.run(f"net user {usuario} /delete", shell=True)
            print(msg['usuario_removido'])
        except Exception as e:
            print(f"{msg['erro']} {msg['falha_remover']} {e}")
    elif opcao == "3":
        resposta = input(msg['confirmar_reset'])
        if resposta.lower() in ['sim', 'yes']:
            subprocess.run("systemreset -cleanpc", shell=True)
            print(msg['sistema_resetado'])
    elif opcao == "4":
        return
    else:
        print("Opção inválida, tente novamente.")

if __name__ == "__main__":
    main()
