'''Entrar com valor de um empréstimo, a taxa de juros e a quantidade de meses. Fazer um programa que calcule o valor da prestação.'''

valorEmp = float(input('Digite o valor do emprestimo: '))
txJuros = float(input('Digite a taxa de juros:'))
qdtMes = int(input('Digite o numero de pretações:'))

prestacao = (valorEmp+(valorEmp*(txJuros/100)))/qdtMes

print('O valor da prestação é de:', prestacao)
