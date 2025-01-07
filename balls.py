import pyttsx3

class VendingMachine:
    def __init__(self):
        self.engine = pyttsx3.init()  # Initialize the TTS engine

    def speak(self, text):
        self.engine.say(text)  # to Say the text
        self.engine.runAndWait()  # Wait until the speech is finished

    def stocks(stuff):  # This is the dictionary of the items available
        stuff.inventory = {
            'D1': {'category': 'Drinks', 'item': 'Water', 'price': 1.00, 'stock': 10},
            'D2': {'category': 'Drinks', 'item': 'Coke', 'price': 1.50, 'stock': 5},
            'D3': {'category': 'Drinks', 'item': 'Coffee', 'price': 2.00, 'stock': 7},
            'S1': {'category': 'Snacks', 'item': 'Lays', 'price': 1.20, 'stock': 8},
            'S2': {'category': 'Snacks', 'item': 'Lebrons', 'price': 1.80, 'stock': 6},
        }

    def menu(stuff):  # This is just for design
        print("\nWelcome to my Vending Machine.!")  # Also displayed on screen
        stuff.speak("Welcome to my Vending Machine!")
        print("/" * 60)
        print("Code:    Category:    Item:           Price:    Stock:")
        for code, details in stuff.inventory.items():  # For every Id, Code Name and price in the dictionary it will print it out
            print(f"{code:<7} {details['category']:<10} {details['item']:<13} ${details['price']:<7} {details['stock']}")
        print("/" * 60)

    def purchase_item(stuff, code):  # This function aims for the item selection and purchase
        if code not in stuff.inventory:  # If the selected Id isn't in the menu/dictionary it'll be invalid and tell them to try again
            print("Invalid item Id. Please try again.")
            return

        item_details = stuff.inventory[code]

        if item_details['stock'] <= 0:
            print(f"Sorry, {item_details['item']} is currently out of stock.")
            return

        print(f"\nYou have selected: {item_details['item']} - ${item_details['price']}")
        while True:
            try:
                money = float(input(f"Please insert Exact Change of, ${item_details['price']} or more: "))
                if money >= item_details['price']:
                    change = round(money - item_details['price'], 2)
                    print(f"Dispensing {item_details['item']}...")
                    print(f"Your change: ${change}")

                    item_details['stock'] -= 1  # Would reduce the stock every time an item is selected and purchased
                    stuff.suggest(code)  # Will grab a category and suggest the item for the user.
                    break
                else:
                    print("Insufficient funds. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid amount.")

    def suggest(stuff, code):
        # Suggest an item based on the category of the purchased item
        category = stuff.inventory[code]['category']
        suggestions = [
            details
            for details in stuff.inventory.values()
            if details['category'] == category and details['stock'] > 0 and details != stuff.inventory[code]
        ]
        if suggestions:
            print("\nYou should also try:")
            for suggestion in suggestions:
                print(f" - {suggestion['item']} for only! ${suggestion['price']}")

    def start(stuff):  # Is the main function to actually run the vending machine
        stuff.stocks()  # Initialize inventory
        while True:
            stuff.menu()
            code = input("\nEnter the code of the item you want to purchase (or 'exit' to quit): ").upper()
            if code == 'EXIT':
                print("Thank you for using it I Guess.!")  # Thank you message
                stuff.speak("Thank you for using it, I guess!")
                break
            stuff.purchase_item(code)


vending_machine = VendingMachine()
vending_machine.start()
