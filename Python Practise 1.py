""""
Author: Bablu bambal
Date: 23 July 2019
Desciption : "A python Practise for thee python"

Python Practice problem 1 (Easy, 10 points)
Your Age In 2090
Take age or year or birth as an input from the user and tell
them when they will turn 100 years old.(5 points)
 Don’t use any type of module like datetime or dateutils(-5 points).

They can then optionally provide a year and your program must tell their age in that particular year.
 (3 points) You should be handling all sorts of errors like (2 points):
You are not yet born
You seem to be the oldest person alive
You can also handle any other error if possible!
"""
print("Welcome to Your age in 2090")
yearnow = 2020
isage = False

def age(age):
    print(isage)
    if isage:
        age100 = 100 - age
        yearWhen100 = yearnow + age100
    else:
        agenow = 2020 - age
        age100 = 100 - agenow
        yearWhen100 = yearnow + age100

    print(f"Your will be 100 years in year {yearWhen100}")


if __name__ == '__main__':
    while True:
        try:
            ageyear = int(input("Enter you age"))
            break

        except Exception as e:
            print("Your age is not integer Please type an Int not a string")
    if ageyear > 1000:
        isage = False
        age(ageyear)
    elif ageyear > 100:
        print("It seems you are the oldest person alive")
    elif ageyear < 100:
        isage = True
        age(ageyear)
    print("Want to know how much is your age in a particluar year")
    year = int(input("Year:"))
    no_of_year = year-yearnow
    if no_of_year < 0:
        print("You cant decrease your age u must enter greater than 2020")
    else:
        if isage:
            age = ageyear+no_of_year
        else:
            age = (yearnow-ageyear)+no_of_year
        print(f"YOur will be {age} years in {year}")










