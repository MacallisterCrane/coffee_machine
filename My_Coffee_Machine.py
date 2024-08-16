MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#format report

def format_data(ingredient):
    ingredient_water = ingredient["water"]
    ingredient_milk = ingredient["milk"]
    ingredient_coffee = ingredient["coffee"]
    return (f"{ingredient_water} ml of water,"
            f"{ingredient_milk} ml of milk,"
            f"{ingredient_coffee} oz of coffee")

#report
def resource_report():
    if user_order == "latte":
        if resources["water"] < MENU["latte"]["water"]:
            print("Sorry theres not enough water at the moment")
        if resources["water"] < MENU["latte"]["water"]:
            resources["water"] -= MENU["latte"]["water"]
        if resources["milk"] < MENU["latte"]["milk"]:
            print("Sorry theres not enough milk at the moment")
        if resources["coffee"] < MENU["latte"]["coffee"]:
            print("Sorry theres not enough coffee at the moment")
    if user_order == "cappuccino":
        if resources["water"] < MENU["cappuccino"]["water"]:
            print("Sorry theres not enough water at the moment")
        if resources["milk"] < MENU["cappuccino"]["milk"]:
            print("Sorry theres not enough milk at the moment")
        if resources["coffee"] < MENU["cappuccino"]["coffee"]:
            print("Sorry theres not enough coffee at the moment")


#coin processing

def coins():
    print("Please enter your coins.")
    global total
    total = 0
    total += int(input("Please enter your quarter")) * 0.25
    total += int(input("Please enter your dime")) * 0.10
    total += int(input("Please enter your nickles")) * 0.05
    total += int(input("Please enter your pennies")) * 0.01
    return total


#change

def change():
    change = 0
    if user_order == "latte":
        if MENU["latte"]["cost"] > total:
            print("Sorry, you dont have enough money")
        elif MENU["latte"]["cost"] == total:
            register += total
            print("Here's your latte")
        elif MENU["latte"]["cost"] < total:
            change += round(total - MENU["latte"]["cost"], 2)
            print(f"Here's your latte, and your change is {change}")
            change -= round(total - MENU["latte"]["cost"], 2)
    if user_order == "cappuccino":
        if MENU["cappuccino"]["cost"] > total:
            print("Sorry, you dont have enough money")
        elif MENU["cappuccino"]["cost"] == total:
            register += total
            print("Here's your cappuccino")
        elif MENU["cappuccino"]["cost"] < total:
            change += round(total - MENU["cappuccino"]["cost"], 2)
            print(f"Here's your cappuccino, and your change is {change}")
            change -= round(total - MENU["cappuccino"]["cost"], 2)




#User order choice

user_order = (input("What would you like? (espresso, latte, cappuccino):"))
if user_order == "latte":
    coins()
    change()
elif user_order == "cappuccino":
    coins()
    change()
elif user_order == "espresso":
    coins()
    change()
elif user_order == "report":
    print(format_data(resources))
else:
    print("Sorry, that's not a current menu option")



