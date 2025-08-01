#
# Eliminação de Gauss


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
def Eliminação_de_Gauss_com_pivoteamento(n, A, b):

    exibe_sistema(A,b,"Sistema inicial")

    for k in range(0,n-1):  # k-esima etapa da Eliminação
        # fazendo o pivoteamento
        Amax = abs(A[k][k])
        lin_indice_max = k
        for i in range(k,n): #percorre as linhas abaixo da diagonal
          if abs( A[i][k] )  > Amax:
           Amax = abs(A[i][k])
           lin_indice_max = i 

        if abs(A[lin_indice_max][k]) < 1e-15:
            raise ValueError(f"Pivo nulo (ou próximo de zero) na etapa {k}.")

        if lin_indice_max != k: #fazer a troca de linhas
            A[k], A[lin_indice_max] = A[lin_indice_max], A[k]
            b[k], b[lin_indice_max] = b[lin_indice_max], b[k]

        for i in range(k + 1, n):  # i se refere à linha
            m = A[i][k] / A[k][k] 
            A[i][k] = 0.0
            for j in range(k+1, n):  # j se refere à coluna 
                A[i][j] =  A[i][j]  - m * A[k][j]
            b[i] = b[i] - m * b[k]
        #exibe_sistema(A, b, f"Após a {k+1}a Etapa ")
    # fim {sistema triangularizado}    
    exibe_sistema(A, b, f"Sistema triangularizado ")

    # Retrosubstituição
    # criando a lista com elementos nulos
    x = [0.0 for i in range(n)]

    x[n-1]= b[i]/A[i][i]
    passo = -1
    for i in range((n-2),(-1), passo): 
        soma = 0
        for j in range(i + 1, n):
           soma = soma + A[i][j] * x[j]
        x[i] = (b[i] - soma) / A[i][i]

    return x
     
# -------------------
#    Main/Principal
# -------------------
# 
# Abaixo há 2 exemplos de sistema lineares resolvidos via Eliminação de Gauss
#
# Exemplo  1)  colocado "à mão no código"
# inicializando/criando uma lista para a matriz A, colocando zeros em todas as posicões 
print("--- Exemplo de um sistema ---")
n = 2
A = [[0 for i in range(2)] for j in range(2)]
#  termo independente b
# inicializando/criando um b (uma lista) com elementos nulos
b = [0.0 for i in range(n)]
# refere-se  à matriz do problema de ajuste por uma reta do exercicio 1 da lista de Ajuste
# Sistema
#Primeira linha  de A (Linha indice 0)
A[0][0] = 5;         A[0][1] = 10;      
# Segunda linha de A (linha indice 1)
A[1][0] = A[0][1];   A[1][1] = 30;       
# termo b
b[0] = 17.70
b[1]=  28.20
# resolvendo o sistema 
x = Eliminação_de_Gauss_com_pivoteamento(n, A, b)
exibe_vetor(x, label="solução")

# Exemplo  2)  entrada via leitura de arquivo
print("--- Outro Exemplo ---")
try:
    nome_arquivo = "exemplo_sistema.txt"  
    # ATENÇAO o arquivo deve estar na mesma pasta que o codigo
    n, A, b = le_sistema_de_arquivo(nome_arquivo)
    # resolvendo o sistema 
    x = Eliminação_de_Gauss_com_pivoteamento(n, A, b)
    exibe_vetor(x, label="solução")
except Exception as erro:
    print("Erro:", erro)


