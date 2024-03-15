
num1 = int(input("Insira um número: "))

if num1 % 42 == 0:
    print ('resposta para tudo')
    
elif num1 % 3 == 0 and num1 % 5 == 0:
    print ('fizzbuzz')
    
elif num1 % 3 == 0:
    print('fizz')

elif num1 % 5 == 0:
    print ('buzz')

else: print (num1)
