print('Este es el archivo del condicional "if"')

if True:
  print('Deberia ejecutarse')

if False: 
  print('Nunca se ejecuta')


pet = input('¿Cual es tu mascota favorita? ')

if pet == 'perro':
  print('Genial, tienes buen gusto!')
elif pet == 'gato': 
  print('Espero tengas suerte')
else:
  print('Debes ingresar "perro" o "gato"')


stock = int(input('Ingrese un número de stock: '))

if stock >= 100 and stock <= 1000:
  print(f'El stock es correcto, su valor: "{stock}"')
else: 
  print('Por favor ingrese un valor entre 100 y 1000')


# PROGRAMA PARA SABER SI UN NÚMERO ES PAR O IMPAR
num = int(input('Ingrese un valor para saber si es par o impar: '))

if num % 2 == 0:
  print('El número es PAR')
else: 
  print('El número es IMPAR')