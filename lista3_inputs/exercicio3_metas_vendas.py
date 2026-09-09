"""
Exercício 3: Análise de Metas de Vendas (Setor Comercial)

Um gerente quer comparar o desempenho de duas filiais. O programa
pede o faturamento de cada loja, calcula o total e a média, e exibe
tudo formatado com separador de milhar e duas casas decimais.
"""

faturamento_a = float(input("Digite o faturamento da Loja A: ").replace(",", "."))
faturamento_b = float(input("Digite o faturamento da Loja B: ").replace(",", "."))

total = faturamento_a + faturamento_b
media = total / 2

print(f"Faturamento total: R$ {total:,.2f} | Média entre as lojas: R$ {media:,.2f}")
