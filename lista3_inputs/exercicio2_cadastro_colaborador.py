"""
Exercício 2: Sistema de Cadastro de Colaborador (Setor de RH)

Ao cadastrar um novo funcionário, o RH precisa extrair o primeiro
nome para criar um crachá e padronizar o e-mail.
"""

nome_completo = input("Digite o nome completo do colaborador: ").strip()
email_pessoal = input("Digite o e-mail pessoal do colaborador: ")

posicao_espaco = nome_completo.find(" ")
primeiro_nome = nome_completo[:posicao_espaco].capitalize()

email_padronizado = email_pessoal.strip().lower()

print(f"Cadastro concluído: {primeiro_nome}. E-mail de acesso: {email_padronizado}")
