#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

import math
def displayMyInfo():
    print("-"*31)
    print("|    Adrian Martinez          |")
    print("|    CNIT155 Lab 07           |")
    print("|    Mart2164@purdue.edu      |")
    print("-"*31)

def factorial(N):
    factorial = math.factorial(N)

#def maximumNo(a,b,c):

#def digits():


def main():
    flag = True
    while flag == True:
        print("\n\n\n===============","User Defined Function Menu","="*15)
        print("1. Compute n Factorial")
        print("2. Find the maximum")
        print("3. Find the number of digits")
        print("4. Exit")
        print("="*58,"\n")

        user_input = int(input("Choose one of the options to perform: "))

        if user_input == 1:
            print("1. Compute n Factorial")
            N = int(input("Enter a natural number for N: "))

        elif user_input == 2:
            print("1. Compute n Factorial")
            N = int(input("Enter a natural number for N: "))

        elif user_input == 3:
            print("1. Compute n Factorial")
            N = int(input("Enter a natural number for N: "))

        elif user_input == 4:
            flag = False
            print("Bye!")

        else:
            print("Invalid option! Enter a number between 1 to 4")


displayMyInfo()
main()