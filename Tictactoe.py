import os

#ID Number = Unplayed spot / ID X = Player 1 play / ID O = Player 2 play
plays = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#ID 0 = Player 1 / ID 1 = Player 2
CurrentPlayer = 0

#This function is responsable for draw the current game in the console
def DrawGame():
    print('     |     |     ')    
    print(f'  {plays[0]}  |  {plays[1]}  |  {plays[2]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {plays[3]}  |  {plays[4]}  |  {plays[5]}  ')
    print('_____|_____|_____')
    print('     |     |     ')
    print(f'  {plays[6]}  |  {plays[7]}  |  {plays[8]}  ')
    print('     |     |     ')
    print('')


def MakeAPlay():
    global CurrentPlayer

    play = input('Make a play: ')
    while int(play) < 1 or int(play) > 9:
        play = input('Make a play: ')

    if CurrentPlayer == 0:
        plays[int(play) - 1] = 'X'
        CurrentPlayer = 1

    else:
        plays[int(play) - 1] = 'O'
        CurrentPlayer = 0


    #This command clear the terminal leaving only the draw of the current game
    os.system('cls' if os.name == 'nt' else 'clear')

    DrawGame()


#Keeps playing the game until all possible plays are filled
def Game():
    for i in plays:
        if i != 'X' or i != 'O':
            MakeAPlay()
            continue
        break

    print("It's a tie!")


#def VerifyWin():
#    if plays[0] == 'X' and plays[1] == 'X' and plays[2] == 'X' or
#    plays[3] == 'X' and plays[4] == 'X' and plays[5] == 'X' or
#    plays[6] == 'X' and plays[7] == 'X' and plays[8] == 'X':


Game()
