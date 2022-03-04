contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = {'cachorro', 'gato', 'elefante'}
print(contador_letras(lista_animais))

soma = lambda a, b: a + b

print(soma(5, 2))

calculadora = {
    'soma': lambda a, b: a + b,
    'sub': lambda a, b: a - b,
    'mul': lambda a, b: a * b,
    'div': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
print(soma(56, 23))