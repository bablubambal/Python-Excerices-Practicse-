""""
Author: Bablu Bambal
Date : 27 July 2019
Purpose: "To practise the python problem"


Funny Names

Its result day at school and not everyone is happy.
You decided to make your friends laugh by jumbling their names to come up with some funny names.

Your program should take the number of names and the names separated by space as input.
Output should be funny names in the same order.

Input:
Enter number of friends:
3
Enter the name of your 3 friends:
Rohan Das
Shubham Agarwal
Ritesh Arora

Output:
Ritesh Das
Shubham Arora
Rohan Agarwal
"""
print("\n \t Funny Names : \n")
number = int(input("Enter the number os friends:\n"))
lis =[]
for i in range(number):
    item = input("Enter the name \n")
    if " " in item:
        item = item.split(" ")
    lis.append(item)
print(lis)
import random
for i in range(len(lis)):
    lis[i][1] = lis[random.randint(0,number-1)][1]

# lis = lis.join(" ")
print(lis)
