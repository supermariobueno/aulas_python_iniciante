 a = int(input('Valor 1: '))
 b = int(input('Valor 2: '))
 c = int(input('Valor 3: '))

 if a > b and a> c:
     print('O maior número é: {}' .format(a))
 elif b > a and b > c:
     print('O maior número é: {}' .format(b))
 else:
     print('O maior número é: {}' .format(c))

 print('Fim do programa')

 a = int(input('Valor 1: '))

 resto = a % 2

 if resto == 0:
     print('O número é par.')
 else:
     print('O número é ímpar')

 a = int(input('Valor 1: '))
 b = int(input('Valor 1: '))

 resto_a = a % 2
 resto_b = b % 2

 if resto_a == 0 or not resto_b > 0:
     print('Foi digitado um número par.')
 else:
    print('Nenhum número par foi digitado.')