import random

def play():
    user = input("faça sua escola, utilize apenas:\nPedra, papel ou tesoura\n")
    computer = random.choice(['pedra', 'papel', 'tesoura'])

    print ('escolha do computador foi {}'.format(computer))
    if user == computer:
        return 'Empate'

    # pedra > tesoura, tesoura > papel, papel > pedra
    if is_win(user, computer):
        
        return '\n\033[32mVocê ganhou' #\n\033[31m imprime em uma cor (33m) = verde
        
    else:
        return '\n\033[31mVocê perdeu' #\n\033[31m imprime em uma cor (31m) = vermelho

def is_win(user, opponent):
    # return true se o jogador ganhou
    if (user == 'pedra' and computer == 'tesoura') or (user == 'tesoura' and computer == 'papel') \
        or (user == 'papel' and computer == 'pedra'):
           
            return True
        
        
print(play())

