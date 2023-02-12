from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMachine = CoffeeMaker()
moneyMachine = MoneyMachine()
menuMachine = Menu()

is_on = True

while is_on:
    options = menuMachine.get_items()
    drink = input(f"What would you like? ({options}: ")
    if drink == "off":
        is_on = False
    elif drink == "report":
        print(coffeeMachine.report(), moneyMachine.report())

    else:
        userDrink = menuMachine.find_drink(drink)
        resource = coffeeMachine.is_resource_sufficient(userDrink)
        if resource == True:
            if moneyMachine.make_payment(userDrink.cost):
                coffeeMachine.make_coffee(userDrink)

        if resource == False:
            print("Sorry there is not enough water.")



