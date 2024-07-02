# arquivo onde criamos nossas funções que queremos utilzar em toda a nossa experiência

def fatorial(n):
    fat = 1
    for x in range(1, n + 1):
        fat *= x
    return fat

def dobro(n):
    return n * 2

def triplo(n):
    return n * 3
