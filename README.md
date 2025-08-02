# Teste Computacional 2025/1 - Ajuste Linear

## Predição de Altura usando Método dos Mínimos Quadrados

### Descrição do Projeto

Este projeto implementa um sistema de ajuste linear para predição da altura de filhas com base na altura dos pais, utilizando o método dos mínimos quadrados. O trabalho foi desenvolvido como parte do Teste Computacional da disciplina de Métodos Numéricos para o curso de Engenharia Elétrica.

### Objetivos

- Implementar ajuste de função linear f(x1,x2) = β0 + β1*x1 + β2*x2
- Resolver sistema normal usando eliminação de Gauss com pivoteamento
- Aplicar o método a dados reais de altura familiar
- Validar a implementação com dados sintéticos

### Estrutura do Projeto

```
parent-height-predictor/
├── dados_meninas_1.csv                   # Base de dados 1 (385 pontos)
├── dados_meninas_2.csv                   # Base de dados 2 (433 pontos)
├── dados_grupo.csv                       # Base sintética gerada (25 pontos)
├── ajuste_linear_minimos_quadrados.py    # Implementação principal
├── eliminacao_de_gauss.py                # Módulo eliminação de Gauss
├── gerar_dados_grupo.py                  # Gerador de dados sintéticos
├── relatorio_teste_computacional.md     # Relatório completo
└── README.md                             # Este arquivo
```

### Como Executar

#### Programa Principal
```bash
python ajuste_linear_minimos_quadrados.py
```

#### Gerar Nova Base de Dados Sintética (se necessário)
```bash
python gerar_dados_grupo.py
```

### Resultados Obtidos

#### Base de Dados 1 (dados_meninas_1.csv)
- Pontos: 385
- Função: f(x1,x2) = 0.466880 + 0.367032*x1 + 0.305567*x2
- Erro Quadrático Médio: 0.00241093
- Qualidade: Boa correlação linear

#### Base de Dados 2 (dados_meninas_2.csv)
- Pontos: 433
- Função: f(x1,x2) = 0.589870 + 0.339350*x1 + 0.360755*x2
- Erro Quadrático Médio: 0.00000010
- Qualidade: Excelente correlação linear

#### Base Sintética do Grupo (25 pontos)
- Parâmetros Reais: β0=0.2, β1=0.4, β2=0.3
- Função Ajustada: f(x1,x2) = 0.191236 + 0.380726*x1 + 0.327085*x2
- Erro Quadrático Médio: 0.00067896
- Recuperação: Excelente (erros menores que 10%)

### Metodologia

1. **Sistema Normal:** Montagem do sistema Ax = b a partir da minimização dos resíduos quadráticos
2. **Resolução:** Eliminação de Gauss com pivoteamento parcial para estabilidade numérica
3. **Validação:** Cálculo de métricas (EQM) e análise de resíduos

### Dependências

- Python 3.x (sem bibliotecas externas)
- Módulos internos utilizados: nenhum além dos padrão do Python

### Interpretação dos Resultados

#### Coeficientes Físicos
- **β1 (altura pai):** Influência da herança paterna (0.34-0.38)
- **β2 (altura mãe):** Influência da herança materna (0.31-0.36)  
- **β0 (termo independente):** Fatores não capturados pelo modelo

#### Qualidade do Ajuste
- **EQM < 0.001:** Excelente
- **EQM < 0.01:** Muito Boa
- **EQM < 0.1:** Boa
- **EQM > 0.1:** Necessita melhorias

### Funcionalidades Principais

- Leitura de dados CSV
- Montagem do sistema normal dos mínimos quadrados
- Resolução via eliminação de Gauss com pivoteamento
- Cálculo de métricas de qualidade
- Interface de menu interativa
- Geração de dados sintéticos para validação

### Formato dos Dados

Os arquivos CSV seguem o formato:
```
altura_pai,altura_mae,altura_filha
1.813,1.629,1.727
1.825,1.617,1.617
...
```

- **Unidade:** metros
- **Precisão:** 6 casas decimais
- **Separador:** vírgula

### Menu do Sistema

```
Digite uma opção:
1 - Fazer o ajuste com a base de dados 1
2 - Fazer o ajuste com a base de dados 2  
3 - Fazer o ajuste com a base inventada pelo grupo
0 - Sair
```

### Referências Teóricas

- Método dos Mínimos Quadrados para Ajuste Linear
- Eliminação de Gauss com Pivoteamento
- Análise de Regressão Linear Múltipla
- Métricas de Avaliação de Modelos

---

**Desenvolvido para:** Universidade Federal do Espírito Santo (UFES)  
**Disciplina:** Métodos Numéricos  
**Período:** 2025/1
