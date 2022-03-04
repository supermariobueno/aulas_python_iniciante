conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}
conjuntouniao = conjunto.union(conjunto2)
print('União: {}' .format(conjuntouniao))
conjunto_inter = conjunto.intersection(conjunto2)
print(conjunto_inter)
conjunto_dif = conjunto.difference(conjunto2)
print(conjunto_dif)
conjunto_dif2 = conjunto2.difference(conjunto)
print(conjunto_dif2)
conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print(conjunto_dif_simetrica)

list = ('cachorro', 'gato', 'gato', 'elefante')
conjunto_animais = set(list)
print(conjunto_animais)