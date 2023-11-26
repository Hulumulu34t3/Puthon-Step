print ('Привіт!')
name = input('Напиши своє ім\'я')
print(f'Привіт', name)
country = input('З якої ти країни:')
if country == 'Україна':
    print('Привіт земляче!')
elif country == 'Білорус':
    print('Вийди геть з України')
elif country == 'England':
    print('Hello, Welcom to Ukraine ')
else:
    print('Вітаю в Україні!')
age = int(input('Скільки вам років:'))
if (age > 0) and (age < 12):
    print( 'Ви дитина')
elif (age > 11) and (age < 16):
    print('Ви підліток')
elif (age > 16) and (age < 25):
    print('Ви доросла людина')
elif (age > 25) and (age < 44):
    print('Ви молода людина')
elif (age > 44) and (age < 60):
    print('Ви  людина середнього віку')
elif (age >65 ) and (age < 90):
    print('Ви  людина похилого віку')
