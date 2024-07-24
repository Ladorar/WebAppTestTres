import random

#Guess the number correctly

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while(guess != random_number):
        guess = int(input(f'Guess a number between 1 and {x}: '))
        print(guess)
        if guess < random_number:
            print('Sorry, guess again, Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')
    print(f'Yay, congrats. You guessed the number {random_number} correctly!')

#Let the computer guess the number correctly

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while(feedback != 'c'):
        if low!= high:
            guess = random.randint(low, high)
        else:
            guess = low #Could also be high, because low=high
        feedback = input(f'Is {guess} too high (H), too low (L) or correct(C)??: ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'Yay the computer guessed your number {guess} correctly!!')

#Rock, Paper, Scissor

def rock_pape_sis(x):
    rounds = x
    played = 0
    player_win = 0
    com_win = 0
    draws = 0
    while(played < rounds):
        com_hand = ''
        rnd_hand = random.randint(1,3)
        if(rnd_hand == 1):
            com_hand = 'r'
        elif(rnd_hand == 2):
            com_hand = 'p'
        else:
            com_hand = 's'
        player_hand = input('Please Input your Hand. Rock(R), Paper(P) or Scissor(S): ').lower()
        if(com_hand == player_hand):
            draws += 1
            print(f'This was a draw! You and the computer choose {player_hand}')
        elif(com_hand == 'r' and player_hand == 's' or com_hand == 's' and player_hand == 'p' or com_hand == 'p' and player_hand == 'r'):
            com_win += 1
            print(f'You choose {player_hand} and the computer choose {com_hand}. Computer Wins!')
        else:
            player_win += 1
            print(f'You choose {player_hand} and the computer choose {com_hand}. Player Wins!')
        played += 1
    if(player_win > com_win):
        print(f'You won!! The Player won {player_win} to {com_win} and there were {draws} draw matches.')
    elif(player_win < com_win):
        print(f'You lost!! The Computer won {com_win} to {player_win} and there were {draws} draw matches.')
    else:
        print(f'The whole competition is a draw! Both player won {player_win} macthes and there were {draws} draw matches.')



class gameBoard:



    def __init__(self) -> None:
        self.board = []
        
        for x in range(9):
            spalte = []
            for x in range(9):
                spalte.append('O')
            self.board.append(spalte)

        #self.board = [['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O'], ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O', 'O']]
        self.player_turn = True
        self.game_over = False
    
    def printBoard(self):
        line = ''
        for x in range(9):
            line = f'{9-x}|'
            for y in range(9):
                line += self.board[x][y]
            line += '|'
            print(line)
        print('  123456789')


    def inserStone(self, spalte):
        for x in range(8,-1,-1):
            if (self.board[x][spalte-1] == 'O'):
                self.setStone(x,spalte-1)
                self.switchTurn()
                return True
        return False

    def setStone(self, reihe, spalte):
        if(self.player_turn == True):
            self.board[reihe][spalte] = 'X'
        else:
            self.board[reihe][spalte] = 'H'

    def switchTurn(self):
        if(self.player_turn == True):
            self.player_turn = False
        else:
            self.player_turn = True

    def checkWin(self):
        #Check Spalten
        for spalte in range(9):
            count_x = 0
            count_h = 0
            for reihe in range(9):
                if (self.board[reihe][spalte] == 'X'):
                    count_x +=1
                    count_h = 0
                elif(self.board[reihe][spalte] == 'H'):
                    count_h += 1
                    count_x = 0
                else:
                    count_x = 0
                    count_h = 0
                
                if(count_x == 4):
                    return 'player'
                elif(count_h == 4):
                    return 'com'

        #Check Reihen
        for reihe in range(9):
            count_x = 0
            count_h = 0
            for spalte in range(9):
                if (self.board[reihe][spalte] == 'X'):
                    count_x +=1
                    count_h = 0
                elif(self.board[reihe][spalte] == 'H'):
                    count_h += 1
                    count_x = 0
                else:
                    count_x = 0
                    count_h = 0
                
                if(count_x == 4):
                    return 'player'
                elif(count_h == 4):
                    return 'com'

        #Check Diagonal Spalte+ Reihe+
        for reihe in range(6):
            for spalte in range(6):
                if(self.board[reihe][spalte] == 'X' and self.board[reihe+1][spalte+1] == 'X' and self.board[reihe+2][spalte+2] == 'X' and self.board[reihe+3][spalte+3] == 'X'):
                    return 'player'
                elif(self.board[reihe][spalte] == 'H' and self.board[reihe+1][spalte+1] == 'H' and self.board[reihe+2][spalte+2] == 'H' and self.board[reihe+3][spalte+3] == 'H'):
                    return 'com'
        

        #Check Diagonal Spalte- Reihe +
        for reihe in range(6):
            for spalte in range(8,2,-1):
                if(self.board[reihe][spalte] == 'X' and self.board[reihe+1][spalte-1] == 'X' and self.board[reihe+2][spalte-2] == 'X' and self.board[reihe+3][spalte-3] == 'X'):
                    return 'player'
                elif(self.board[reihe][spalte] == 'H' and self.board[reihe+1][spalte-1] == 'H' and self.board[reihe+2][spalte-2] == 'H' and self.board[reihe+3][spalte-3] == 'H'):
                    return 'com'
                

        #Check for Draw
        count_o = 0
        for reihe in range (9):
            for spalte in range (9):
                if(self.board[reihe][spalte] == 'O'):
                    count_o +=1
        if(count_o == 0):
            return 'draw'

        return 'none'

    def runGame(self):
        while(self.game_over == False):
            self.printBoard()
            if(self.player_turn == True):
                insert_confirmed = False
                choice = int(input('It is your turn. Please place a piece by typing the column you want to inset it(1-9): '))
                while(insert_confirmed == False):
                    if(self.inserStone(choice) == False):
                        choice = int(input(f'There was no free space in column {choice}. Please select another column 1-9: '))
                    else:
                        print(f'Your piece was placed successfully in column {choice}')
                        insert_confirmed = True
            else:
                insert_confirmed = False
                while(insert_confirmed == False):
                    choice = random.randint(1,9)
                    if(self.inserStone(choice) == True):
                        print(f'The computer chose column {choice}.')
                        insert_confirmed = True
            winner = self.checkWin()
            if(winner == 'player'):
                print('Yay, you won!! Congratulations.')
                self.game_over = True
                self.printBoard()
            elif(winner == 'com'):
                print('Oh no, the computer won. Better Luck next time!')
                self.game_over = True
                self.printBoard()
            elif(winner == 'draw'):
                print('There are no open spots left. This game is a draw...')
                self.game_over = True
                self.printBoard()
                





tryc = gameBoard()
tryc.runGame()

