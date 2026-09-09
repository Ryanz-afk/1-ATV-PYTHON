"""
Exercício 4: Análise de Margem de Lucro (Financeiro)

Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos
foram de R$ 5.000,00 e o imposto sobre o faturamento é de 15%.
Calcule o imposto, o lucro líquido e a margem de lucro
(Lucro / Faturamento). No final, crie uma variável booleana chamada
meta_atingida que verifica se a margem de lucro é superior a 0.30
(30%).
"""

faturamento = 15000.00
custos_fixos = 5000.00
percentual_imposto = 0.15

imposto = faturamento * percentual_imposto
lucro_liquido = faturamento - custos_fixos - imposto
margem_lucro = lucro_liquido / faturamento
meta_atingida = margem_lucro > 0.30

print(f"Imposto: R$ {imposto:.2f}")
print(f"Lucro líquido: R$ {lucro_liquido:.2f}")
print(f"Margem de lucro: {margem_lucro:.2%}")
print(f"Meta atingida (>30%): {meta_atingida}")
