'''Dado um numero de conta corrente com três dígitos, retorne o seu digito verificador, o qual é calculado da seguinte maneira. 
Exemplo: numero conta 235, somar o numero da conta com seu inverso : 235+532=767. 
Multiplicar cada digito pela sua ordem posicional e somar estes resultados: 7 6 7 (7x1+6x2+7x3) = 40. 
O ultimo digito desse resultado é o digito verificador da conta (40-> 0 )'''

conta = int(input('Digite o numero de sua conta de três digitos: '))

cen = int(conta/100)
dez = int((conta % 100)/10)
uni = int(conta - (cen*100+dez*10))
numIvert = int((uni*100)+(dez*10)+cen)
somaConNumInvert = conta + numIvert
somaCen = int(somaConNumInvert/100)
somaDez = int((somaConNumInvert % 100)/10)
somaUni = int(somaConNumInvert - (cen*100+dez*10))
multSoma = (somaCen*1+somaDez*2+somaUni*3)
dv = multSoma % 10

print('O digito verificar da conta é:', dv)
