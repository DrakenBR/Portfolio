import random

options = ('piedra', 'papel', 'tijera')

pc_wins = 0
user_wins = 0

round = 1

while True: 

  print('***' * 10)
  print('ROUND', round)
  print('***' * 10)

  print('Computador wins', pc_wins)
  print('User wins', user_wins)
  
  user_option = input('piedra, papel o tijera ? =>')
  user_option = user_option.lower()

  round += 1
  
  if not user_option in options:
    print('esa opcion no es valida')
    continue 
  
  pc_option = random.choice(options)
  
  print('User Option => ', user_option)
  print('PC Option => ', pc_option)
  
  if user_option == pc_option: 
    print('Empate!')
  elif user_option == 'piedra':
    if pc_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('pc gano!')
      pc_wins += 1
  elif user_option == 'papel':
    if pc_option == 'piedra':
      print('papel gana a piedra')
      print('user gano!')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('pc gano!')
      pc_wins += 1
  elif user_option == 'tijera':
    if pc_option == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('pc gano!')
      pc_wins += 1

  if pc_wins == 2:
    print('El ganador del juego es la computadora')
    break

  if user_wins == 2:
    print('El ganador del juego es el usuário')
    break