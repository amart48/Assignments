#===============================================================================
# Adrian Martinez, Thursday 9:30am
# Mart2164@purdue.edu
# Program Description: A program that will print info on products. After the 
# initial print, it will apply a discount to the values in the list. It will then
# print the discounted price of the products. It will also print the average price 
# of all the discounted items. It will finally print what products are $75.81 cents 
# or less. 
# Academic Honesty:
# I attest that this is my original work.
# I have not used unauthorized source code, code either modified or unmodified.
# I have not given other fellow student(s) access to my program. 
#===============================================================================

def displayMyInfo():
    print("*"*44)
    print("********       Assignment 08        ********")
    print("*"*44)

def Discount(lst):
    update = []

    # Loop to find the discounted price of the product
    for price in lst:
        discountedPrice = (price * .07) * 10
        update.append(discountedPrice)
    return update

def PrintInfo(lst1, lst2, lst3):
    print("\tName\t\t\tID\tPrice")
    print("="*50)
    for name, ID, price in zip(lst1, lst2, lst3):
        print(f"\t{name}\t\t{ID}\t${price:.2f}")
    print("\n")

def Average(lst):
    total = 0
    cnt = 0
     
     # Loop to find the average price of the items in the list
    for price in lst:
        total += price
        cnt += 1
    average = total / cnt

    return average

def Search(lst1, lst2, lst3, Average):
    # Print column headers
    print("============ Products under <= $75.81 ============")
    print("\tName\t\t\tID\tPrice")
    print("="*50)
    
    # Loop through each item in the lists
    for name, ID, price in zip(lst1, lst2, lst3):
        # Check if the price is less than or equal to the average
        if price <= Average:
            # Print the product information
            print(f"\t{name}\t\t{ID}\t${price:.2f}")

def main():
    # Define lists for Names, Prices, and IDs
    Names = ["Paint Brush", "Sander\t", "Hand Drill", "Vac Cleaner", "Roller\t", "Chainsaw"]
    IDs = [3750, 4389, 3986, 9562, 1967, 2988]
    Prices = [12.99, 82.49, 117.89, 178.99, 57.49, 199.99]

    # Call PrintInfo to display three lists
    PrintInfo(Names, IDs, Prices)
    
    # Call Average to find the average of prices
    average_price = Average(Prices)
    
    # Print average price with two decimals
    print("*"*50)
    print("==================   Averages   ==================")
    print(f"\nThe average of prices before the discount is $ {average_price:.2f}\n\n")
    
    # Call Discount to change prices of products
    Updated = Discount(Prices)
    
    # Print message for adjusted prices
    print("*"*50)
    print("Prices have been adjusted!")
    
    # Call PrintInfo to display three lists
    PrintInfo(Names, IDs, Updated)
    
    # Call Average to find the average of updated prices
    average_updated_price = Average(Updated)
    
    # Print average updated price with two decimals
    print("*"*50)
    print("==================   Averages   ==================")
    print(f"\nThe average of prices after the discount is $ {average_updated_price:.2f}\n\n")
    
    # Call Search to display products with prices less than or equal to the average after discount
    Search(Names, IDs, Updated, average_updated_price)

displayMyInfo()
main()