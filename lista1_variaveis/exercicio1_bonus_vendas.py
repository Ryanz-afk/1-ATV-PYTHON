"""
Exercício 1: Cálculo de Bônus de Vendas (RH/Vendas)

Uma empresa decidiu dar um bônus de 10% sobre o faturamento total
para a equipe de vendas. Calcule o valor do bônus e o faturamento
final da empresa após subtrair esse bônus.
"""

faturamento_inicial = 50000
percentual_bonus = 0.10

bonus = faturamento_inicial * percentual_bonus
faturamento_final = faturamento_inicial - bonus

print(f"Valor do bônus: R$ {bonus:.2f}")
print(f"Faturamento final: R$ {faturamento_final:.2f}")
