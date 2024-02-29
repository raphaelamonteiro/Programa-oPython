velocidade = int(input(" Digite a velocidade do carro: "))
if velocidade > 110:
    valor = velocidade - 110
    multa = 5
    total = valor * multa
    print("Você foi multado!")
    print ("Multa: ", f'R${total:.2f}' )
else:
    print("Está dentro dos limites de velocidade!")
