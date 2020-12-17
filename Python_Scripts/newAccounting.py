import sys


def mixed_cost(fixed_cost, variable_cost, activity_level, mixed_cost):
    """
    Input
    -----
    fixed_cost : the total fixed cost (the vertical intercept of the line)
    variable_cost : the variable cost per unit of activity (the slope of the line)
    activity_level : the level of activity
    mixed_cost : total mixed cost

    Output
    ------
    cost : total mixed cost
    """
    if mixed_cost == nan:
        mixed_cost_value = fixed_cost + (variable_cost * activity_level)
    elif fixed_cost == nan:
        fixed_cost_value = (variable_cost * activity_level) - mixed_cost
    elif variable_cost == nan:
        variable_cost_value = 13

    return print()


def product_cost(direct_materials, direct_labor, manu_overhead):
    """
    Input
    -----
    direct_materials : cost of direct materials
    direct_labor : cost of direct labor
    manu_overhead : cost of manufacturing overhead

    Output
    ------
    cost : total product cost
    """
    return print(
        "\nTotal Product Cost: ", direct_materials + direct_labor + manu_overhead
    )


def run_program():
    """
    program skeleton
    """
    try:
        print(
            "\n1 Mixed Cost",
            "\n2 Product Cost",
            "\n3 Period Cost",
            "\n4 Conversion Cost",
            "\n5 Prime Cost",
            "\n6 Variable Cost",
            "\n7 Cost of Goods Sold",
        )
        equation_selection = int(
            input("\nEnter value for equation you want to solve: ")
        )
        if equation_selection == 1:
            mixed_cost(
                float(input("\nTotal fixed cost: ")),
                float(input("Variable cost: ")),
                float(input("Level of activity: ")),
            )
            sys.exit()
        elif equation_selection == 2:
            product_cost(
                float(input("\nDirect materials cost: ")),
                float(input("Direct labor cost: ")),
                float(input("Manufacturing overhead cost: ")),
            )
            sys.exit()
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
        sys.exit()


while True:
    run_program()
