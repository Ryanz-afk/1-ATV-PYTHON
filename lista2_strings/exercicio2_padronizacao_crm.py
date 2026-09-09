"""
Exercício 2: Padronização de Dados de CRM (Setor de Vendas)

Um vendedor cadastrou um cliente com os dados desorganizados no
sistema. Para evitar duplicidade e erros de envio:
1. Remover os espaços extras no início e fim das duas variáveis.
2. Deixar o nome apenas com as primeiras letras de cada palavra em
   maiúsculo (formato de nome próprio).
3. Deixar o e-mail todo em letras minúsculas.
"""

nome = " mArCoS aNtOnIo rOcHa "
email = " MARCOS.ROCHA@GMAIL.COM "

nome_padronizado = nome.strip().title()
email_padronizado = email.strip().lower()

print(f"Nome padronizado: {nome_padronizado}")
print(f"E-mail padronizado: {email_padronizado}")
