"""
Exercício 2: Controle de Estoque de E-commerce (Logística)

Um e-commerce começou o dia com 250 unidades de um smartphone no
estoque. Durante o dia, foram vendidas 78 unidades e chegaram mais
100 unidades de um fornecedor. Atualize a variável de estoque e
exiba o saldo final.
"""

estoque = 250
vendidas = 78
recebidas = 100

estoque = estoque - vendidas + recebidas

print(f"Saldo final do estoque: {estoque} unidades")
