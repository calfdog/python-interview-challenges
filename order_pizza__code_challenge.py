"""
    Description: Pizza Ordering code - code hacked from some other code I saw online
    Developer: Rob M
"""

import sys

max_pizzas = 5

# list of dictionaries (pizzas) with name and price
pizzas_available = (
    {"name": "Hawaiian",             "price": 12.5},
    {"name": "Meat Lovers",          "price": 14.5},
    {"name": "Pepperoni",            "price": 10.5},
    {"name": "Ham & Cheese",         "price": 10.5})


class CancelOrder(Exception):
    pass


class Order:
    def __init__(self):
        self.name = ""
        self.number_pizzas = 0
        self.pizzas = []
        self.total_cost = 0
        self.max_pizzas = 5


def get_input(input_message=None):
    """Gets valid input"""

    # loops until break is called
    while True:
        # input to validate, input prompt is as specified
        user_input = input(str(input_message))

        # check if the user wants to quit or cancel the order
        lower = user_input.lower()
        if lower == "qq" or lower == "quit":
            sys.exit()
        elif user_input == "cc" or user_input == "cancel":
            raise CancelOrder()
        else:
            break
    return user_input


def print_order(order):
    print("Name: {}".format(order.name))
    print("\nOrder summary:" + 4 *"\t" + "Price each:\tSubtotal:")
    for pizza in order.pizzas:
        print("\t{}x {:<22}\t${:<6.2f}\t\t${:>5.2f}".format(
            pizza['amount'], pizza['name'],
            pizza['price'], pizza['price']*pizza['amount']))
    print("{:61}--------".format(""))
    print("{:54} Total: ${:.2f}".format("", order.total_cost))


print("*** Rob's Pizzas ***")
print("Enter 'CC' to cancel order, or 'QQ' to exit program at any time")

# list to hold all completed orders
orders = []

# sorts pizza list by price, then alphabetically
pizzas_available = sorted(
    pizzas_available,
    key=lambda k: (k["price"], k["name"]))

# keep getting orders, only exits through sys.exit()
while True:
    # try ... except to catch CancelOrder exception
    try:
        print("\nNew Order")
        order = Order()

        # get name info
        order.name = get_input( "Enter customer name:")

        # get number of pizzas to order,
        # make sure it is more than 0,less than max_pizzas
        while True:
            user_input = get_input("Number of pizzas to order: ")
            user_input = int(user_input)
            if 0 < user_input <= max_pizzas:
                order.number_pizzas = user_input
                break
            else:
                print("Must be a digit, 5 or less (but more than 0)")

        # print menu (each pizza is assigned a number)
        print("\nWhat pizzas would you like to order?")
        for i, pizza in enumerate(pizzas_available):
            # each pizza's number is its index (i) + 1,
            # so the first pizza is 1
            print("{}: {}".format(str(i+1).zfill(2), pizza['name']))

        print("\nEnter your selection number for each pizza you want to buy")
        for i in range(order.number_pizzas):
            while True:
                string = "Pizza #{} of {}:".format(i+1, order.number_pizzas)
                user_input = get_input( string)
                user_input = int(user_input)
                try:
                    if user_input == 0:
                        raise IndexError
                    # selects the pizza based on user_input
                    to_add = pizzas_available[user_input-1]

                    # if the pizza has already been ordered,
                    # increment the amount ordered
                    for ordered in order.pizzas:
                        if to_add["name"] == ordered["name"]:
                            ordered["amount"] += 1
                            break
                    # else add the pizza to the order list
                    else:
                        order.pizzas.append(to_add)
                        order.pizzas[-1]["amount"] = 1

                    # if there has been no error,
                    # input is valid, break from the while loop
                    break

                except IndexError:
                    print("Pizza selection number must"
                        "correspond to those listed above")

        order.total_cost = sum(
            pizza["price"]*pizza["amount"]
            for pizza in order.pizzas)

        # add order to list of orders
        orders.append(order)
        print("\nYour Order was:")
        print_order(order)

        user_input = get_input("Would you like to enter another order? [Yes][No]")

        if user_input.lower().startswith("y"):
            for i, order in enumerate(orders):
                print("-" * 73)
                print_order(order)
                if i == len(orders) + 1:
                    print("-" * 73)
        elif user_input.lower().startswith("n"):
            sys.exit()

    except CancelOrder:
        try:
            print("\nOrder cancelled")
            user_input = get_input("Would you like to enter another order? [Yes][No]")
            if user_input.lower().startswith("n"):
                sys.exit()
        except CancelOrder:
            print("Type 'QQ' to exit the program")

