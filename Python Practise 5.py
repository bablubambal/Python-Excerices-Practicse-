""""
Author: Bablu bambal
Date: 24 July 2019
Desciption : "A python Practise for thee python"

Palindromify The List
You are given a list which contains some numbers.
 You have to print a list of next palindromes
  only if the number is greater than 10 otherwise you will print that number.

Input:

[1, 6, 87, 43]

Output:

[1, 6, 88, 44]
"""

##plaindorme the list
def findnextpalindrome(number):
    """"
    In this string is taken as the input which is converted to integer and
     and returns the next future palindrome number
    """
    i = int(number)
    while True:

        if str(i) == str(i)[::-1]:
            #print(f"The Next palindrome is :{i} ")
            return i
        i = i+1
#plaindromifing the list


# taking input a string from the user seperated by space
lis = input("Enter the list elements seperated by space\n")
#spliting the string by spaces to get the numbers as a string
lis = lis.split(" ")
print(f"list  {lis}")
l1 = []
for item in lis:
    if int(item)<10:
        l1.append(item)
        continue
    i = findnextpalindrome(item)
    l1.append(i)

print(int(l1))

