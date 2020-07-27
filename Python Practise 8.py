""""
Author: Bablu Bambal
Date : 26 July 2019
Purpose: "To practise the python problem"

Python Practice problem 8 (Easy, 10 points)
Rohan Das Is A Fraud:

Rohan das is a fraud by nature.

Rohan Das wrote a python function to print a multiplication table of a given number and put one of the values (randomly generated) as wrong.

Rohan Das did this to fool his classmates and make them commit a mistake in a test. You cannot tolerate this!

So you decided to use your python skills to counter Rohan’s actions by writing a python program that validates Rohan’s multiplication table.

Your function should be able to find out the wrong values in Rohan’s table and expose Rohan Das as a fraud.


Note: Rohan’s function returns a list of numbers like this



Rohan Das’s Function Input:

rohanMultiplication(6)



Rohan’s function returns this output:

[6, 12, 18, 26, …., 60]

You have to write a function isCorrect(table, number) and return the index where rohan’s function is wrong and print it to the screen! If the table is correct, your function returns None.


"""
def rohantable(number):
    import random
    wrong = random.randint(0,9)
    table = [i*number for i in range(1,11)]
    table[wrong] = table[wrong]+random.randint(0,9)
    return table
def isTCorrect(table,number):
    for i in range(1,11):
        if table[i-1] != i*number:
            return i-1
    return None

def rohanMultiplication(number):
     """
     It return  a table with the multiplication table list

     :param number:  number
     :return:  A list of number showing the table
     """
     import random
     randomvar = random.randint(1,10)
     randnumber = random.randint(number,number*10)
     multable = []
     for i in range(1,11):
         if randomvar == i:
             print(f"{number} X {i} = {randnumber}")
             multable.append(randnumber)

             continue
         print(f"{number} X {i} = {number*i}")
         multable.append(number*i)
     return multable

def isCorrect(multiplicationlist,number):
    mul = []
    for i in range(1, 11):
        if i>=10:
            break
        mul.append(number*i)
        if  multiplicationlist[i-1] != mul[i-1]:
            print(f"the erroe index is {i-1} and at the place of {i}")

    print(mul)






tableinput = int(input("Enter the number to get table"))

rohantable = rohanMultiplication(tableinput)

print(rohantable)
print("Do you want to check the Correct table press 1")
choice = int(input())
if choice ==1:
    isCorrect(rohantable,tableinput)
