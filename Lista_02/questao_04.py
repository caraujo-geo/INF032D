'''Calcular o salario liquido de um professor. Os dados fornecidos serão: a) valor hora aula; b) numero de aulas dadas; c) percentual de desconto INSS.'''

horaAula = float(input('Digite o valor da hora/aula: '))
aulas = int(input('Dgite a quantidade de aulas minitradas: '))
descINSS = float(input('Digite o percentual de desconto do INSS:'))

salBruto = horaAula * aulas
salLiq = (salBruto - (salBruto * (descINSS / 100)))

print(salBruto)
print(salLiq)
