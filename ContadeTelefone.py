# Considere a empresa de telefonia "Tchau".
#Abaixo de 200 minutos, a empresa cobra  R$ 0,20 por minuto;
#Entre 200 e 400 minutos, a empresa cobra  R$ 0,18 por minuto;
#Acima de 400 minutos, a empresa cobra  R$ 0,15 por minuto;
# Calcule a conta de telefone:
minutos = int(input(" Minutos utilizados: "))
if minutos < 200:
    valor = 0.20
    conta = minutos * valor
    print("A conta é de: ", f'R${conta:.2f}')

if  200 < minutos <= 400:
    valor = 0.18
    conta = minutos * valor
    print("A conta é de: ", f'R${conta:.2f}')

elif minutos > 400:
    valor = 0.15
    conta = minutos * valor
    print("A conta é de: ", f'R${conta:.2f}')
