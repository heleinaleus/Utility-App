"""

Vending Machine
Assessment 2 - Intro to Programming

"""

# Making a vending machine

# Create a vending machine with two categories (drinks and food)
# Define a dictionary of items and their prices
# Each item has its own code, name, price, and number of items in stock.
items = {
    "A1": {"name": "Coke", "price": 2.00, "stock": 5},
    "A2": {"name": "Pepsi", "price": 2.00, "stock": 5},
    "B1": {"name": "Water", "price": 1.50, "stock": 5},
    "B2": {"name": "Coffee", "price": 2.50, "stock": 5},   
    "C1": {"name": "Orange Juice", "price": 3.00, "stock": 5},
    "C2": {"name": "Milkshake", "price": 4.00, "stock": 5},
    "D1": {"name": "Popcorn", "price": 2.25, "stock": 5},
    "D2": {"name": "Skittles", "price": 1.75, "stock": 5},
    "E1": {"name": "Lays Chips", "price": 2.00, "stock": 5},
    "E2": {"name": "Mixed Nuts", "price": 3.00, "stock": 5},
    "F1": {"name": "Chocolate Bar", "price": 2.00, "stock": 5},
    "F2": {"name": "Protein Bar", "price": 3.50, "stock": 5},
}


# Function to display the menu of items
def display_menu():
    print("################  Vending Machine  ################")
    print(f"----------------- Total Items : {len(items)}  ----------------- \n")
    print("Code  |   Name                 | Price ")
    print("--------------------------------------------------")
    for code, item in items.items():
        # Formatting the display to ensure that all information is aligned
        print(f"{code:<5} |  {item['name']:<25} | {item['price']:.2f}")
        
# Display the menu once at the start of the program        
display_menu()

# Function to get a valid code from the user
def get_code(items): 
    while True:
        code = input("Enter code: ") # Get input from user 
        # Check if the code is valid
        if code in items:
            return code
        print("Error: Invalid code. Please try again.") # Error message for invalid codes

# User selects an item by entering a code
selected_code = get_code(items)

# Function to get a valid amount of money from the user
def get_money(items, code):
    # Check if the code is valid and get the item
    item = items.get(code)
    if not item:
        # This case should not happen as we already checked the code
        print(f'Error: Invalid code "{code}".') 
        return
    
    while True:
        try:
            # Ask user to enter an amount of money
            money = float(input("Enter amount of money: "))
            # Check if enough money was provided
            if money >= item["price"]:
                return money # Return the valid amount of money
            # Inform user how much more money is needed
            print(f'Error: Not enough money. Please Insert {item["price"] - money:.2f} dhs more.')
        except ValueError:
            # Handle non-numeric inputs
            print("Error: Please enter a valid number.") 
            
# User provides money for the selected item
money_inserted = get_money(items, selected_code) 

# Function to dispense item and calculate change 
def dispense_item(items, code, money): 
    # Use the code to get the item details
    item = items.get(code) 
    if not item: 
        #  This case should not happen as we already checked the code
        print(f'Error: Invalid code "{code}".') 
        return
    
    # Check stock before dispensing
    if item["stock"] > 0: 
        # Dispense the item
        print(f'\nDispensing {item["name"]}...') 
        # Calculate how much change should be returned
        change = money - item["price"] 
        # Update the stock for the item
        item["stock"] -= 1
        # Inform user about the change
        print(f"Returning ${change:.2f} change...\n")
    else:       
        # Inform user if the item is out of stock
        print(f'\nError: {item["name"]} is out of stock.') 

# Call the dispense function 
dispense_item(items, selected_code, money_inserted)

# Function to suggest additional purchase 

def suggest_purchase(items, code):
    # Check if selected code is for a drink
    if code[0] in ['A', 'B', 'C']: 
        print("You might also like:")
        # Look for food (codes starting with D, E, F)
        for snack_code, item in items.items():
            if snack_code[0] in ['D', 'E', 'F']: 
                print(f'({snack_code}): {item["name"]} ({item["price"]:.2f} dhs)')
    # Check if selected code is for a food
    elif code[0] in ['D', 'E', 'F']: 
        print("You might also like:")
        # Look for drinks (codes starting with A, B, C)
        for drink_code, item in items.items():
            if drink_code[0] in ['A', 'B', 'C']: 
                print(f'({drink_code}): {item["name"]} ({item["price"]:.2f} dhs)')

# Call the suggest purchase function after dispensing the item
suggest_purchase(items, selected_code)

# Main Program

import sys

while True:
    # Print menu of items
    display_menu()  
    # Get valid code from user
    code = get_code(items)
    # Get valid amount of money from user
    money = get_money(items, code)
    # Dispense item and calculate change
    dispense_item(items, code, money)
    # Suggest additional purchase based on previous purchase
    suggest_purchase(items, code)
    # Prompt user to continue or exit
    while True:
        # Ask user if they want to make another purchase
        response = input("\nWould you like to make another purchase? (y/n) ")
        # If user says yes, restart process
        if response.lower() == "y":
            break
        elif response.lower() == "n":
        # If user says no, exit program
            print("Thank you for using the vending machine!")
            sys.exit()
        else:
        # Handle invalid input
            print("Error: Invalid response. Please try again.")
            
            
            
            
     








    




