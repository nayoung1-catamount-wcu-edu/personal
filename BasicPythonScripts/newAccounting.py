def mixed_cost(a, b, X):
    """
    Input
    -----
    a : the total fixed cost (the vertical intercept of the line)
    b :

    """
    return


def runProgram():
    try:
        equation_list = print(
            "\n1 Mixed Cost\n2 Product Cost\n3 Period Cost\n4 Conversion Cost\n5 Prime Cost\n6 Variable Cost\n7 Cost of Goods Sold"
        )
        equation_selection = int(input("Enter value for equation you want to solve: "))
        if equation_selection == 1:
            a = input("Total fixed cost")
            mixed_cost(a, b, X)
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