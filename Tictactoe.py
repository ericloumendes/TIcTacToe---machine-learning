import os

#ID Number = Unplayed spot / ID X = Player 1 play / ID O = Player 2 play
plays = [[1, 2, 3],
        [ 4, 5, 6],
        [ 7, 8, 9]]

#ID 0 = Player 1 / ID 1 = Player 2
CurrentPlayer = 0

#This function is responsable for draw the current game in the console
def DrawGame():
    print('     |     |     ')    
    print(f'  {plays[0][0]}  |  {plays[0][1]}  |  {plays[0][2]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {plays[1][0]}  |  {plays[1][1]}  |  {plays[1][2]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {plays[2][0]}  |  {plays[2][1]}  |  {plays[2][2]}  ')
    print('     |     |     ')
    print('')


def MakeAPlay():
    global CurrentPlayer

    play = int(input('Make a play: '))
    while play < 1 or play > 9:
        play = input('Make a play: ')

    if CurrentPlayer == 0:
        plays[int((play-1)/3)][(play-1)%3] = 'X'
        CurrentPlayer = 1

    else:
        plays[int((play-1)/3)][(play-1)%3]  = 'O'
        CurrentPlayer = 0


    #This command clear the terminal leaving only the draw of the current game
    os.system('cls' if os.name == 'nt' else 'clear')

    DrawGame()


#Keeps playing the game until all possible plays are filled
def Game():
    for i in range(9):
        if i != 'X' or i != 'O':
            MakeAPlay()
            VerifyWin()
            continue
        break

    print("It's a tie!")
    

def VerifyWin():
    for line in plays:
        if len(set(line)) == 1:
            print(f'O Jogador {str(set(line))} ganhou!')
            return
    for i in range(3):
        if plays[0][i] == plays[1][i] == plays[2][i]:
            print(f'O Jogador {plays[0][i]} ganhou!')
            return
    
    k = 1

    if plays[k][k] in ['X', 'O']:
        if plays[k+1][k-1] == plays[k-1][k+1] == plays[k][k]:
            print(f'O Jogador {plays[k][k]} ganhou!')
            return
        elif plays[k-1][k-1] == plays[k][k] == plays[k+1][k+1]:
            print(f'O Jogador {plays[k][k]} ganhou!')
            return


Game()
