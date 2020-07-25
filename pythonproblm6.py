""""
Guess The number
Generate a random integer from a to b.
 You and your friend have to guess a number between two numbers a and b.
 a and b are inputs taken from the user. Your friend is player 1 and plays first.
He will have to keep choosing the number and your program must tell whether the number is greater
than the actual number or less than the actual number. Log the number of trials it took your friend
to arrive at the number. You play the same game and then the person with minimum number of trials wins!

Randomly generate a number after taking a and b as input and don’t show that to the user (say 6)

Input:

Enter the value of a

4

Enter the value of b

13

Output:

Player1 :

Please guess the number between 4 and 13

5

Wrong guess a greater number again

8

Wrong guess a smaller number again

6

Correct you took 3 trials to guess the number

Player 2:

.

.

.

Correct you took 7 trials to guess the number

Player 1 wins!

"""
import random
def checkNumber(num,rnum):
    """"
    It is a function which prints wheather the number you entered is less than or greater than the number
    """
    if num>rnum:
        print("The number u choosed is greater then magic number")
    elif num==rnum:
        print("Your guess is correct")
        return 1
    else:
        print("The number u choosed is lower than the magic number")
    return 0

def gamePlay(player,playerchances = 0):
    """"
    this function takes  player chance and get playerchances
    it will return how many chances it took to win by the player...
    """
    print(player)

    while True:
        playerchances= playerchances + 1
        guess = int(input("Guess the number\n"))
        val = checkNumber(guess, magicnumber)
        if val == 1:
            print("You Won ")
            print(f"It took you {playerchances} chance to win")
            break
    return playerchances


num1 = int(input("Enter the minimum number\n"))
num2 = int(input("Enter the maximum number\n"))
magicnumber = random.randint(num1,num2)

p1 = gamePlay("Player1")
p2 = gamePlay("Player2")
if p1 >p2:
    print("Player One Wins!")
elif p1 == p2:
    print("The match ties...")
else:
    print("Player 2 Wins!")






