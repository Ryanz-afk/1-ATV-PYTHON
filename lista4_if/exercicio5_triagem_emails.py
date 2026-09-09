"""
Exercício 5: Sistema de Triagem de E-mails (Setor de Customer Experience)

Filtra para qual departamento uma reclamação deve ir, de acordo com
palavras-chave presentes no assunto do e-mail digitado.
"""

assunto = input("Digite o assunto do e-mail: ").lower()

if "pagamento" in assunto or "boleto" in assunto:
    print("Encaminhado para o Financeiro")
elif "entrega" in assunto or "atraso" in assunto:
    print("Encaminhado para a Logística")
else:
    print("Encaminhado para o Suporte Geral")
