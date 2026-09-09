"""
Exercício 2: Controle de Acesso ao Sistema (Setor de Segurança)

Verifica se o e-mail digitado pelo usuário está na lista de
administradores autorizados.
"""

admins = ["ana@empresa.com", "guilherme@empresa.com", "felipe@empresa.com"]

email_digitado = input("Digite seu e-mail: ")
email_padronizado = email_digitado.strip().lower()

if email_padronizado in admins:
    print("Acesso liberado! Bem-vindo ao painel de controle")
else:
    print("Acesso negado. Você não tem permissões de administrador")
