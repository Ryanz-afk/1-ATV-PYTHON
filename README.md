# Lista Extra 01 – Paradigmas de Programação com Python

Soluções comentadas para os exercícios de variáveis, strings, inputs e estruturas condicionais (`if`).

## Índice

- [Lista 1: Exercícios de variáveis](#lista-1-exercícios-de-variáveis)
- [Lista 2: Exercícios de strings](#lista-2-exercícios-de-strings)
- [Lista 3: Exercícios de inputs](#lista-3-exercícios-de-inputs)
- [Lista 4: Exercícios com if](#lista-4-exercícios-com-if)

---

## Lista 1: Exercícios de variáveis

### Exercício 1 — Cálculo de Bônus de Vendas (RH/Vendas)

```python
faturamento_inicial = 50000
percentual_bonus = 0.10

bonus = faturamento_inicial * percentual_bonus
faturamento_final = faturamento_inicial - bonus

print(f"Valor do bônus: R$ {bonus:.2f}")
print(f"Faturamento final: R$ {faturamento_final:.2f}")
```

**Saída:**
```
Valor do bônus: R$ 5000.00
Faturamento final: R$ 45000.00
```

---

### Exercício 2 — Controle de Estoque de E-commerce (Logística)

```python
estoque = 250
vendidas = 78
recebidas = 100

estoque = estoque - vendidas + recebidas

print(f"Saldo final do estoque: {estoque} unidades")
```

**Saída:**
```
Saldo final do estoque: 272 unidades
```

---

### Exercício 3 — Divisão de Cargas (Logística/Transporte)

```python
total_caixas = 1250
capacidade_caminhao = 12

caminhoes_cheios = total_caixas // capacidade_caminhao
caixas_restantes = total_caixas % capacidade_caminhao

print(f"Caminhões totalmente cheios: {caminhoes_cheios}")
print(f"Caixas restantes para a última viagem: {caixas_restantes}")
```

**Saída:**
```
Caminhões totalmente cheios: 104
Caixas restantes para a última viagem: 2
```

---

### Exercício 4 — Análise de Margem de Lucro (Financeiro)

```python
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
```

**Saída:**
```
Imposto: R$ 2250.00
Lucro líquido: R$ 7750.00
Margem de lucro: 51.67%
Meta atingida (>30%): True
```

---

### Exercício 5 — Conversão de Tempo de Contrato (Gestão de Projetos)

```python
meses_totais = 40

anos = meses_totais // 12
meses_restantes = meses_totais % 12

print(f"Duração do contrato: {anos} anos e {meses_restantes} meses")
```

**Saída:**
```
Duração do contrato: 3 anos e 4 meses
```

---

## Lista 2: Exercícios de strings

### Exercício 1 — Relatório de Margem de Lucro (Setor Financeiro)

```python
faturamento = 45000.00
custo = 23500.00

lucro = faturamento - custo
margem_lucro = lucro / faturamento

print(f"Lucro: R$ {lucro:,.2f}")
print(f"Margem de lucro: {margem_lucro:.0%}")
```

**Saída:**
```
Lucro: R$ 21,500.00
Margem de lucro: 48%
```

---

### Exercício 2 — Padronização de Dados de CRM (Setor de Vendas)

```python
nome = " mArCoS aNtOnIo rOcHa "
email = " MARCOS.ROCHA@GMAIL.COM "

nome_padronizado = nome.strip().title()
email_padronizado = email.strip().lower()

print(f"Nome padronizado: {nome_padronizado}")
print(f"E-mail padronizado: {email_padronizado}")
```

**Saída:**
```
Nome padronizado: Marcos Antonio Rocha
E-mail padronizado: marcos.rocha@gmail.com
```

---

### Exercício 3 — Migração de Servidor de E-mail (Setor de TI)

```python
email_antigo = "andre_silva@empresa.com.br"

email_novo = email_antigo.replace("@empresa.com.br", "@grupocorp.com")

print(f"Novo e-mail: {email_novo}")
```

**Saída:**
```
Novo e-mail: andre_silva@grupocorp.com
```

---

### Exercício 4 — Extração de Username para Log (Setor de Segurança)

```python
email = "beatriz.oliveira@grupocorp.com"

posicao_arroba = email.find("@")
username = email[:posicao_arroba]

print(f"Username extraído: {username}")
```

**Saída:**
```
Username extraído: beatriz.oliveira
```

---

### Exercício 5 — Personalização de E-mail de Marketing (Setor de Marketing)

```python
nome_completo = "lucas ferreira souza"

posicao_espaco = nome_completo.find(" ")
primeiro_nome = nome_completo[:posicao_espaco]
primeiro_nome = primeiro_nome.capitalize()

print(f"Olá, {primeiro_nome}, seja bem-vindo ao nosso clube!")
```

**Saída:**
```
Olá, Lucas, seja bem-vindo ao nosso clube!
```

---

## Lista 3: Exercícios de inputs

### Exercício 1 — Calculadora de Imposto sobre Vendas (Setor Fiscal)

```python
valor_digitado = input("Digite o valor bruto da nota fiscal (Ex: R$ 5.000,00): ")

valor_limpo = valor_digitado.replace("R$", "").strip()
valor_limpo = valor_limpo.replace(".", "").replace(",", ".")
valor_bruto = float(valor_limpo)

imposto = valor_bruto * 0.15

print(f"O valor do imposto (15%) é: R$ {imposto:.2f}")
```

**Exemplo de execução:**
```
Digite o valor bruto da nota fiscal (Ex: R$ 5.000,00): R$ 5.000,00
O valor do imposto (15%) é: R$ 750.00
```

---

### Exercício 2 — Sistema de Cadastro de Colaborador (Setor de RH)

```python
nome_completo = input("Digite o nome completo do colaborador: ").strip()
email_pessoal = input("Digite o e-mail pessoal do colaborador: ")

posicao_espaco = nome_completo.find(" ")
primeiro_nome = nome_completo[:posicao_espaco].capitalize()

email_padronizado = email_pessoal.strip().lower()

print(f"Cadastro concluído: {primeiro_nome}. E-mail de acesso: {email_padronizado}")
```

**Exemplo de execução:**
```
Digite o nome completo do colaborador: Juliana Alves Pereira
Digite o e-mail pessoal do colaborador:  Juliana.Alves@Gmail.com 
Cadastro concluído: Juliana. E-mail de acesso: juliana.alves@gmail.com
```

---

### Exercício 3 — Análise de Metas de Vendas (Setor Comercial)

```python
faturamento_a = float(input("Digite o faturamento da Loja A: ").replace(",", "."))
faturamento_b = float(input("Digite o faturamento da Loja B: ").replace(",", "."))

total = faturamento_a + faturamento_b
media = total / 2

print(f"Faturamento total: R$ {total:,.2f} | Média entre as lojas: R$ {media:,.2f}")
```

**Exemplo de execução:**
```
Digite o faturamento da Loja A: 12000
Digite o faturamento da Loja B: 9500,50
Faturamento total: R$ 21,500.50 | Média entre as lojas: R$ 10,750.25
```

---

## Lista 4: Exercícios com if

### Exercício 1 — Validação de Investimento (Setor Financeiro)

```python
valor_digitado = input("Digite o valor que deseja investir: ")

valor_limpo = valor_digitado.replace("R$", "").strip()
valor_limpo = valor_limpo.replace(".", "").replace(",", ".")
valor = float(valor_limpo)

if valor < 1000:
    print("Perfil iniciante: Sugerimos Tesouro Direto")
elif valor <= 5000:
    print("Perfil moderado: Sugerimos Fundos Imobiliários")
else:
    print("Perfil arrojado: Sugerimos Ações")
```

---

### Exercício 2 — Controle de Acesso ao Sistema (Setor de Segurança)

```python
admins = ["ana@empresa.com", "guilherme@empresa.com", "felipe@empresa.com"]

email_digitado = input("Digite seu e-mail: ")
email_padronizado = email_digitado.strip().lower()

if email_padronizado in admins:
    print("Acesso liberado! Bem-vindo ao painel de controle")
else:
    print("Acesso negado. Você não tem permissões de administrador")
```

---

### Exercício 3 — Cálculo de Desconto Progressivo (Setor de Vendas)

```python
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
```

---

### Exercício 4 — Análise de Metas Combinadas (Setor Comercial)

```python
vendas_vendedor = float(input("Digite as vendas do vendedor: R$ ").replace(",", "."))
meta_vendedor = float(input("Digite a meta individual do vendedor: R$ ").replace(",", "."))
vendas_loja = float(input("Digite as vendas totais da loja: R$ ").replace(",", "."))
meta_loja = float(input("Digite a meta da loja: R$ ").replace(",", "."))

if vendas_vendedor >= meta_vendedor and vendas_loja >= meta_loja:
    bonus = vendas_vendedor * 0.20
else:
    bonus = 0

print(f"Seu bônus este mês é de: R$ {bonus:.2f}")
```

---

### Exercício 5 — Sistema de Triagem de E-mails (Setor de Customer Experience)

```python
assunto = input("Digite o assunto do e-mail: ").lower()

if "pagamento" in assunto or "boleto" in assunto:
    print("Encaminhado para o Financeiro")
elif "entrega" in assunto or "atraso" in assunto:
    print("Encaminhado para a Logística")
else:
    print("Encaminhado para o Suporte Geral")
```

---

## Observações gerais

- Os exercícios que dependem de `input()` foram testados com valores de exemplo nos comentários de saída; ao rodar localmente, o resultado varia conforme o que for digitado.
- Nos exercícios que tratam valores monetários vindos de texto (`"R$ 5.000,00"`), o padrão usado foi: remover o `"R$"`, remover espaços com `.strip()`, remover o ponto de milhar e trocar a vírgula decimal por ponto antes de converter com `float()`.
- Para deixar apenas a primeira letra de cada palavra maiúscula, `.title()` foi usado em nomes completos; para uma única palavra, `.capitalize()` é suficiente.
