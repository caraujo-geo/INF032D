

fitas = int(input('Digite a quantidade fitas que a locadora possui:  '))
valor = float(input('Digite o valor da locação de cada fita:  '))

faturamento = ((fitas/3) * valor)*12
multaMensal = (((fitas/3) * 0.1)*(valor*0.1))
fitasFinal = int((fitas - (fitas*0.02)+(fitas*0.1)))

print('o faturamento anuel é de: {}'.format(faturamento))
print('O valor ganho com multas pod mês é de: {}'.format(multaMensal))
print('A quantidade de fitas no final do ano é de: {}'.format(fitasFinal))
