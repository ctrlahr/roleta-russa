from random import choice
numeros = [1, 2, 3, 4, 5, 6]
def linha(l):
    print('-' * 25)
    return l

linha(linha)
print('     ROLETA RUSSA     ')
linha(linha)


while True:
# ESCOLHA DA ROLETA
    revolver = choice(numeros)
# DEFININDO OQ ACONTECE SE O NÚMERO FOR MAIOR QUE 6 OU MENOR QUE 1
    try:
        jogador = int(input('Escolha um número entre 1 e 6: '))
        if jogador > 6 or jogador < 1:
            print('Escolha um número entre 1 e 6 seu animal!')
            continue

# SE O JOGADOR PERDEU
        if jogador == revolver:
            print('você perdeu!')
            escolha = str(input('Quer tentar dnv? [S/N]: ')).upper()[0]
            if escolha == 'Y':
                continue
            elif escolha == 'N':
                print('Parabéns você saiu vivo! :)')
                break
            
# SE O JOGADOR GANHOU
        elif jogador != revolver:
            print('Você ganhou!')
            escolha2 = str(input(('Quer tentar morrer dnv? [S/N]: '))).upper()[0]
            if escolha2 == 'Y':
                continue
            elif escolha2 == 'N':
                print('Você saiu vivo, parabéns! :)')
                break
    
    except:
        print('O valor digitado não é um número inteiro!!')            



