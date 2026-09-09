"""
Exercício 1: Validação de Investimento (Setor Financeiro)

Uma corretora de valores quer automatizar a recomendação básica de
perfil, de acordo com o valor que o usuário deseja investir.
"""

valor_digitado = input("Digite o valor que deseja investir: ")

# Trata o input caso o usuário digite "R$" ou use vírgula/ponto de milhar
valor_limpo = valor_digitado.replace("R$", "").strip()
valor_limpo = valor_limpo.replace(".", "").replace(",", ".")
valor = float(valor_limpo)

if valor < 1000:
    print("Perfil iniciante: Sugerimos Tesouro Direto")
elif valor <= 5000:
    print("Perfil moderado: Sugerimos Fundos Imobiliários")
else:
    print("Perfil arrojado: Sugerimos Ações")
