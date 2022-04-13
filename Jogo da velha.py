import random

def play():
    user = input("faça sua escola, utilize apenas:\nPedra, papel ou tesoura\n")
    escolhas = ['pedra', 'papel', 'tesoura']
    computer = random.choice(escolhas)
    print ('escolha do computador foi {}\n\033[31m'.format(computer)) 
    
    if user == computer:
        return 'Empate'

    # pedra > tesoura, tesoura > papel, papel > pedra.
    if is_win(user, computer):
        
        return 'Você ganhou'
        

    return 'Você perdeu'

def is_win(player, opponent):
    # return true se o jogador ganhou
    if (player == 'pedra' and opponent == 'tesoura') or (player == 'tesoura' and opponent == 'papel') \
        or (player == 'papel' and opponent == 'pedra'):
           
            return True
        
        
print(play())
