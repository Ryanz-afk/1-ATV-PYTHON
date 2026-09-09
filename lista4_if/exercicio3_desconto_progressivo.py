"""
Exercício 3: Cálculo de Desconto Progressivo (Setor de Vendas)

Um e-commerce aplica descontos automáticos no carrinho, de acordo
com faixas de valor da compra.
"""

valor_digitado = input("Digite o valor total da compra: R$ ")
valor_compra = float(valor_digitado.replace(",", "."))

if valor_compra >= 500:
    desconto = valor_compra * 0.15
elif valor_compra >= 200:
    desconto = valor_compra * 0.10
else:
    desconto = 0

valor_final = valor_compra - desconto

print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")
