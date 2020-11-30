'''12.Krissia gosta de bolinhas de queijo. Ela quer saber quantas bolinhas de queijo dá para colocar dentro de um potede sorvete de 2𝐿. 
Ela pensou assim:
Um pote de sorvete tem dimensões 15 cm x 10 cm x 13 cm. 
Uma bolinha de queijo é uma esferade raio r = 1.2 cm. 
O fator de empacotamento ideal é 0.74, mas o pote de sorvete tem tamanho comparável às bolinhas de queijo, aí tem efeitos de borda, então o fator deve ser menor. 
Mas asbolinhas de queijo são razoavelmente elásticas, então empacota mais. 
Esse valor parece razoável.Sabendo que o volume de uma esfera de raio 𝑟é 𝑉= 43𝜋𝑟3, o volume do pote de sorvete é 𝑉= 𝑥• 𝑦• 𝑧e o fator de empacotamento é a fração de volume ocupado pelas bolinhas de queijo. 
Ou seja, 74% do pote de sorvete vaiser ocupado pelas bolinhas de queijo.
Ajude a Krissia descobrir quantas bolinhas de queijo cabem no pote de sorvete!'''

volPote = 15*10*13
pi = 3.141592
rBol = 1.2
volBoli = (4*pi*(rBol**3))/3
volPoteOcup = volPote*0.74
boliPote = volPoteOcup / volBoli

print(' No pote de sorvete de Krissia cabem', int(boliPote), 'bolinhas')
