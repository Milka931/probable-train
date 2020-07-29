
#1. Write a Python program to print the following string in a specific format (see the output). Go to the editor/Sample String : "Twinkle, twinkle, little star, How I wonder what you are! Up above the world so high, Like a diamond in the sky. Twinkle, twinkle, little star, How I wonder what you are" Output :

#Twinkle, twinkle, little star,#
	#How I wonder what you are! #
		#Up above the world so high,  # 		
                    #Like a diamond in the sky. #
#Twinkle, twinkle, little star, #
	#How I wonder what you are#


print("Twinkle, twinkle, little star,\n\tHow I wonder what you are!\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky.\nTwinkle, twinkle, little star,\n\tHow I wonder what you are")

print("***************************************\n\n")

#2. Write a Python program to get the Python version you are using.#
import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)

print("***************************************\n\n")

#3. Write a Python program to display the current date and time.#
import datetime
now=datetime.datetime.now()
print("Currend date and time: ")
print(now.strftime("%Y-%m-%d %H:%M:%S"))

print("***************************************\n\n")

#4. Write a Python program which accepts the radius of a circle from the user and compute the area.#
from math import pi
radius= float(input("Enter radius of a circle: "))
print("Area of a circle: {:.3f}" .format(pi* radius**2))

print("***************************************\n\n")

#5. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them."#

fname=(input("Enter your first name: "))
lname=(input("Enter your last name: "))
print("Hello",lname,fname)

print("***************************************\n\n")

#6. Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers. #

numbers=(input("Enter numbers - separate them with comma: "))
print("List of numbers: ", list(numbers.split(",")))
print("Tuple of numbers: ", tuple(numbers.split(",")))

print("***************************************\n\n")

#7. Write a Python program to accept a filename from the user and print the extension of that#

filename=input("Enter your file name: ")
lista=list(filename.split("."))
print("Extension of file is:", lista[1])

print("***************************************\n\n")

#8. Write a Python program to display the first and last colors from the following list.#

color_list = ["Red","Green","White" ,"Black"]
print("First colour from list is {} and last colour from list is {}".format(color_list[0], color_list[-1]))

print("***************************************\n\n")

#9. Write a Python program to display the examination schedule. (extract the date from exam_st_date).#

exam_st_date = (11, 12, 2014)
print("Examination schedule: {}-{}-{}".format(exam_st_date[0],exam_st_date[1],exam_st_date[2]))

print("***************************************\n\n")

#10. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.#

ynumb=input("Enter an integer: ")
print(int(ynumb)+int(ynumb*2)+int(ynumb*3))

print("***************************************\n\n")
