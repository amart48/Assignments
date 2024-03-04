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
    return factorial

def maximumNo(N1,N2,N3):
    if N1 > N2 and N3:
        return N1
    elif N2 > N1 and N3:
        return N2
    elif N3 > N1 and N2:
        return N3

#def digits():

def main():
    flag = True # Set the flag to true to repeat the main function 
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
            factorialResult = factorial(N)
            print(f"{N} ! = {factorialResult}")


        elif user_input == 2:
            print("2. Find the maximum")
            N1 = float(input("Please enter the 1st number: "))
            N2 = float(input("Please enter the 2nd number: "))
            N3 = float(input("Please enter the 3rd number: "))
            result = maximumNo(N1,N2,N3)
            print(f"The greatest number among the three numbers: {int(result)}")

        elif user_input == 3:
            print("3. Find the number of digits")
            N = int(input("Enter a natural number for N: "))

        elif user_input == 4:
            flag = False # Sets the flag to false to end the program
            print("Bye!")

        else:
            print("Invalid option! Enter a number between 1 to 4")


displayMyInfo() # Call the displayMyInfo function
main() # Call the main function