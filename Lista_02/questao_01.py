'''1. Entrar com dois números inteiros e imprimir a seguinte saída: a)dividendo; b) divisor; c) quociente; d) resto.'''

print("Digite dois numero inteiros")

divisor = int(input())
dividendo = int(input())

print('O divisor é:', divisor, '\nO dividendo é:', dividendo, '\nO quociente é:',
      round(divisor/dividendo, 2), '\nO resto da divisão é:', divisor % dividendo)
