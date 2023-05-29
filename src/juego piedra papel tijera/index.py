username = str(input('Cual es tu nombre? '))
print(f'Bienvenido al juego {username}!')

user = input('Elige una opcion: piedra, papel o tijera = ')
user = user.lower()
pc = 'piedra'

# user_win = print(f'{username} gana!')

if user == pc:
  print('Empate!')
elif user == 'piedra' and pc == 'tijera':
  print(f'{username} eligió "piedra"')
  print(f'{username} gana!')
elif user == 'papel' and pc == 'piedra':
  print(f'{username} eligió "papel"')
  print(f'{username} gana!')
elif user == 'tijera' and pc == 'papel':
  print(f'{username} eligió "tijera"')
  print(f'{username} gana!')
else: 
  print('Pc gana!')