from Resources import MENU, resources, money

# Check if resources are sufficient

def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True

# Process coins

def process_coins():
    print('Please insert coins')
    total = int(input(f"How many quarters?: ")) * 0.25
    total += int(input(f"How many dimes?: ")) * 0.10
    total += int(input(f"How many nickles?: ")) * 0.05
    total += int(input(f"How many pennies?: ")) * 0.01
    return total

# Check transaction succesful

def is_transaction_successful(money_received, drink_cost):
    if money_received > drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f'Here is your {change}$')
        global money
        money += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded. ")
        return False

#Make the coffee
def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}, enjoy it!")

flag = False

while not flag:
    request = input('What would you like? (espresso/latte/cappuccino): ')

    if request == "off":
        print('Machine turned off')
        flag = True
    elif request == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif request in ['espresso', 'latte', 'cappuccino']:
        drink = MENU[request]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(request, drink['ingredients'])
    else:
        print('Invalid request, try again!')