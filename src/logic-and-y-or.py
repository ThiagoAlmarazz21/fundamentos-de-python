print('Este es el archio de Operadores lógicos!!!')

# OPERADOR AND

print('Las 2 partes de la operacion tienen que ser verdaderas para que de "True"')
print('True "and" True =>', True and True)
print('True "and" False =>', True and False)
print('False "and" True =>', False and True)
print('False "and" False =>', False and False)

print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)

num = int(input('Ingrese un numero: '))

if num < 100 :
  print('Error: el numero que ingrese tiene que ser mayor o igual a 100')
elif  num > 1000 :
  print('Debe ingresar un numero menor a 1000')
else: 
  print(f'El número ingresado es {num}')

# OPERADOR OR

print('Si alguno de los 2 es verdadero, la operacion es "True"')
print('True "or" True =>', True or True)
print('True "or" False =>', True or False)
print('False "or" True =>', False or True)
print('False "or" False =>', False or False)

rol = input('Digite el rol: ')

if rol == 'admin' or rol == 'seller':
  print('Puede entrar a la página')
else: 
  print('"No puede ingresar a esta página, siga navegando por el inicio"')