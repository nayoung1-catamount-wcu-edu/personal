import sys
import numpy

# Mixed Cost
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
    if mixed_cost == " ":
        mixed_cost_value = fixed_cost + (variable_cost * activity_level)
    elif fixed_cost == " ":
        fixed_cost_value = (variable_cost * activity_level) - mixed_cost
    elif variable_cost == " ":
        variable_cost_value = 13

    return print()

# Product Cost
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
        "\nTotal Product Cost: ${:4.2f}".format(direct_materials + direct_labor + manu_overhead
    ))

# Period Cost
def period_cost(se, ae):
    """
    inputs:
        se : float : selling expenses
        ae : float : administrative expenses

    outputs:
        cost : float : period cost
    """
    return print(
        "\nThe total period cost is: ${:4.2f}".format(se + ae)
    )