first_name = 'Leandro'
last_name = 'Cotrim'

#parametros seguidos
print('Meu nome completo é {} {}'.format(first_name, last_name))

#parametros indexados
print('Meu último nome é {1}, e o primeiro é {0}'.format(first_name, last_name))

#parametros unpacking 
print('As letras do meu primeiro nome é {} {} {} {} {} {} {}'.format(*first_name))

#parametros com argurments names
obj = { 'first_name': first_name, 'last_name': last_name }
print('Meu nome completo é {first_name} {last_name}'.format(**obj))