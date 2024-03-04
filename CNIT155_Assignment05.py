#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will display a menu with options for the 
# user to choose. Depending on the option they choose, it will perform various 
# tasks. The program will end when the user selects option E.  
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

import math
def main():
    flag = True # To repeat the program after completing a function
    while flag == True:
        print("                 While Loops")
        print("**************************************************************")
        print("A. Sum of odd natural numbers from 1 to N")
        print("B. Sum of cubes of odd natural numbers from 1 to N")
        print("C. Check if a natural number, N, is a prime number")
        print("D. Print the multiplication table of N")
        print("E. Exit")
        print("**************************************************************")
        user_input = input("\n\nChoose one of the options to perform: ")

        if (user_input == "A"):
            N = int(input("Enter a natural number for N: "))
            num = 1 # Starting point for 1 through N
            odd_sum = 0 # Start adding from 0
            print("Displaying odd natural numbers from 1 to",N)
            while (num <= N): # Keep the loop going from 1 through users selection until it gets to N
                if num % 2 !=0:
                    odd_sum += num # Add the exisiting odd number to odd_sum
                    print(num) # Print the odd numbers between 1 and N
                num += 1 # Skip the even numbers to get to the next odd number
            print("The sum of odd natural numbers from 1 to",N,"is",odd_sum,"\n")

        elif(user_input == "B"):
            N = int(input("Enter a natural number for N: ")) # Prompt for the user to insert an int for N
            num = 1 # Have 1 be starting point
            cube_sum = 0 # Start adding from 0
            print("Displaying the cubes of odd natural numbers from 1 to",N) 
            while(num <= N): # Keep the loop going from 1 through users selection until it gets to N
                if num % 2 !=0: # Checks to see if the current number is odd
                    cube = num ** 3 # Calculates the cube of the current odd number
                    print(cube) # Prints the cube numbers of the odd numbers between 1 and N
                    cube_sum += cube # Adds the cube to the cube_sum and assigns that value to it
                num += 1 # Move to the next number
            print("The sum of cubes of odd natural numbers between 1 and",N,"is",cube_sum,"\n")
            
        elif(user_input == "C"):
            N = int(input("Enter a natural number for N: "))
            num = 2 # Initalizes the num variable at 2 because 1 is not prime 
            prime = 1 # Initializes the prime variable 
            while num < N: # Keep the loop going while num is less than N 
                if N % num == 0: 
                    prime = 0 
                num += 1 # Move to the next number
            if prime == 1 and N > 1: # Check if N is prime and greater than 1
                print(f"{N} is a prime number\n") # If N is a prime number
            else:
                print(f"{N} is not a prime number\n") # If N is not a prime number

        elif(user_input == "D"): 
            N = int(input("Enter a natural number for N: "))
            num = 1 # Intitalizes the num variable to start at 1
            print("Multiplication table of",N)
            while (num<=10): # Continues the loop until num = 10
                result = num * N # Calculate the result of num and N and moves to the result variable
                print (N, "x", num, "=", result,"\n") # Print N x the num that it is on and continues from 1 to 10
                num +=1 # Add 1 to num to continue to the next number

        elif(user_input == "E"):
            flag = False # Sets the flag to false to stop the program
            print("Goodbye!")

        # If the user selects anything other than A through E, it will ask them to choose from A through E. 
        else:
            print("Invalid input!\nPlease choose from option A through B. ") 
main()