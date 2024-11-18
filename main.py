from machine import VendingMachine
from beverage import Beverage


def main():
    beverage1 = Beverage("Coke",3.00)
    beverage2 = Beverage("Pepsi",2.75)
    beverage3 = Beverage("Dr.Pepper",2.50)
    beverage4 = Beverage("Water",1.50)
    beverage5 = Beverage("Gatorade",3.50)
    beverage6 = Beverage("Redbull",4.00)

    beverages = [beverage1,beverage2,beverage3,beverage4,beverage5,beverage6]
    vending_machine = VendingMachine()
    for item in beverages:
        vending_machine.add_beverage(item)

    while True:
        print()
        vending_machine.display_beverages()
        choice = input("Select a beverage (enter a name):\n").strip()

        beverage = vending_machine.selection(choice)
        if beverage is None:
            continue

        money = float(input(f"Please enter your money for {beverage.name} (${beverage.price:.2f}): \n$"))
        vending_machine.insert_money(money)
        vending_machine.vend_item(beverage.name)


main()

