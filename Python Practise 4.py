""""
Author: Bablu bambal
Date: 24 July 2019
Desciption : "A python Practise for thee python"
Python Practice problem 4 (Easy, 10 points)

The Next Palindrome

Problem Statement

A palindrome is a string which when reversed is equal to itself:

Examples of palindrome includes 616, mom, 676, 100001

You have to take a number as an input from the user. You have to find the next palindrome corresponding to that number. Your first input should be ‘number of test cases’ and then take all the cases as input from the user



Input:

3

451

10

2133



Output:

Next palindrome for 451 is 454

Next palindrome for 10 is 11

Next palindrome for 2133 is 2222


"""

def findnextpalindrome(number):
    i = int(number)
    while True:

        if str(i) == str(i)[::-1]:
            print(f"The Next palindrome is :{i} ")
            break
        i = i+1


print("To find the Palindrome of the strings")
number = int(input("Enter the number items:"))
list = []
for i in range(number):
      item = input("Enter the number for finding next palindrome:")
      list.append(item)

for item in list:
    # print(item)
    findnextpalindrome(item)