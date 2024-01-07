from random import choice

print('=' * 30)
print('ROLETA RUSSA')
print('=' * 30)


revolver = [1, 2, 3, 4, 5, 6]
roleta = choice(revolver)
jogador = int(input('Escolha um número de 1 até 6: '))

while True:
    if jogador == roleta:
        resposta = str(input(('Você perdeu, quer tentar dnv? [Y/N]: '))).upper()[0]
        if resposta == 'N':
            break
            

#escolha = print('Quer tentar de novo? [Y/N]').upper
#if escolha == 'Y':
    
#else:
#    print('O jogo acabou!')
        


