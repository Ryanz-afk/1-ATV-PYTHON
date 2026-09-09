"""
Exercício 1: Calculadora de Imposto sobre Vendas (Setor Fiscal)

Uma empresa de serviços precisa calcular o imposto de 15% sobre o
valor bruto de uma nota fiscal. Como o valor muitas vezes vem
copiado de planilhas com "R$" e vírgula, o programa deve limpar o
texto, converter para float e calcular o imposto.

Exemplo de entrada: R$ 5.000,00
"""

valor_digitado = input("Digite o valor bruto da nota fiscal (Ex: R$ 5.000,00): ")

# Remove "R$", espaços, o ponto de milhar e troca a vírgula decimal por ponto
valor_limpo = valor_digitado.replace("R$", "").strip()
valor_limpo = valor_limpo.replace(".", "").replace(",", ".")
valor_bruto = float(valor_limpo)

imposto = valor_bruto * 0.15

print(f"O valor do imposto (15%) é: R$ {imposto:.2f}")
