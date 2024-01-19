import random

class Board:
    """
    This is a class that will create the board, size of the board, and keep track of hits/misses, as well as the player name/computer
    """

    def __init__(self, board_size, whos_playing, type):
        self.board_size = board_size
        self.whos_playing = whos_playing
        self.type = type

    #We will use the below function to set up the two boards 
    
    def print_board(self, miss_ship, hit_ship, boat_player):
        place = 0
        print("__________________")
        print(f"\n{self.whos_playing}'s board\n")
        print("__________________")
        print("     0  1  2  3  4")
        for point in range(5):
            row = ""
            for y in range(5):
                ch = " _ "
                if self.type == "Type A" and place in miss_ship_player:
                    ch = " x "
                elif self.type == "Type B" and place in miss_ship_computer:
                    ch = " x "
                elif self.type == "Type A" and place in hit_ship_player:
                    ch = " o "
                elif self.type == "Type B" and place in hit_ship_computer:
                    ch = " o "
                elif self.type == "Type A" and place in boat_player:
                    ch = " @ "
                elif self.type == "Type B" and place in boat_computer:
                    ch = " @ "
                row = row + ch
                place = place + 1
            print(point, " ", row)
   
# Our function to get the player name    
def get_player_name():
    trigger = "off"
    while trigger == "off":
        try:
            name_not_capitalized = input("What is your name, please use three letters only. ")
            if len(name_not_capitalized) > 3 or len(name_not_capitalized) < 3:
                raise ValueError("Wrong amount of characters, try again! ")
            elif name_not_capitalized.isalpha():
                name = name_not_capitalized.capitalize()
                return name
                trigger = "on"
        except ValueError as e:
            print("Error:", e)

#This is the function to get the ships on the board 
def print_boats(boat):
    random_numbers = random.sample(range(0, 24), 2)
    boat.extend(random_numbers)
                
#This is our functuon to get the players hit 

def get_hit(hit_ship_player, miss_ship_player, boat_player):
    while True:
        try:
            ro = input("\nPlease select a row? ")
            row = int(ro) 
            if row in range(0,5):
                break
            elif row not in range(0,5):
                print("\nThat's off the board!")
        except ValueError as e:
            print("\nPssst, it's meant to be a number!")
    while True:
        try:
            co = input("\nPlease select a column? ")
            column = int(co) 
            if column in range(0,5):
                break
            elif column not in range(0,5):
                print("\nThat's off the board!")
        except ValueError as e:
            print("\nHey now, it's meant to be a number!")
    return (row * 5) + column

#This is our function to have the players turn 
def player_turn(hit_ship_player, miss_ship_player, boat_player):
    player_hit = "n"
    player_hit = get_hit(hit_ship_player, miss_ship_player, boat_player)
    while True:
        #This will check if the guess is in these lists, if it is we need to guess again
        if player_hit in hit_ship_player or player_hit in miss_ship_player:
            print("Looks like you had that guess!")
            player_hit = get_hit(hit_ship_player, miss_ship_player, boat_player)
        else:
            return player_hit
            break
        
        
#This will get the computer's guess 
def computer_guess(computer_poss_guesses):
    computer_hit = random.choice(computer_poss_guesses)
    computer_poss_guesses.remove(computer_hit)
    return computer_hit

#This wll check if the guess hit a boat, if it does it's added to hit, if not it's a miss 
def check(miss, hit, boat, result):
    if result in boat:
        boat.remove(result)
        hit.append(result)
    else:
        miss.append(result)      
        
#This is our function to check for the winner        
def check_winner(boat_player, boat_computer):
    if len(boat_computer) == 0 and len(boat_player) == 0:
        print("\nAll ships are down,  it's a tie! ")
        return True 
    elif len(boat_computer) == 0:
        print("\nYour ships are down, computer wins! ")
        return True 
    elif len(boat_player) == 0:
        print("\nComputer's ships are down, you win! ")  
        return True 
    else:
        return
    
#RThis is to let the player know where the scores were
def print_hits(result, miss, hit, player):
    if result in hit:
        print(f"\n{player} guessed {result}, it was a hit!" )
    elif result in miss:
        print(f"\n{player} guessed {result}, it was a miss" )
    
       
#These are the lists for the player 
miss_ship_player = []
hit_ship_player = []
boat_player = []

#These are the lists for the computer
miss_ship_computer = []
hit_ship_computer = []
boat_computer = []

#This is the list so we can keep track of the computers guesses 
computer_poss_guesses = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]



def main():
    global miss_ship_player, hit_ship_player, boat_player, miss_ship_computer, hit_ship_computer, boat_computer, computer_poss_guesses
    #get name 
    turns = 10
    print("\nWelcome to the Battleship Game!")
    print("You will play against the computer. Here are the rules:")
    print("1. You and the computer each have a fleet of ships, five each!.")
    print("2. Your goal is to sink all of the computer's ships before yours are sunk.")
    print("3. The game is played on a 5x5 board.")
    print("4. Ships are represented by '@'. Misses are marked with 'x', and hits are marked with 'o'.")
    print("You each have five ships!")
    print("5. You and the computer will take turns guessing the coordinates to attack.")
    print("6. Enter row and column numbers when prompted to make a guess.")
    print("7. The game ends when either all your ships or the computer's ships are sunk, or a draw!.")
    print("8. You have 10 turns to defeat the computer. Use them wisely!")
    print("\nNow we've got that out of the way, ships ahoy!\n")
    player_name = get_player_name()
    game_board = Board(5, "Computer", "Type A")
    player_print_boats = print_boats(boat_player)
    game_board.print_board(miss_ship_player, hit_ship_player, boat_player)
    
    #Get computer's game board 
    comp = Board(5, player_name, "Type B")
    computer_print_boats = print_boats(boat_computer)
    comp.print_board(miss_ship_computer, hit_ship_computer, boat_computer)
    print(f"Here is miss ship: {miss_ship_player}\nHere is hit ship {hit_ship_player}\nHere is player boat: {boat_player}")
    print(f"Here is miss ship comp: {miss_ship_computer}\nHere is hit ship comp {hit_ship_computer}\nHere is comp boat: {boat_computer}")
    print(f"\nTurns: {turns}")
    for x in range(0, 10):

        
        turns -= 1
        result = player_turn(miss_ship_player, hit_ship_player, boat_computer)
        result_computer = computer_guess(computer_poss_guesses)
        
        check(miss_ship_player, hit_ship_player, boat_computer, result)
        check(miss_ship_computer, hit_ship_computer, boat_player, result_computer)
        
        game_board.print_board(miss_ship_player, hit_ship_player, boat_player)
        comp.print_board(miss_ship_computer, hit_ship_computer, boat_computer)
        print(f"Here is miss ship: {miss_ship_player}\nHere is hit ship {hit_ship_player}\nHere is player boat: {boat_player}")
        print(f"Here is miss ship comp: {miss_ship_computer}\nHere is hit ship comp {hit_ship_computer}\nHere is comp boat: {boat_computer}")
        print(f"\nTurns: {turns}")

        print_hits(result_computer, miss_ship_computer, hit_ship_computer, "Computer")
        print_hits(result, miss_ship_player, hit_ship_player,player_name)
        if  check_winner(boat_player, boat_computer):
            while True:
                try:
                    play_again = input("\nThat's the game! Would you like to play again?\nHit y to play again, or n to quit! ") 
                    if play_again == "y":
                        miss_ship_player = []
                        hit_ship_player = []
                        boat_player = []
                        
                        #These are the lists for the computer
                        miss_ship_computer = []
                        hit_ship_computer = []
                        boat_computer = []
                        
                        #This is the list so we can keep track of the computers guesses 
                        computer_poss_guesses = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
                        main()
                    elif play_again == "n":
                        print("Goodbye! ")
                        return False 

                except ValueError:
                    print("Please enter a valid choice! ")
        if turns == 0:
                
            while True:
                try:
                    play_again = input("\nThat's the game, shame it ended in a draw, why don't you play again!\nHit y to play again, or n to quit! ") 
                    if play_again == "y":
                        miss_ship_player = []
                        hit_ship_player = []
                        boat_player = []
                        
                        #These are the lists for the computer
                        miss_ship_computer = []
                        hit_ship_computer = []
                        boat_computer = []
                        
                        #This is the list so we can keep track of the computers guesses 
                        computer_poss_guesses = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
                        main()
                    elif play_again == "n":
                        print("Goodbye! ")
                        return False 

                except ValueError:
                    print("Please enter a valid choice! ")

    
    
main()








