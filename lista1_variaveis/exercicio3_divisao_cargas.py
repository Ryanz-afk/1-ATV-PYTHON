"""
Exercício 3: Divisão de Cargas (Logística/Transporte)

Uma transportadora precisa levar 1.250 caixas em caminhões pequenos.
Cada caminhão suporta exatamente 12 caixas. Quantos caminhões
sairão totalmente cheios? (Use //) e quantas caixas sobrarão para
serem enviadas em uma última viagem menor? (Use %).
"""

total_caixas = 1250
capacidade_caminhao = 12

caminhoes_cheios = total_caixas // capacidade_caminhao
caixas_restantes = total_caixas % capacidade_caminhao

print(f"Caminhões totalmente cheios: {caminhoes_cheios}")
print(f"Caixas restantes para a última viagem: {caixas_restantes}")
