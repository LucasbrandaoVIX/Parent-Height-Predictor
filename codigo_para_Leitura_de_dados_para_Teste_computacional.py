# Esse código  é o esqueleto/template  para ser usado 
# para o desenvolvmento do Teste Computacional
# Faz a leiutra dos dados dos arquivos
#  e cria listas com esses dados
# para que possam ser usados para montar o sistema normal para fazer o ajuste de dados


def exibe_alguns_elementos(lista, qte_elem_exibidos):#------------
    for i in range(0, qte_elem_exibidos):
      print(f" o elemento {i} da lista: {lista[i]}  ") 
# ------------------------------

# Lê um arquivo com dados com 
#  altura do pai, altura da mae e altura  do/a filho/a 
# ------------------------------
def Cria_Listas_dados(nome_arquivo): #Faz a  leitura dos dados e retorna  3 listas 
    xp_altura_pai = []
    xm_altura_mae = []
    y_altura_cria = [] # altura do filho ou da filha

    try:
        with open(nome_arquivo, 'r') as f:
            linhas = f.readlines()

        for linha in linhas:
            partes = linha.strip().split(',')
            if len(partes) != 3:
                print("Linha ignorada (formato inesperado):", linha)
                continue

            xp_altura_pai.append(float(partes[0]))
            xm_altura_mae.append(float(partes[1]))
            y_altura_cria.append(float(partes[2]))

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {nome_arquivo}")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

    return xp_altura_pai, xm_altura_mae, y_altura_cria
#------------------

#
# -------------------
#    Main/Principal
# -------------------
try:
    nome_arquivo= "dados_meninas_1.csv"  # exemplo com o arquivo  das meninas
    xp, xm, y = Cria_Listas_dados(nome_arquivo)
    print("Foram criadas 3 listas")
    print("Mostrando alguns dados da lista com a altura dos pais, do arquivo "+ nome_arquivo)
    exibe_alguns_elementos(xp,5)
    #exibindo _alguns_elementos da  lista
    print("Mostrando alguns dados da lista com a altura dos mães, do arquivo "+ nome_arquivo)
    exibe_alguns_elementos(xm,5)
except Exception as erro:
    print("Erro:", erro)


