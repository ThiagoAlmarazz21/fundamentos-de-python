print('Este es el archivo de Strings!!!')

text = 'El sabe programar en Python'
# ESTO VA A BUSCAR SI LA PALABRA INGRESADA ESTÁ EN EL TEXTO O NO
print('Javascript' in text)
print('Python' in text)


if 'Python' in text:
  print('Elegiste bien!')
else: 
  print('Tambien elegiste bien!')


'''
leng = str(input('Elige tu lenguaje de programacion: '))
if leng == 'javascript':
  print('Elegiste bien, javascript es un lenguaje muy usado!')
elif leng == 'python':
  print('Buena eleccion, python es un buen lenguaje de backend')
else: 
  print('Debe ingresar algun lenguaje de programacion!')
'''
# METODO "len": examina el tamaño en el numero de caracteres y tambien cuenta los espacios
size = len('amor')
print('Metodo len()',size)

# METODO upper(): pasa todo el texto a mayuscula
print(text)
print(text.upper())

# METODO lower(): pasa todo el texto a minuscula
print(text)
print(text.lower())  

# METODO count(): cuenta el numero de apariciones que tiene una letra en especifico
print(text)
print('contando letras en especifico => a:', text.count('a'))

# METODO swapcase(): transforma un caracter minuscula a mayuscula y viceversa
print('METODO swapcase()')
print(text.swapcase())

# METODO startswith(): verifica si un texto inicia con algo en especifico
print('METODO startswith() y endswith()')
print(text.startswith('¿'))
print(text.endswith('?'))

# METODO replace(): reemplaza una cosa por otra
print('METODO replace()')
print(text.replace('Python', 'Go'))

# CAMBIO DE TEXTO 
text_2 = 'este es un ttulo'

# METODO capitalize(): Pone el primer caracter en mayus
print('METODO capitalize()')
print(text_2)
print(text_2.capitalize())

# METODO title(): pone el inicio de cada palabra en mayus
print('METODO title()')
print(text_2)
print(text_2.title())

# METODO isdigit(): nos dice si el texto es un digito
print('METODO isdigit()')
print(text_2)
print(text_2.isdigit())
print('234'.isdigit())