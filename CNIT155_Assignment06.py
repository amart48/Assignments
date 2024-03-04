#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will prompt the user to choose an option 
# from A to E. Based on the response from the user, it will execute the code that  
# includes displaying odd numbers from one input through the other, finding the 
# factorial of an number, displaying a right triangle of stars, displaying a 
# centered triangle.
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

import math
def main():
    flag = True
    while flag == True:
        print("\nFor Loops Assignment")
        print("\n=========================")
        print("\nA. Display Odd natural numbers from N1 to N2, where N2>N1")
        print("\nB. Find factorial of N ")
        print("\nC. Display Right Angled Triangle of Stars")
        print("\nD. Display Centered Triangle of Stars")
        print("\nE. Exit\n")
        user_input = input("\n\nEnter your choice: ")        

        if user_input == "A": # If the user selects A...
            N1 = int(input("\n  Enter a natural number for N1: ")) # Asks for the user input for N1
            N2 = int(input("  Enter a natural number for N2: ")) # Asks for the user input for N2
            print("\nDisplaying Odd numbers from,",N1,"to",N2) # Prints the odd numbers from N1 through N2
            for i in range(N1, N2 + 1): # Loop for odd numbers N1 through N2
                if i % 2 !=0: # Check to see if the current number is odd
                    print("\n\n    ",i)

        elif user_input == "B": # If the user selects B...
            N = int(input("\nEnter a natural number for N: ")) # Gathers an input from the user for the N variable
            factorial = 1 # Initializes the factorial variable
            for i in range(1,N+1): # Loop for calculating the factorial of the inputted number
                factorial *= i # Calculates and stores the factorial in the factorial variable
            print("The factorial of",N,"is:",factorial)

        elif user_input == "C": # If the user selects C...
            row = int(input("\n Enter number of rows to print *s: ")) # Gathers an input from the user for the row variable
            print("Right Angled Triangle of Stars with",row,"rows: \n") 
            for i in range(row): 
                for j in range(i+1):
                    print("*",end="")
                print()

        elif user_input == "D": # If the user selects D...
            row = int(input("\n Enter number of rows to print *s: ")) # Gathers an input from the user for the row variable
            print("Centered Triangle of Star with: ",row,"\n") 
            for i in range(1, row + 1):
                print(" " * (row - i), end="") # Prints the spaces
                print("*" * (2 * i - 1)) # Prints the stars
                
        elif user_input == "E": # If the user selects E the program will end
            flag = False
            print("Goodbye!")

        else: # If the user inputs anything except for options A to E
            print("Invalid input!\nPlease choose an option from A to E.")  
            
main()