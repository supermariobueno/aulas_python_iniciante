a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input('Nota inválida. Digite uma nota válida: '))
b = int(input('Segundo Bimestre: '))
if b > 10:
    int(input('Nota inválida. Digite uma nota válida: '))
c = int(input('Terceiro Bimestre: '))
if c > 10:
    int(input('Nota inválida. Digite uma nota válida: '))
d = int(input('Quarto Bimestre: '))
if d > 10:
    int(input('Nota inválida. Digite uma nota válida: '))

media = (a + b + c + d) / 4

print(media)

if media >= 6:
    print('Aluno Aprovado')
elif media >=4:
    print('Aluno de Recuperação')
else:
    print('Aluno Reprovado')

print('Fim do programa')