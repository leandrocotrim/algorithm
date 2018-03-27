from random import randint
from collections import defaultdict

dicC = defaultdict(int)
dicE = defaultdict(int)

while True:
    try:
        t = randint(3, 9)
        n = randint(2, 9)

        r = t * n

        ri = input('{} x {} = '.format(t, n))
        #rr = True if ri == 'sair' else False
        if ri == 'sair': break

        if r == int(ri):
            print('Correto - {} x {} = {}'.format(t, n, r))
            dicC[t] = dicC[t] + 1
            dicC[n] = dicC[n] + 1        
        else:
            print('ERRADO - {} x {} = {}'.format(t, n, r))
            dicE[t] = dicE[t] + 1
            dicE[n] = dicE[n] + 1
    except:
        print('Erro ao digitar')

print('')
for d in dicE:    
    print('Tabuada do {}, errou {} vezes'.format(d, dicE[d]))
print('')
for d in dicC:    
    print('Tabuada do {}, acertou {} vezes'.format(d, dicC[d]))
print('')
print('Total de erros {}, Total de acerto {}.'.format(sum(dicE.values()), sum(dicC.values())))