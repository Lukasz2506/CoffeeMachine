# 100 Days of Code, Angela Yu
# Coffee Machine Project
#Student: Łukasz Świątek Brzeziński, my own workshop

# TODO: 2. Check resources are sufficient to make a drink.

def is_enough_sources(coffee_type):
    '''Check is the sources level in the Coffee Machine are enough
       to make your coffee (coffee_type: espresso, latte, cappuccino)'''
    if resources["water"] <= MENU[coffee_type]["ingredients"]["water"]:
        print("Sorry there is not enough water.")
        return False
    elif resources["coffee"] <= MENU[coffee_type]["ingredients"]["coffee"]:
        print("Sorry there is not enough water and coffee.")
        return False
    elif resources["milk"] <= MENU[coffee_type]["ingredients"]["milk"]:
        print("Sorry there is not enough milk.")
        return False
    else:
        return True




MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# is_enough_sources('cappuccino')


# TODO: 1. Print the report of all coffee machine sources.

def report():
    '''Print report for all resources Coffee Machine
       currently has.'''
    for key in resources:
        if key == 'coffee':
            print(f"{key}: {resources[key]}g,")
        else:
            print(f"{key}: {resources[key]}ml,")
    print(f"Money: ${profit}")

# TODO: 5. Process coins (after sources check), calculate the money.

coins = {
    "penny": 0.01,
    "dime": 0.1,
    "nickel": 0.05,
    "quarter": 0.25
}

def coins_process():
    '''Ask for the coins you put in the machine and count the money sum.'''
    how_many_pennies = int(input("How many pennies? "))
    how_many_dimes = int(input("How many dimes?"))
    how_many_nickel = int(input("How many nickel? "))
    how_many_quarter = int(input("How many quarter? "))
    money_sum = (how_many_quarter * coins['quarter']) + (how_many_pennies * coins['penny']) + (
            how_many_nickel * coins['nickel']) + (how_many_dimes * coins['dime'])
    print(f"${money_sum}")
    return money_sum


# TODO: 6. Check is enough money to prepare the coffe. Actualise sources if coffe will be proceeded.

def is_enough_money(coffee_cost, money_sum):
    """Compare is the coffee price lower then money you putted
       into the coffee machine."""
    change = money_sum - coffee_cost
    if coffee_cost <= money_sum:
        global profit
        profit += coffee_cost
        print(f"Here is ${change} dollars in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO: 7. Create resources actualisation:

def sources_update(coffee_type, resources):
    for key in resources:
        resources[key] = resources[key] - MENU[coffee_type]['ingredients'][key]
    return resources


# TODO: 4. Create turn off machine function

def machine_power(turn_on, coffee_type):
    turn_on = True
    if coffee_type == 'off':
        print("Good Bye!")
        turn_on = False
    return turn_on

# TODO: 8. Make a function which manage the Coffee Machine work
# TODO: 3. Ask the user what to do and prompt the choice. Prompts on each step.

def CoffeMachine(MENU, resources):

    turn_on = True
    coffee_type = input("What would you like? (espresso, latte, cappuccino): ").strip().lower()
    turn_on = machine_power(turn_on, coffee_type)

    while turn_on:

        if coffee_type == "report":
            report()
        else:
            enough_sources = is_enough_sources(coffee_type)
            if enough_sources:
                payment = coins_process()
                print(payment)
                print(coffee_type)
                evaluation = is_enough_money(MENU[coffee_type]['cost'], payment)
                if evaluation:
                    resources = sources_update(coffee_type, resources)
                    print(f"Here is your  ☕{coffee_type}. Enjoy!")

        coffee_type = input("What would you like? (espresso, latte, cappuccino): ").strip().lower()
        turn_on = machine_power(turn_on, coffee_type)

CoffeMachine(MENU, resources)
