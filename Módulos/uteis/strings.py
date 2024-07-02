# Arquivo que guarda funções para strings.

def escreva(texto):
    '''
    --> Função que imprime um texto formatado por linhas
    :texto: mensagem que você quer formatar
    :retunr - print: Mensagem formatada
    '''

    tam = len(texto) + 4
    print("~"*tam)
    print(f"  {texto}")
    print("~"*tam)
