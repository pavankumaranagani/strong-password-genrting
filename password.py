import random

print('Welocome To Your Passwords Generator')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$&1234567890'

number = input('Amount Of Password to generate: ')

number = int(number)

length = input('Input Your Password length: ')
length = int(length)

print('\nhere are your passwords: ')

for pwd in range(number):
    password = ''
    for c in range(length):
      password += random.choice(chars)
    print(password)    
      