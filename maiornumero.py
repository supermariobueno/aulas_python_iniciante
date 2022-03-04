a = int(input('Primeiro Valor: '))
b = int(input('Valor dois: '))
c = int(input('Terceiro valor: '))

if a > b and a > c:
    print('O maior número é: {}' .format(a))
elif b > a and b > c:
    print('O maior número é: {}' .format(b))
else:
    print(('O maior número é {}' .format(c)))
print('Fim do programa')

