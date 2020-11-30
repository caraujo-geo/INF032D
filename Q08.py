''' supondo um numero 123, imprimi-lo invertido. Exemplo (123,321). O numero deverá ser armazenado em outra variável.'''

num = 123
cen = int(num/100)
dez = int((num % 100)/10)
uni = int(num - (cen*100+dez*10))
numIvert = int((uni*100)+(dez*10)+cen)
print('O numero ', num, 'invertido é:', numIvert)
