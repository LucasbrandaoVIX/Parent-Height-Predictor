# Eliminação de Gauss - Módulo separado
# Baseado no código fornecido

def le_sistema_de_arquivo(filename):
    with open(filename, 'r') as f:
        lines = f.read().strip().splitlines()  
    n = int(lines[0])
    A = [list(map(float, lines[i + 1].split())) for i in range(n)]
    b = list(map(float, lines[n + 1].split()))
    return n, A, b


def exibe_sistema(A, b, label=""): #exibe com  formatação
    print(f"\n{label}")
    for i in range(len(A)):
        row = ' '.join(f"{A[i][j]:>10.4f}" for j in range(len(A)))
        print(f"[{row}] | {b[i]:>10.4f}")
    print()   

def  exibe_vetor(v, label=""):
    for i in range(len(v)):
        print(f"{label}[{i}] = {v[i]:.14f}")
    print()


# ------------------------------------------------------------------
# Dado um sistema A|b, obtem a sua solução via Eliminação de Gauss
# -----------------------------------------------------------------  
def Eliminacao_de_Gauss_com_pivoteamento(n, A, b):

    # fazendo cópia dos dados para não alterar os originais
    A_copia = [linha[:] for linha in A]
    b_copia = b[:]

    for k in range(0,n-1):  # k-esima etapa da Eliminação
        # fazendo o pivoteamento
        Amax = abs(A_copia[k][k])
        lin_indice_max = k
        for i in range(k,n): #percorre as linhas abaixo da diagonal
          if abs( A_copia[i][k] )  > Amax:
           Amax = abs(A_copia[i][k])
           lin_indice_max = i 

        if abs(A_copia[lin_indice_max][k]) < 1e-15:
            raise ValueError(f"Pivo nulo (ou próximo de zero) na etapa {k}.")

        if lin_indice_max != k: #fazer a troca de linhas
            A_copia[k], A_copia[lin_indice_max] = A_copia[lin_indice_max], A_copia[k]
            b_copia[k], b_copia[lin_indice_max] = b_copia[lin_indice_max], b_copia[k]

        for i in range(k + 1, n):  # i se refere à linha
            m = A_copia[i][k] / A_copia[k][k] 
            A_copia[i][k] = 0.0
            for j in range(k+1, n):  # j se refere à coluna 
                A_copia[i][j] =  A_copia[i][j]  - m * A_copia[k][j]
            b_copia[i] = b_copia[i] - m * b_copia[k]
    # fim {sistema triangularizado}    

    # Retrosubstituição
    # criando a lista com elementos nulos
    x = [0.0 for i in range(n)]

    x[n-1]= b_copia[n-1]/A_copia[n-1][n-1]  # Correção: usar índice correto
    passo = -1
    for i in range((n-2),(-1), passo): 
        soma = 0
        for j in range(i + 1, n):
           soma = soma + A_copia[i][j] * x[j]
        x[i] = (b_copia[i] - soma) / A_copia[i][i]

    return x
