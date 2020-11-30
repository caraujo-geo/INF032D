'''11. Você e os outros integrantes da sua república (Joca, Moacir, Demival e Jackson) foram no supermercado ecompraram alguns itens:
•75 latas de cerveja: R$ 2,20 cada (da ruim ainda, pra fazer o dinheiro render)
• 2 pacotes de macarrão: R$ 8,73 cada
• 1 pacote de Molho de tomate: R$ 3,45
• 420g Cebola: R$ 5,40/kg
• 250g de Alho: R$ 30/kg
• 450g de pães franceses: R$ 25/kg'''

alunos = 5
cerv = 2.20 * 75
macar = 8.73 * 2
molTom = 3.45 * 1
cebo = 5.40*(420/1000)
alho = 30*(250/1000)
pao = 25*(450/1000)
conta = (cerv + macar + molTom + cebo + alho + pao)/alunos
print('O valor que cada aluno deve pagar é de R$: ', round(conta, 2))
