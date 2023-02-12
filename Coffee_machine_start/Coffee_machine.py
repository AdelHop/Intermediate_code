import Menu_resources

turn = True
coffeeMenu = Menu_resources.MENU
wallet = 0
water = Menu_resources.resources['water']
milk = Menu_resources.resources['milk']
coffee = Menu_resources.resources['coffee']

def userPayment():
    """Recalculates the user's charges and returns the total."""
    quartersValue = float(quarters * 0.25)
    dimesValue = float(dimes * 0.1)
    nicklesValue = float(nickles * 0.05)
    penniesValue = float(pennies * 0.01)
    payment = quartersValue + dimesValue + nicklesValue + penniesValue
    return payment

def coffeeMachineWallet(payment, ):
    """Adds the user's deposit to the machine's wallet"""
    global wallet
    wallet += payment
    return wallet

def paymentChoice():
    """It gives the rest to the user."""
    global wallet
    if userPayment() < coffeePrice:
        coffeeMachineWallet(payment)
        wallet -= payment
        print("Sorry that's not enough money. Money refunded.")

    elif userPayment() >= coffeePrice:
        coffeeMachineWallet(payment)
        change = userPayment() - coffeePrice
        wallet -= change
        change = round(change,2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {userChoice} ☕. Enjoy!")

def checkResources():
    """Checks whether the machine has sufficient resources to fulfill the order"""
    global water
    global milk
    global coffee
    # for item in order_ingredients:
    #     if order_ingredients[item] >= Menu_resources.resources[item]:
    #         print(f"Sorry there is not enough {item}.")
    #         return False
    # return True

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
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        payment = userPayment()
        paymentChoice()