"""
Exercício 5: Personalização de E-mail de Marketing (Setor de Marketing)

O marketing quer enviar um e-mail de boas-vindas. Você deve extrair
apenas o primeiro nome para usar na saudação:
1. Encontrar a posição do primeiro espaço.
2. Fatiar o texto para pegar apenas o primeiro nome.
3. Formatar o nome com a primeira letra maiúscula.
4. Exibir a mensagem de boas-vindas.
"""

nome_completo = "lucas ferreira souza"

posicao_espaco = nome_completo.find(" ")
primeiro_nome = nome_completo[:posicao_espaco]
primeiro_nome = primeiro_nome.capitalize()

print(f"Olá, {primeiro_nome}, seja bem-vindo ao nosso clube!")
