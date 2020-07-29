
#11. Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s).#
print(sum.__doc__)

print("***********************************************\n\n")

#12. Write a Python program to print the calendar of a given month and year. Note : Use 'calendar' module.#

import calendar
y = int(input("Input the year : "))
m = int(input("Input the month : "))
print(calendar.month(y, m))

print("***********************************************\n\n")

#14. Write a Python program to calculate number of days between two dates. Sample dates : (2014, 7, 2), (2014, 7, 11)#
#14.1#
date1=(2014, 7, 2)
date2=(2014, 7, 11)
print("Number of days between 2 dates:", date2[2]-date1[2], "days")
#14.2#
from datetime import date
f_date = date(2014, 7, 2)
l_date = date(2014, 7, 11)
delta = l_date - f_date
print(delta.days)

print("***********************************************\n\n")

#15. Write a Python program to get the volume of a sphere with radius 6.#
from math import pi
r=6
volume=4/3 * pi * r**3
print("Volume of a sphere with radius 6 is {:.3f}".format(volume))

print("***********************************************\n\n")

#16. Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.#

num1=int(input("Input a number: "))
num2=17
if num1>num2:
    print("Double the absolute difference: ", 2*(num1-num2))
else:
    print("Difference between numbers: ", num2-num1)

print("***********************************************\n\n")

#17. Write a Python program to test whether a number is within 100 of 1000 or 2000.#

numb=int(input("Input a number over 100: "))
if 100<=numb<=1000:
    print("Your number is within 100 of 1000")
elif 1000<numb<=2000:
    print("Your number is within 1000 of 2000")
elif numb>2000:
    print("Your number is grater than 2000")   
else:
    print("Your number is smaller than 100")
    
print("***********************************************\n\n")

#18. Write a Python program to calculate the sum of three given numbers, if the values are equal then return three times of their sum#


numb1=int(input("Enter a number: "))
numb2=int(input("Enter a number: "))
numb3=int(input("Enter a number: "))
if numb1==numb2==numb3:
    print("Te numbers are equal! So three times of their sum is ",3*(numb1+numb2+numb3))
else:
    print("Sum of numbers: ", numb1+numb2+numb3)
   
print("***********************************************\n\n")

#19. Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.#

my_string=input("Input a string: ")
text_list=list(my_string.split(" "))
if text_list[0]=="Is":
    print( my_string)
else:
    text_list.insert(0,"Is")
    text2=" ".join(text_list)
    print(text2)
    
print("***********************************************\n\n")

#20. Write a Python program to get a string which is n (non-negative integer) copies of a given string.#

def copies_string(str1, n):
    mystr=""
    for i in range(n):
        mystr=mystr+str1
    return mystr  
    
   
print("***********************************************\n\n")
