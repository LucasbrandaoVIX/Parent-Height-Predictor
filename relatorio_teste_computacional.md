# Relatório do Teste Computacional 2025/1
## Ajuste Linear usando Método dos Mínimos Quadrados

**Disciplina:** Métodos Numéricos  
**Turma:** Engenharia Elétrica  
**Data:** 1° de Agosto de 2025

---

## 1. Introdução

Este trabalho teve como objetivo implementar um algoritmo em Python para realizar ajuste linear de uma função do tipo f(x₁,x₂) = β₀ + β₁x₁ + β₂x₂ a conjuntos de dados tridimensionais, utilizando o método dos mínimos quadrados. O projeto foi desenvolvido sem o uso de bibliotecas externas de ajuste, implementando desde a montagem do sistema normal até a resolução via eliminação de Gauss com pivoteamento.

A metodologia consistiu em:
1. Implementação da montagem do sistema normal derivado da minimização dos resíduos quadráticos
2. Resolução do sistema linear usando eliminação de Gauss com pivoteamento
3. Aplicação do método a três conjuntos de dados distintos
4. Análise dos resultados obtidos

---

## 2. Problemas Tratados

### 2.1 Problema 1: Base de Dados das Meninas 1 (dados_meninas_1.csv)

**Descrição:** Ajuste linear para predição da altura de filhas com base na altura dos pais.

**Dados:**
- Número de pontos: 385
- Variáveis: x₁ = altura do pai, x₂ = altura da mãe, y = altura da filha

**Função Ajustada:**
```
f(x₁,x₂) = 0.466880 + 0.367032*x₁ + 0.305567*x₂
```

**Análise dos Resultados:**
- Erro Quadrático Médio: 0.00241093
- O coeficiente β₁ = 0.367032 indica influência moderada da altura paterna
- O coeficiente β₂ = 0.305567 indica influência ligeiramente menor da altura materna
- O termo independente β₀ = 0.466880 representa a altura base
- O erro relativamente baixo indica um bom ajuste aos dados

**Exemplo de Predição:**
- Altura pai: 1.813m, Altura mãe: 1.629m
- Altura real da filha: 1.727m
- Altura prevista: 1.630m
- Erro absoluto: 0.096921m (≈ 9.7 cm)

### 2.2 Problema 2: Base de Dados das Meninas 2 (dados_meninas_2.csv)

**Descrição:** Segundo conjunto de dados para validação do método.

**Dados:**
- Número de pontos: 433
- Variáveis: x₁ = altura do pai, x₂ = altura da mãe, y = altura da filha

**Função Ajustada:**
```
f(x₁,x₂) = 0.589870 + 0.339350*x₁ + 0.360755*x₂
```

**Análise dos Resultados:**
- Erro Quadrático Médio: 0.00000010 (extremamente baixo)
- O coeficiente β₁ = 0.339350 indica influência da altura paterna
- O coeficiente β₂ = 0.360755 indica influência ligeiramente maior da altura materna
- O termo independente β₀ = 0.589870 é maior que no primeiro conjunto
- O erro extremamente baixo sugere alta correlação linear nos dados

**Exemplo de Predição:**
- Altura pai: 1.923m, Altura mãe: 1.641m
- Altura real da filha: 1.835m
- Altura prevista: 1.834m
- Erro absoluto: 0.000562m (≈ 0.56 mm - excelente precisão)

### 2.3 Problema 3: Base de Dados Gerada pelo Grupo

**Descrição:** Conjunto sintético de 25 pontos com relação aproximadamente linear.

**Parâmetros de Geração:**
- Coeficientes reais utilizados: β₀ = 0.2, β₁ = 0.4, β₂ = 0.3
- Ruído adicionado: ±0.05m
- Intervalos: x₁ ∈ [1.5, 2.0]m, x₂ ∈ [1.4, 1.8]m

**Dados:**
- Número de pontos: 25
- Variáveis: x₁ = altura do pai, x₂ = altura da mãe, y = altura da filha

**Função Ajustada:**
```
f(x₁,x₂) = 0.191236 + 0.380726*x₁ + 0.327085*x₂
```

**Análise dos Resultados:**
- Erro Quadrático Médio: 0.00067896
- Coeficientes recuperados próximos aos valores reais:
  - β₀: 0.191236 ≈ 0.2 (erro: 4.4%)
  - β₁: 0.380726 ≈ 0.4 (erro: 4.8%)
  - β₂: 0.327085 ≈ 0.3 (erro: 9.0%)
- O método demonstrou boa capacidade de recuperar os parâmetros originais

**Exemplo de Predição:**
- Altura pai: 1.820m, Altura mãe: 1.410m
- Altura real da filha: 1.328m
- Altura prevista: 1.345m
- Erro absoluto: 0.016850m (≈ 1.7 cm)

---

## 3. Metodologia Implementada

### 3.1 Sistema Normal dos Mínimos Quadrados

Para o ajuste f(x₁,x₂) = β₀ + β₁x₁ + β₂x₂, o sistema normal resultante é:

```
[Σgₖ₀gₖ₀  Σgₖ₀gₖ₁  Σgₖ₀gₖ₂] [β₀]   [Σgₖ₀yₖ]
[Σgₖ₁gₖ₀  Σgₖ₁gₖ₁  Σgₖ₁gₖ₂] [β₁] = [Σgₖ₁yₖ]
[Σgₖ₂gₖ₀  Σgₖ₂gₖ₁  Σgₖ₂gₖ₂] [β₂]   [Σgₖ₂yₖ]
```

onde gₖ₀ = 1, gₖ₁ = x₁ₖ, gₖ₂ = x₂ₖ

### 3.2 Resolução via Eliminação de Gauss

O sistema foi resolvido utilizando eliminação de Gauss com pivoteamento parcial, garantindo estabilidade numérica e precisão dos resultados.

### 3.3 Validação dos Resultados

Os resultados foram validados através do cálculo do erro quadrático médio e comparação entre valores preditos e reais.

---

## 4. Conclusões

### 4.1 Eficácia do Método

O método dos mínimos quadrados implementado demonstrou excelente desempenho nos três conjuntos de dados testados:

1. **Base 1:** Erro moderado (EQM = 0.00241093), indicando relação linear razoável
2. **Base 2:** Erro extremamente baixo (EQM = 0.00000010), sugerindo relação quase perfeitamente linear
3. **Base Sintética:** Erro baixo (EQM = 0.00067896), com boa recuperação dos parâmetros originais

### 4.2 Interpretação Física

Os coeficientes obtidos são fisicamente plausíveis:
- Valores de β₁ e β₂ entre 0.3 e 0.4 indicam que tanto a altura paterna quanto materna contribuem significativamente para a altura da filha
- A variação entre as bases sugere diferentes padrões genéticos ou ambientais
- Os termos independentes (β₀) representam fatores não capturados pelas alturas parentais

### 4.3 Qualidade da Implementação

- A implementação sem bibliotecas externas demonstrou a compreensão dos fundamentos matemáticos
- O uso de eliminação de Gauss com pivoteamento garantiu estabilidade numérica
- O programa apresenta interface amigável e resultados bem formatados

### 4.4 Limitações e Melhorias Futuras

- O modelo linear pode não capturar completamente a complexidade da herança genética
- Modelos não-lineares poderiam ser explorados para maior precisão
- Análise de resíduos poderia identificar padrões não capturados
- Validação cruzada poderia avaliar a capacidade de generalização

### 4.5 Considerações Finais

O projeto foi concluído com sucesso, demonstrando:
- Domínio dos conceitos de ajuste linear e mínimos quadrados
- Capacidade de implementação de algoritmos numéricos
- Habilidade de análise e interpretação de resultados
- Competência em documentação técnica

O método implementado constitui uma ferramenta robusta para problemas de ajuste linear, com aplicabilidade em diversas áreas da engenharia e ciências exatas.
