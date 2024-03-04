#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that converts units into other units. Conversions
# that are featured are Pounds to Kilograms, Celcius to Fahrenheit, miles to 
# kilometers, and more. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

def main(): #Define the main function
    print("         ********************************************")
    print("         *         CNIT155 Assignmnet 02            *") # Print my name
    print("         *                                          *") # prints the assignment 
    print("         *         Conversion Calculator            *") # prints the assignment 
    print("         ********************************************")

    print("")

    name_input = input("Enter your full name: ") # Asks the user to input their name
    print("My name is", name_input) # Prints the users name 

    print("")

    print("** 1st. Pounds to Kilograms conversion **")
    pounds_input = input("What is the weight in pounds to convert it to kilograms?: ")# Asks the user to input the weight in pounds
    pounds = float(pounds_input) # Formats the input from the user to a float
    kilograms = pounds / 2.2046 # Converts the pounds to kilograms
    print (f"The weight entered in pounds is {pounds:.2f} lbs and it is {kilograms:.2f} kg") 
    
    print("")

    print("** 2nd. Celsius to Fahrenheit conversion **")
    Celsius_input = input("Enter the Celsius temperature to convert it to Fahrenheit: ") # Asks the user to input the temperature in  celsius
    Celsius = float(Celsius_input) # Formats the input from the user to a float
    Fahrenheit = (Celsius * 9/5) + 32 # Convert the input from the user for celsius and converts it to fahrenheit
    print (f"The entered temperature in Celsius is {Celsius:.2f} C and it is {Fahrenheit:.2f} F") 
    
    print("")

    print("** 3rd. Miles to Kilometers conversion **")
    miles_input = input("Enter miles to convert it to kilometers: ")
    miles = float(miles_input)
    kilometers =  miles * 1.609344 # Converts the miles to kilometers 
    print (f"The entered distance in miles is {miles:.2f} mi and it is {kilometers:.2f} km.") 
    
    print("")
    
    print("** 4th. Yards to Meters conversion **")
    yards_input = input("Enter yards to convert it to meters: ")
    yards = float(yards_input)
    meters =  yards * .9144 # Converts the yards to meters
    print (f"The entered distance in yards is {yards:.2f} yards and it is {meters:.2f}m.") 

    print("")

    print("** 5th. Feet and Inches to Centimeters? **")
    print("Whats your height in feet and inches?")
    feet_input = int(input("Feet?: ")) # Asks the user to input the feet measurement
    inches_input = int(input("Inches?: ")) # Asks the user to input the inches measurement
    height_inches = feet_input * 12 + inches_input # Converts the input from the feet and inch input to make it 1 variable 
    height_centimeters = height_inches * 2.54 # Converts the height_inchces variable into centimeters
    print(f"The entered height is {feet_input} feet and {inches_input} inch and it is {height_centimeters:.2f} cm")

main()
