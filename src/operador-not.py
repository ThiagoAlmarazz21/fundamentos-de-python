print('Este es el archivo de Operador Not!!!')

print('"True"' ,not True)
print('"False"' ,not False)

print('NOT AND')
print('True "and" True =>', not (True and True))
print('True "and" False =>', not (True and False))
print('False "and" True =>', not (False and True))
print('False "and" False =>', not (False and False))

# AHORA LA OPERACION ESTÁ NEGADA, OSEA QUE LOS NUMEROS TIENEN QUE ESTAR FUERA DEL RANGO DE 100 Y 1000 PARA QUE DE "TRUE"
num = int(input('Ingrese un numero: '))
print(not (num >= 100 and num <= 1000))