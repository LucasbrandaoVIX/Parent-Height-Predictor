"""
Gerador de Base de Dados do Grupo
Cria um arquivo CSV com os dados sintéticos para análise posterior
"""

import random


def gerar_e_salvar_base_grupo(nome_arquivo="dados_grupo.csv", n_pontos=25):
    """
    Gera e salva base de dados do grupo em arquivo CSV
    """
    # Coeficientes "reais" para gerar os dados
    beta0_real = 0.2
    beta1_real = 0.4
    beta2_real = 0.3
    
    print(f"Gerando base de dados com {n_pontos} pontos...")
    print(f"Parâmetros reais:")
    print(f"  β0 = {beta0_real}")
    print(f"  β1 = {beta1_real}")  
    print(f"  β2 = {beta2_real}")
    
    random.seed(42)  # Para reprodutibilidade
    
    dados = []
    
    for i in range(n_pontos):
        # Gerar x1 e x2 aleatórios em intervalos realistas
        x1 = random.uniform(1.5, 2.0)  # altura do pai entre 1.5m e 2.0m
        x2 = random.uniform(1.4, 1.8)  # altura da mãe entre 1.4m e 1.8m
        
        # Calcular y com a relação linear + ruído pequeno
        y_teorico = beta0_real + beta1_real * x1 + beta2_real * x2
        ruido = random.uniform(-0.05, 0.05)  # ruído pequeno
        y = y_teorico + ruido
        
        dados.append((x1, x2, y))
    
    # Salvar em arquivo CSV
    try:
        with open(nome_arquivo, 'w') as f:
            for x1, x2, y in dados:
                f.write(f"{x1:.6f},{x2:.6f},{y:.6f}\n")
        
        print(f"\nDados salvos em: {nome_arquivo}")
        print(f"Formato: altura_pai,altura_mae,altura_filha")
        
        # Exibir primeiros pontos como exemplo
        print(f"\nPrimeiros 5 pontos gerados:")
        for i in range(min(5, len(dados))):
            x1, x2, y = dados[i]
            print(f"  {i+1}: Pai={x1:.3f}m, Mãe={x2:.3f}m, Filha={y:.3f}m")
            
    except Exception as e:
        print(f"Erro ao salvar arquivo: {e}")
    
    return dados


if __name__ == "__main__":
    print("Gerador de Base de Dados do Grupo")
    print("Teste Computacional 2025/1 - Engenharia Elétrica")
    print("="*50)
    
    gerar_e_salvar_base_grupo("dados_grupo.csv", 25)
