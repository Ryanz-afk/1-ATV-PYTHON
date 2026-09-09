"""
Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos)

Um contrato de manutenção de software tem a duração de 40 meses.
O cliente quer ver esse tempo no formato: "X anos e Y meses".
Utilize os operadores de divisão inteira e resto da divisão para
converter os 40 meses.
"""

meses_totais = 40

anos = meses_totais // 12
meses_restantes = meses_totais % 12

print(f"Duração do contrato: {anos} anos e {meses_restantes} meses")
