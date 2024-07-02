# Modulação em Python, crie suas próprias bibliotecas/pacotes

# para isso, precisamos de arquivos.pyc para rodar os códigos
# o VS-Code já automatiza isso criando a pasta __pycache__ com todos os arquivos necessários
# em Python, a pasta "uteis" é chamada Pacote enquanto seus arquivos de funções de bibliotecas

# importando nossos arquivos/bibliotecas/pacotes
# import Módulos.uteis.numeros as num
# ou
from uteis import numeros as num
from uteis import strings as sng

# PÁGINA PRINCIPAL
n = int(input("Digite um número: "))
txt = input("Digite um texto: ")

print()

print(f"O fatorial de {n} é {num.fatorial(n)}")
print(f"O dobro de {n} é {num.dobro(n)}")
print(f"O triplo de {n} é {num.triplo(n)}")
sng.escreva(txt)
