import random
from flask import Flask

print('=' * 30)
print('ROLETA RUSSA')
print('=' * 30)


revolver = [1, 2, 3, 4, 5, 6]
roleta = random.choice(revolver)
jogador = int(input('Escolha um número de 1 até 6: '))

if jogador == roleta:
    print('Você morreu :)')
elif jogador != roleta:
    print('Você sobreviveu')
print('FIM')

#escolha = print('Quer tentar de novo? [Y/N]').upper
#if escolha == 'Y':
    
#else:
#    print('O jogo acabou!')
        


