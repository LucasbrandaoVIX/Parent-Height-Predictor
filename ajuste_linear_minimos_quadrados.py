"""

.Ajuste Linear usando Método dos Mínimos Quadrados

Componentes do Grupo:
- Lucas Dantas Brandão.

Objetivo: Implementar ajuste de função f(x1,x2) = β0 + β1*x1 + β2*x2
usando método dos mínimos quadrados sem bibliotecas de ajuste existentes.
"""

from eliminacao_de_gauss import Eliminacao_de_Gauss_com_pivoteamento


def le_dados_csv(nome_arquivo):
    """
    Lê um arquivo CSV com dados de altura do pai, mãe e filho(a)
    Retorna 3 listas: altura_pai, altura_mae, altura_filha
    """
    altura_pai = []
    altura_mae = []
    altura_filha = []
    
    try:
        with open(nome_arquivo, 'r') as f:
            linhas = f.readlines()
        
        for linha in linhas:
            partes = linha.strip().split(',')
            if len(partes) != 3:
                continue
            
            altura_pai.append(float(partes[0]))
            altura_mae.append(float(partes[1]))
            altura_filha.append(float(partes[2]))
    
    except FileNotFoundError:
        print(f"Arquivo não encontrado: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao processar arquivo: {e}")
    
    return altura_pai, altura_mae, altura_filha


def montar_sistema_normal(x1_dados, x2_dados, y_dados):
    """
    Monta o sistema normal Ax = b para o ajuste linear
    f(x1,x2) = β0 + β1*x1 + β2*x2
    
    Sistema resultante:
    [Σg0g0  Σg0g1  Σg0g2] [β0]   [Σg0y]
    [Σg1g0  Σg1g1  Σg1g2] [β1] = [Σg1y]
    [Σg2g0  Σg2g1  Σg2g2] [β2]   [Σg2y]
    
    onde g0=1, g1=x1, g2=x2
    """
    n = len(x1_dados)
    
    # Inicializar somatórios
    soma_g0g0 = 0  # Σ1*1 = n
    soma_g0g1 = 0  # Σ1*x1 = Σx1
    soma_g0g2 = 0  # Σ1*x2 = Σx2
    soma_g1g0 = 0  # Σx1*1 = Σx1
    soma_g1g1 = 0  # Σx1*x1 = Σx1²
    soma_g1g2 = 0  # Σx1*x2
    soma_g2g0 = 0  # Σx2*1 = Σx2
    soma_g2g1 = 0  # Σx2*x1 = Σx1*x2
    soma_g2g2 = 0  # Σx2*x2 = Σx2²
    
    soma_g0y = 0   # Σ1*y = Σy
    soma_g1y = 0   # Σx1*y
    soma_g2y = 0   # Σx2*y
    
    # Calcular os somatórios
    for k in range(n):
        g0 = 1
        g1 = x1_dados[k]
        g2 = x2_dados[k]
        y = y_dados[k]
        
        soma_g0g0 += g0 * g0
        soma_g0g1 += g0 * g1
        soma_g0g2 += g0 * g2
        soma_g1g0 += g1 * g0
        soma_g1g1 += g1 * g1
        soma_g1g2 += g1 * g2
        soma_g2g0 += g2 * g0
        soma_g2g1 += g2 * g1
        soma_g2g2 += g2 * g2
        
        soma_g0y += g0 * y
        soma_g1y += g1 * y
        soma_g2y += g2 * y
    
    # Montar a matriz A do sistema
    A = [
        [soma_g0g0, soma_g0g1, soma_g0g2],
        [soma_g1g0, soma_g1g1, soma_g1g2],
        [soma_g2g0, soma_g2g1, soma_g2g2]
    ]
    
    # Montar o vetor b do sistema
    b = [soma_g0y, soma_g1y, soma_g2y]
    
    return A, b


def calcular_erro_quadratico_medio(x1_dados, x2_dados, y_dados, beta0, beta1, beta2):
    """
    Calcula o erro quadrático médio do ajuste
    """
    n = len(x1_dados)
    soma_erros_quadrados = 0
    
    for k in range(n):
        y_predito = beta0 + beta1 * x1_dados[k] + beta2 * x2_dados[k]
        erro = y_dados[k] - y_predito
        soma_erros_quadrados += erro * erro
    
    erro_quadratico_medio = soma_erros_quadrados / n
    return erro_quadratico_medio


def exibir_resultados(nome_base, x1_dados, x2_dados, y_dados, beta0, beta1, beta2):
    """
    Exibe os resultados do ajuste de forma organizada
    """
    print(f"\n{'='*60}")
    print(f"RESULTADOS DO AJUSTE - {nome_base}")
    print(f"{'='*60}")
    print(f"Número de pontos: {len(x1_dados)}")
    print(f"\nFunção ajustada:")
    print(f"f(x1,x2) = {beta0:.6f} + {beta1:.6f}*x1 + {beta2:.6f}*x2")
    print(f"\nOnde:")
    print(f"  x1 = altura do pai")
    print(f"  x2 = altura da mãe")
    print(f"  f(x1,x2) = altura prevista da filha")
    
    # Calcular e exibir erro quadrático médio
    eqm = calcular_erro_quadratico_medio(x1_dados, x2_dados, y_dados, beta0, beta1, beta2)
    print(f"\nErro Quadrático Médio: {eqm:.8f}")
    
    # Exemplo de predição
    if len(x1_dados) > 0:
        x1_exemplo = x1_dados[0]
        x2_exemplo = x2_dados[0]
        y_real = y_dados[0]
        y_predito = beta0 + beta1 * x1_exemplo + beta2 * x2_exemplo
        
        print(f"\nExemplo de predição:")
        print(f"  Altura pai: {x1_exemplo:.3f}m, Altura mãe: {x2_exemplo:.3f}m")
        print(f"  Altura real da filha: {y_real:.3f}m")
        print(f"  Altura prevista: {y_predito:.3f}m")
        print(f"  Erro absoluto: {abs(y_real - y_predito):.6f}m")


def fazer_ajuste(nome_base, x1_dados, x2_dados, y_dados):
    """
    Realiza o ajuste linear completo para um conjunto de dados
    """
    print(f"\nProcessando {nome_base}...")
    print(f"Montando sistema normal...")
    
    # Montar o sistema normal
    A, b = montar_sistema_normal(x1_dados, x2_dados, y_dados)
    
    print(f"Resolvendo sistema linear...")
    
    # Resolver o sistema usando eliminação de Gauss
    try:
        solucao = Eliminacao_de_Gauss_com_pivoteamento(3, A, b)
        beta0, beta1, beta2 = solucao[0], solucao[1], solucao[2]
        
        # Exibir resultados
        exibir_resultados(nome_base, x1_dados, x2_dados, y_dados, beta0, beta1, beta2)
        
        return beta0, beta1, beta2
        
    except Exception as e:
        print(f"Erro ao resolver sistema: {e}")
        return None, None, None


def menu_principal():
    """
    Menu principal do programa
    """
    while True:
        print("\n" + "="*50)
        print("AJUSTE LINEAR - MÉTODO DOS MÍNIMOS QUADRADOS")
        print("Predição de Altura de Filhas")
        print("="*50)
        print("Digite uma opção:")
        print("1 - Fazer o ajuste com a base de dados 1 (dados_meninas_1.csv)")
        print("2 - Fazer o ajuste com a base de dados 2 (dados_meninas_2.csv)")
        print("3 - Fazer o ajuste com a base inventada pelo grupo")
        print("0 - Sair")
        
        try:
            escolha = input("\nEscolha: ").strip()
            
            if escolha == "0":
                print("Encerrando programa...")
                break
                
            elif escolha == "1":
                x1, x2, y = le_dados_csv("dados_meninas_1.csv")
                if x1:
                    fazer_ajuste("Base de Dados 1 (dados_meninas_1.csv)", x1, x2, y)
                else:
                    print("Erro ao carregar dados da base 1")
                    
            elif escolha == "2":
                x1, x2, y = le_dados_csv("dados_meninas_2.csv")
                if x1:
                    fazer_ajuste("Base de Dados 2 (dados_meninas_2.csv)", x1, x2, y)
                else:
                    print("Erro ao carregar dados da base 2")
                    
            elif escolha == "3":
                x1, x2, y = le_dados_csv("dados_grupo.csv")
                if x1:
                    fazer_ajuste("Base de Dados Gerada pelo Grupo (dados_grupo.csv)", x1, x2, y)
                else:
                    print("Erro ao carregar dados do grupo. Execute 'python gerar_dados_grupo.py' primeiro.")
                
            else:
                print("Opção inválida! Tente novamente.")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário.")
            break
        except Exception as e:
            print(f"Erro inesperado: {e}")


if __name__ == "__main__":
    print("Ajuste Linear usando Método dos Mínimos Quadrados")
    
    menu_principal()
