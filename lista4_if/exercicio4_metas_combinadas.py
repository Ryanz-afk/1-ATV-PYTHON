"""
Exercício 4: Análise de Metas Combinadas (Setor Comercial)

Uma empresa paga bônus se a meta individual do vendedor e a meta da
loja forem batidas ao mesmo tempo.
"""

vendas_vendedor = float(input("Digite as vendas do vendedor: R$ ").replace(",", "."))
meta_vendedor = float(input("Digite a meta individual do vendedor: R$ ").replace(",", "."))
vendas_loja = float(input("Digite as vendas totais da loja: R$ ").replace(",", "."))
meta_loja = float(input("Digite a meta da loja: R$ ").replace(",", "."))

if vendas_vendedor >= meta_vendedor and vendas_loja >= meta_loja:
    bonus = vendas_vendedor * 0.20
else:
    bonus = 0

print(f"Seu bônus este mês é de: R$ {bonus:.2f}")
