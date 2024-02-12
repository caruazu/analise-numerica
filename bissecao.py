# defina sua função
# a função deve ser contínua no intervalo e no conjunto numérico dos reais
def funcao(x):
    y = 2*x**2 + x - 2
    return y

# intervalo de operacao:
x_inicio = -2
x_fim = -1

# criterios de parada
tolerancia_de_erro = 10**-4
limite_de_iterecoes = 10**3

# PARA FAZER: implementar aqui a verificação de intervalo
# o meio do intervalo já é a raiz?
# só tem uma raiz no intervalo? (usar derivada)
# muda de sinal?
# esta na ordem correta?

# inicialização burra de variaveis
cabeçalho = ["i","y_meio","x_meio","x_inicio","x_fim","erro"]
print("{: >6} {: >30} {: >20} {: >20} {: >20} {: >20}".format(*cabeçalho))
erro = 100
y_meio = 1

# o meio do intervalo é suficientemente próximo a raiz?
while(limite_de_iterecoes>0 and y_meio!=0 and erro>tolerancia_de_erro):

    x_meio = x_inicio + ((x_fim - x_inicio)/2)
    y_meio = funcao(x_meio)
    y_inicio = funcao(x_inicio)

    # do inicio até o meio do intervalo a função muda de sinal?
    if (y_inicio * y_meio < 0):
        # a raiz está entre o inicio e o meio
        x_fim = x_meio
    else:
        # a raiz esta entre o meio e o fim
        x_inicio = x_meio

    limite_de_iterecoes=limite_de_iterecoes-1

    # cálculo do erro:
    # pelas características do método, sabemos que o erro é igual a:
    erro = (x_fim - x_inicio)/2

    estado = [limite_de_iterecoes,y_meio,x_meio,x_inicio,x_fim,erro]
    print("{: >6} {: >30} {: >20} {: >20} {: >20} {: >20}".format(*estado))