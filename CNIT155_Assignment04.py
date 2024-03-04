#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will use the inputs from the user to create
# a quadratic equation. Following the creation of the quadratic equation, it will
# calculate the discriminant, any roots the inputs produce and the smallest
# coeffecient the inputs produce
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

import math
def main():
    print("\n           ++++++++++++++++++++++++++++++++++++++++++++")
    print("           +              Adrian Martinez             +") # Prints my name
    print("           +            mart2164@purdue.edu           +") # prints my email 
    print("           +           CNIT155 Assignment 4           +") # prints the assignment 
    print("           ++++++++++++++++++++++++++++++++++++++++++++")

    print("\nSecond degree quadratic equation roots calculator: aX^2 + bX + c = 0")

    a = float(input("\n        Enter the coefficient a: ")) # Gather input from the user for a
    b = float(input("        Enter the coefficient b: ")) # Gather input from the user for d
    c = float(input("        Enter the coefficient c: ")) # Gather input from the user for c

    # Print the quadratic equation with the inputs from the user with only one decimal
    print(f"\n        Quadratic equation is: {a:.1f}X^2 + {b:.1f}X + {c:.1f} = 0")

    # Calculate the discriminant(D) = b^2 - 4ac
    D = b ** 2 - 4 * a * c

    # Print the discriminant with 3 decimals
    print(f"\n        The discriminant is {D:.3f}")
    print("\n\n Calculating the roots...................")

    # If else statements to find the roots and print if the equation has one, two or no real roots
    if (D > 0):
        root1 = (-b + math.sqrt(D)) / (2 * a)
        root2 = (-b - math.sqrt(D))/ (2 * a)
        print(f"\n       The equation has two real roots {root1:.3f} and {root2:.3f}")

    # If there are two real roots
    elif (D == 0):
        root1 = (-b + math.sqrt(D)) / (2 * a) # Calculating the first real root
        root2 = (-b - math.sqrt(D)) / (2 * a) # Calculating the first real root

        if isinstance(root1, int): # Checking to see if root1 produces an integer
            print(f"\n       The equation has one real root {root1:.3f}") 

        else: # If root 1 does not produce an integer, it will print the outcome of root2
            print(f"\n       The equation has one real root {root2:.3f}")

    # If there are no real roots, the following will print
    elif (D < 0):
        print("\n       The equation has no real roots")
    
    # If else statements to find the smallest coefficients between a, b and c
    if (a < b and a < c):
        print(f"       The smallest coefficient is {a:.2f}\n")
    elif (b < a and b < c):
        print(f"       The smallest coefficient is {b:.2f}\n")
    elif (c < a and c < b):
        print(f"       The smallest coefficient is {c:.2f}\n")

main()