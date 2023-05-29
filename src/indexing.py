print('Este es el archivo de Indexing!!!')

text = 'El sabe Python'
print(text[0])
print(text[1])
# print(text[999]) <---- error
size = len(text)
print('size =>', size)
print(text[size - 1])
print(text[-1])

# SLICING

print(text[0:5])
print(text[8:14])
# si no le enviamos nada, python reconoce el inicio en 0 
print(text[:10])
print(text[5:-1])
# si no le enviamos nada, python reconoce el final 
print(text[5:])
# si no le enviamos nada, python reconoce el inicio y el final
print(text[:])
# SALTOS
print(text[8:14:2])
print('Va del inicio al final haciendo saltos de a 2 =>',text)
print('Resultado =>',text[::2])