print('Este es el archivo de Flotantes!')

x = 3.3
print(x)
y = 1.1 + 2.2
print(y)

print(x == y)

# print(round(y, 2)) RETORNA 3.3 

y_str = format(y, '.2')
print('str =>',y_str)
print(y_str == str(x))

print('-' * 50)

print(x, y)
tolerance = 0.00001
print(abs(x - y) < tolerance)