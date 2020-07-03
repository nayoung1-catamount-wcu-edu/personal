# Script for Solving Accounting problems


def mixed_cost():  # Mixed Cost Formula -> Y = a + b(X)
    # The total fixed cost (the vertical intercept of the line)
    a = int(input("\nEnter value for a: "))
    # The variable cost per unit of activity (the slope of the line)
    b = int(input("Enter value for b: "))
    # The level of activity
    X = int(input("Enter value for x: "))

    cost = a + (b * X)
    print("\nThe total mixed cost is: ${:4.2f}".format(cost))


def product_cost():  # Product Cost Formula -> Direct Materials + Direct Labor + Manufacturing overhead
    # The cost of direct materials
    dm = int(input("\nEnter direct materials cost: "))
    # The cost of direct labor
    dl = int(input("Enter direct labor cost: "))
    # The cost of manufactoring overhead
    mo = int(input("Enter manufactoring overhead cost: "))

    cost = dm + dl + mo
    print("\nThe total product cost is: ${:4.2f}".format(cost))


def period_cost():  # Period Cost Formula -> Selling Expenses + Administrative Expenses
    # The cost of selling expenses
    se = int(input("\nEnter selling expenses cost: "))
    # The cost of administrative expenses
    ae = int(input("Enter administrative expenses cost: "))

    cost = se + ae
    print("\nThe total period cost is: ${:4.2f}".format(cost))


def conversion_cost():  # Conversion Cost Formula -> Direct Labor + Manufacturing overhead
    # The cost of direct labor
    dl = int(input("Enter direct labor cost: "))
    # The cost of manufactoring overhead
    mo = int(input("Enter manufactoring overhead cost: "))

    cost = dl + mo
    print("\nThe total conversion cost is: ${:4.2f}".format(cost))


def prime_cost():  # Prime Cost Formula -> Direct Materials + Direct Labor
    # The cost of direct materials
    dm = int(input("\nEnter direct materials cost: "))
    # The cost of direct labor
    dl = int(input("Enter direct labor cost: "))

    cost = dm + dl
    print("\nThe total prime cost is: ${:4.2f}".format(cost))


def variable_cost():  # Variable Cost Formula -> Change in Cost/Change in activity
    # The change in cost
    cc = int(input("\nEnter change in cost: "))
    # THe change in activity
    ca = int(input("Enter change in activity: "))

    cost = cc + ca
    print("\nThe total variable cost is: ${:4.2f}".format(cost))


def cost_of_goods_sold():  # COGS Formula -> Beginning Merchandise Inventory + Purchases - Ending Merchandise Inventory
    # Beginning Merchandise Inventory
    bi = int(input("\nEnter cost of beginning inventory: "))
    # Puchases
    p = int(input("Enter cost of purchases: "))
    # Ending Merchandise Inventory
    ei = int(input("Enter cost of ending inventory: "))

    cost = bi + p - ei
    print("\nThe total cost of goods sold is: ${:4.2f}".format(cost))


def runProgram():
    try:
        equation_list = print(
            "\n1 Mixed Cost\n2 Product Cost\n3 Period Cost\n4 Conversion Cost\n5 Prime Cost\n6 Variable Cost\n7 Cost of Goods Sold"
        )
        equation_selection = int(input("Enter value for equation you want to solve: "))
        if equation_selection == 1:
            mixed_cost()
        elif equation_selection == 2:
            product_cost()
        elif equation_selection == 3:
            period_cost()
        elif equation_selection == 4:
            conversion_cost()
        elif equation_selection == 5:
            prime_cost()
        elif equation_selection == 6:
            variable_cost()
        else:
            cost_of_goods_sold()

    except KeyboardInterrupt:
        exit()

while True:
    runProgram()