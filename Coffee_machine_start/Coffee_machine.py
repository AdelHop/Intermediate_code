import Menu_resources

turn = True
coffeeMenu = Menu_resources.MENU
wallet = 0
water = Menu_resources.resources['water']
milk = Menu_resources.resources['milk']
coffee = Menu_resources.resources['coffee']

def userPayment():
    quartersValue = float(quarters * 0.25)
    dimesValue = float(dimes * 0.1)
    nicklesValue = float(nickles * 0.05)
    penniesValue = float(pennies * 0.01)
    payment = quartersValue + dimesValue + nicklesValue + penniesValue
    return payment

def coffeeMachineWallet(payment, ):
    global wallet
    wallet += payment
    return wallet

def paymentChoice():
    global wallet
    if userPayment() < coffeePrice:
        coffeeMachineWallet(payment)
        wallet -= payment
        print("Sorry that's not enough money. Money refunded.")

    elif userPayment() > coffeePrice:
        coffeeMachineWallet(payment)
        change = userPayment() - coffeePrice
        wallet -= change
        change = round(change,2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {userChoice}. Enjoy!")

    elif userPayment() == coffeePrice:
        print("równo")

def checkResources():
    global water
    global milk
    global coffee

    if (water >= coffeeChoice['ingredients']['water']) and (milk >= coffeeChoice['ingredients']['milk']) and (coffee >= coffeeChoice['ingredients']['coffee']):
        water -= coffeeChoice['ingredients']['water']
        milk -= coffeeChoice['ingredients']['milk']
        coffee -= coffeeChoice['ingredients']['coffee']
        return True

    else:
        if water < coffeeChoice['ingredients']['water']:
            print("Sorry there is not enough water.")

        elif milk < coffeeChoice['ingredients']['milk']:
            print("Sorry there is not enough milk.")

        elif coffee < coffeeChoice['ingredients']['coffee']:
            print("Sorry there is not enough coffee.")

        return False

while True:
    userChoice = input("What would you like? (espresso/latte/cappuccino): ")
    while userChoice == 'off':
        print("Your Coffee Machine is turn off")
        turn = False
        turnON = input("If you want to use Caffe Machine push 'on'.")
        if turnON == "on":
            turn = True
            userChoice = input("What would you like? (espresso/latte/cappuccino): ")

    if userChoice == "report":
        print(f"Water: {water}ml")
        print(f"Milk: {milk}ml")
        print(f"Coffee: {coffee}g")
        print(f"Money: ${round(wallet,2)}")
        userChoice = input("What would you like? (espresso/latte/cappuccino): ")

    coffeeChoice = coffeeMenu[userChoice]
    coffeePrice = coffeeChoice['cost']

    if checkResources() == True:
        print(f"Coffee cost {coffeePrice}$. Please insert coins.")
        quarters = 10  # int(input("How many quarters?: "))
        dimes = 10  # int(input("How many dimes?: "))
        nickles = 10  # int(input("How many nickles?: "))
        pennies = 10  # int(input("How many pennies?: "))
        payment = userPayment()
        paymentChoice()







# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# 1a. Check the user’s input to decide what to do next.
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# 2a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off the machine. Your code should end execution when this happens.
#
# checkWater = water
# 1b. The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.
#
# 4. Check resources sufficient?
# 4a. When the user chooses a drink, the program should check if there are enough resources to make that drink.
# 4b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”
# 4c. The same should happen if another resource is depleted, e.g. milk or coffee.
# 5. Process coins.
# 5a. If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
# 5b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# 5c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# 6. Check transaction successful?
# 6a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the program should say “Sorry that's not enough money. Money refunded.”.
# 6b. But if the user has inserted enough money, then the cost of the drink gets added to the machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100mllatt
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# 6c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal places.
# 7. Make Coffee.
# 7a. If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# 7b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.