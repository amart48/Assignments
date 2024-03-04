#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will use the inputs from the user to 
# calculate metrics for a pool. The metrics are the side area of the pool, the 
# bottom area of the pool and the volume of the pool. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

import math
def main(): 

    depth1 = float((input("Enter a value for Depth1 (D1): "))) # Gathers the depth1 input from the user
    depth2 = float((input("Enter a value for Depth2 (D2): "))) # Gathers the depth2 input from the user
    
    if(depth1 > depth2): # Check if the depth1 is greater than depth2
        print("Invalid input! D2 must be greater than D1.") # If depth1 is greater than depth2, then it will display an error to the user
    
    else: # If depth1 is less than depth2, the program will continue

        width = float((input("Enter a value for Width (W): "))) # Gathers the width input from the user
        length = float((input("Enter a value for Length (L): "))) # Gathers the length input from the user

        side_area_pool = ((depth1 + depth2) * (length / 2)) # Calculates the side area of the pool
        depth3 = depth2 - depth1 # Calculates the depth3 for future calculations
        hypotenuse_pool = math.sqrt((pow(depth3, 2)) + pow(length, 2)) # Calculates the hypotenuse of the pool
        bottom_area_pool = hypotenuse_pool * width # Calculates the bottom area of the pool
        volume_pool = side_area_pool * width # Calculates teh volume of the pool
        
        print("\nCalculating...\n")

        print(f"The side area of the pool is: {side_area_pool:.2f}") # prints the results of the side area of the pool
        print(f"The bottom area of the pool is: {bottom_area_pool:.2f}") # prints the results of the bottom area of the pool
        print(f"The volume of the pool is: {volume_pool:.2f}") # prints the results of the side area of the pool

main()