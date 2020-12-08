'''Dada a frase “Python é muito legal". 
use fatiamento para dar nome às variáveis contendo cada palavra. Qual o tamanho dessa frase? E qual o tamanho de cada palavra?'''

frase = ("Python é muito legal")

print(frase)

tamFrase = len(frase)
verf = frase.split(" ")[0:tamFrase]
v1 = verf[0]
v2 = verf[1]
v3 = verf[2]
v4 = verf[3]

print(f'O tamanho da frase é: {len(frase)} '.format(frase))
print(f'O tamanho da primeira palavra é: {len(v1)} '.format(v1))
print(f'O tamanho da segunda  palavra é: {len(v2)} '.format(v2))
print(f'O tamanho da terceira palavra é: {len(v3)} '.format(v3))
print(f'O tamanho da quarta palavra é: {len(v4)} '.format(v4))
