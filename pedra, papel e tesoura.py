import random

def play():
    user = input("faça sua escola, utilize apenas:\nPedra, papel ou tesoura\n")
    escolhas = ['pedra', 'papel', 'tesoura']
    computer = random.choice(escolhas)
    print
    print ('escolha do computador foi {}'.format(computer))
    if user == computer:
        return 'Empate'

    # pedra > tesoura, tesoura > papel, papel > pedra
    if is_win(user, computer):
        
        return '\n\033[32mVocê ganhou' #\n\033[31m imprime em uma cor (33m) = verde
        

    return '\n\033[31mVocê perdeu' #\n\033[31m imprime em uma cor (31m) = vermelho

def is_win(player, opponent):
    # return true se o jogador ganhou
    if (player == 'pedra' and opponent == 'tesoura') or (player == 'tesoura' and opponent == 'papel') \
        or (player == 'papel' and opponent == 'pedra'):
           
            return True
        
        
print(play())

