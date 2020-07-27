""""
Author: Bablu bambal
Date: 23 July 2019
Desciption : "A python Practise for thee python"
Foods and Calories
You visit a restaurant called CodeWithHarry and food items in this restaurant
 are sorted based on their amount of calories.
  You have to reverse this list of food items containing their calories.

You have to use following three methods to reverse a list:

• Inbuilt method of python
• Listname[::-1] slicing trick
• Swapping first element with last one and second element with second last one and so on….
Input:
Take a list as an input from the user.
[5,4,1]

Output:
[1,4,5]
[1,4,5]
[1,4,5]
All the three methods give same results!
"""
print("List in the reverse sort using 3 methods")
no_of_element  = int(input("Enter the number of elements\n"))

listitems = []
for i in range(no_of_element):
    item = int(input("Enter the item in list : "))
    listitems.append(item)
print(listitems)
l = listitems.copy()
# i have sorted the list:
listitems.sort()
# method 1: reversing using the inbuilt method
l1= listitems.copy()
l1.reverse()
print("method1 ",l1)
# method 2: reversing the list using slcing
l2 = listitems[::-1]
print("method2 ",l2)
# method 3  reversing using swaping
lis = listitems.copy()

for i in range(int(len(lis)/2)):
    lis[i],lis[-(i+1)] = lis[-(i+1)],lis[i]
print("method3",lis)

if l1 is l2 is lis:
    print("All are same")
else :
    print("Not same")



