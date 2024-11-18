

class VendingMachine:
    def __init__(self):
        self.inventory = []
        self.money_inserted = 0.0

    def add_beverage(self, beverage):
        self.inventory.append(beverage)

    def display_beverages(self):
        print("Available beverages:")
        for beverage in self.inventory:
            print(f"{beverage.name} - {beverage.price:.2f}")

    def selection(self, choice):
        for beverage in self.inventory:
            if beverage.name.lower() == choice.lower():
                return beverage

        print("Invalid selection, please try again")
        return None

    def insert_money(self, amount):
        self.money_inserted += amount
        print(f"You have inserted: ${self.money_inserted:.2f}")

    def vend_item(self, beverage_name):
        beverage = self.selection(beverage_name)
        if beverage is None:
            return

        while self.money_inserted < beverage.price:
            additional_needed = beverage.price - self.money_inserted
            print(f"Insufficient money. You need ${additional_needed:.2f} more")
            additional_money = (input(f"Please enter the remaining balance ${additional_needed} or enter 'Q' to quit: \n")).strip()

            if additional_money.upper() == "Q":
                print("Transaction canceled. Thank you for using our service!")
                return
            else:
                self.insert_money(float(additional_money))


        self.money_inserted -= beverage.price
        print(f"Vending {beverage.name}. . . . Enjoy!")

        if self.money_inserted > 0:
            print(f"Returning change: ${self.money_inserted:.2f}")
            self.money_inserted = 0.0




