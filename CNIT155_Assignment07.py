#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will not use the math library to perform
# various functions such as computing the factorial of a natural number, finding 
# the maximum number of 3 numbers, and finding how many numbers are within a 
# natural number. This program does not use any built-in functions besides range. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

def displayMyInfo():
    print("-"*31)
    print("|    Adrian Martinez          |")
    print("|    CNIT155 Assignment 07    |")
    print("|    Mart2164@purdue.edu      |")
    print("-"*31)

def factorial(N): # Function to find the factorial of a natural number
    factorialResult = 1
    for i in range(1,N+1): # For loop to continue the function from 1 until N + 1
        factorialResult *= i # Multiplies the current factorialResult by itself and stores in the same variable
    return factorialResult

def maximumNo(N1, N2, N3): # Function to find the mac number of 3 natural numbers
    if N1 > N2 and N1 > N3: # If N1 is greater than both N2 and N3
        return N1
    elif N2 > N1 and N2 > N3: # If N2 is greater than both N1 and N3
        return N2
    elif N3 > N1 and N3 > N2: # If N3 is greater than both N1 and N3
        return N3

def digits(N): # Function to find the amount of numbers in a natural number
    numberResult = 0 # Initalize the numberResult variable to start at 0
    while N > 0: # While variable N is greater than 0, the loop will continue
        N //=10 # Floor division operator to make the number one character shorter. ie: 123/10 = 12.3 = 12 and store in the N variable
        numberResult +=1 # Everytime the function loops, it will add 1 to the numberResult variable to get a count of how many characters in the N variable
    return numberResult

def main():
    displayMyInfo() # Call the displayMyInfo function
    flag = True # Set the flag to true to repeat the main function 
    while flag == True:
        print("\n\n\n===============","User Defined Function Menu","="*15)
        print("1. Compute n Factorial")
        print("2. Find the maximum")
        print("3. Find the number of digits")
        print("4. Exit")
        print("="*58,"\n")

        user_input = int(input("Choose one of the options to perform: ")) # Asks for the user input 

        if user_input == 1: # If the user selects 1...
            print("1. Compute n Factorial")
            N = int(input("Enter a natural number for N: "))
            factorialResult = factorial(N)
            print(f"{N} ! = {int(factorialResult)}")

        elif user_input == 2: # If the user selects 2...
            print("\n2. Find the maximum")
            N1 = float(input("Please enter the 1st number: "))
            N2 = float(input("Please enter the 2nd number: "))
            N3 = float(input("Please enter the 3rd number: "))
            maxResult = maximumNo(N1,N2,N3)
            print(f"The greatest number among the three numbers: {float(maxResult)}")

        elif user_input == 3: # If the user selects 3...
            print("\n3. Find the number of digits")
            N = int(input("Enter a natural number for N: "))
            numberResult = digits(N)
            print(f"The number of digits in {N} is {int(numberResult)}")

        elif user_input == 4: # If the user selects 4, it will end the program
            flag = False # Sets the flag to false to end the program
            print("Bye!")

        else:
            print("Invalid option! Enter a number between 1 and 4")

main() # Call the main function