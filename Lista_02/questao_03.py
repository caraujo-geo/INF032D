'''Entrar com um nome e imprimir: a) todo o nome; b) primeiro carcater; c) ultimo carcater; d) do primeiro ate o terceiro caracter; 
e)quarto caracter; f) os dois últimos.'''

nome = input("Digite seu nome:")

print(nome)

pos = (len(nome))

print('O primeiro caracter é:', nome[0])
print('O ultimo caracter é:', nome[pos-1])
print('O quarto caracter é:', nome[3])
print('Do primeiro ate o terceiro caracter:', nome[0:3])
print('Os dois últimos caracteres são:', nome[pos-2:pos])
