# This code intend to recreate the game "Vache taureau" that i used to play with my friends
# Hope it doesnt produces any more bugs hh  , ENJOY !
import random 
random_number = ""
random_table_digit =[]

# Create the computer number that we are trying to guess
while len(random_number)<4 :
    random_digit = random.randint(1,9)
    if str(random_digit) not in random_table_digit :
        random_number += str(random_digit)
        random_table_digit += str(random_digit)
# Print instructions for player
def print_instructions():
    print("  ^__^")
    print(" (oo)\\_______")
    print(" (__)\       )\\/\\")
    print("     ||----w |")
    print("     ||     ||")
    print("                                           ")
    """Print the game instructions."""
    print("------------------------------GAME INSTRUCTIONS------------------------------")
    print('*' * 100)
    print("Taureau, Vache is a game where you try to guess a 4-digit number.")
    print("The number is composed of distinct digits ranging from 1 to 9 (zero not included).")
    print("You have a unlimited number of chances to guess the right number.")
    print("After each guess, you will receive feedback:")
    print("- If a digit is in the correct place, you get +1 Taureau.")
    print("- If a digit exists in the number but is not in the correct place, you get +1 Vache.")
    print("Try to guess the number with 4 Taureaux to win!")
    print("Let's get started! Enjoy the game.")
    print("NOTE : if you want to leave just press 'Ctrl+C' ")
    print('*' * 100)

# Condtions on inserted number
#chech if a digit is repeated function 
def CheckRepeatedElement(number):
    table = []
    for i in range(len(number)):
        table += number[i]
    for i in range(len(table)):
        repetition = 0
        for j in range(len(table)):
            if number[i] == number[j] : 
                repetition += 1 
        if repetition > 1 :
            print("The number containes a repeated digit")
            return True
    return False
# choose a number function 
def Choose():
    player_number = ""
    user_table_digit = []
    
    while (len(player_number)<4) or( repeated_elemnt == True) or (zero_detected == True ) :
        repeated_elemnt = True
        zero_detected = True
        # check length of number
        player_number = input("Choose your number ")
        if len(player_number)<4:
            print("Number too short")
        # check if number contains 0 
        if "0" not in player_number:
            zero_detected = False
        else : print("Number contains a zero")
        # divide the number into digits in a table 
        for i in range(4):
            if i < len(player_number):
                user_table_digit += player_number[i]
        # check if the number contains any repeated digits 
        repeated_elemnt = CheckRepeatedElement(player_number)     
    return player_number  , user_table_digit 


            
# Compare number and results
def main():

    print_instructions()
    user_win = False
    while user_win == False :
        taureau = 0
        vache = 0
        returned =  Choose()
        player_number = returned[0]
        user_table_digit = returned[1]
        if player_number == random_number:
            user_win = True
            print("yahou ! you won")
            break
        for i in range(4):
            if random_table_digit[i] == user_table_digit[i]:
                taureau += 1 
            elif (random_table_digit[i] in user_table_digit) and (random_table_digit[i] != user_table_digit[i]):
                vache +=1
        print(f"Taureau = {taureau} , Vache = {vache}")
        print("Try again")
            
if __name__ == "__main__":
    try:
        main()          
    except KeyboardInterrupt:
        print("\nGame interrupted. Exiting...")
