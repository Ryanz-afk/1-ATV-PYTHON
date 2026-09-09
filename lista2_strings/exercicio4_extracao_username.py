"""
Exercício 4: Extração de Username para Log (Setor de Segurança)

Para criar um log de acessos, o sistema precisa extrair apenas a
parte do nome do usuário de um e-mail corporativo (tudo o que vem
antes do @). Use a função .find() e o fatiamento de texto para
extrair e exibir apenas o nome.
"""

email = "beatriz.oliveira@grupocorp.com"

posicao_arroba = email.find("@")
username = email[:posicao_arroba]

print(f"Username extraído: {username}")
