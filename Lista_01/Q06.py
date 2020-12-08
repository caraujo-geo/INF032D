''' Se você correr 65 quilômetros em 3 horas, 23 minutos e 17 segundos, qual é a sua velocidade média em m/s?'''

deslocamentoKm = 65
horas = 3
min = 23
seg = 17
segTot = ((horas*3600)+(min*60)) + seg
deslocMet = deslocamentoKm * 1000
velMed = deslocMet/segTot

print(' A velicidade média foi de:', round(velMed, 2))
