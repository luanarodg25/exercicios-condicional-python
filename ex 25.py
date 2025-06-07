num_horas_ex = int(input('Digite o número de horas extras trabalhadas: '))
num_horas_faltas = int(input('Digite o número de horas faltadas ao trabalho: '))


horas = num_horas_ex -(2/3*(num_horas_faltas))

minutos = horas * 60

if minutos >= 2400:
    premio = 500
elif minutos > 1800:
    premio = 400
elif minutos >= 1200:
    premio = 300
elif minutos < 1200 and minutos > 600:
    premio = 200
else:
    premio = 100
print(f'O valor do prêmio foi de R${premio}.') 
