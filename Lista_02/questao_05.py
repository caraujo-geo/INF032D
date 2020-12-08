'''Calcular a quantidade de litros de combustível gastos em uma viagem, sabendo-se que o carro faz 12km com 1 litro. Deverão. Ser fornecidos
a) tempo gasto na viagem;
b) e a velocidade media.
Apresentar os valores da velocidade media, tempo gasto, distancia percorrida e quatidade de litros gastos.'''

tempo = int(input('Dgite quantas horas foi gasto na viagem: '))
velMedia = float(input('Digite a velecidaade media da viagem: '))
disPercorrida = velMedia * tempo
qdtLitros = disPercorrida / 12

print('A velocidade media e: ', velMedia, '\nO tempo gasto foi de:', tempo, 'horas\nA distância percorrida foi de: ', disPercorrida,
      ' Km\nA quantidade litros gastos foi de: ', round(qdtLitros, 2))
