# Declare Variables
# Get values for Variables
wage = float(input("Enter the wage: $"))
regularHours = float(input("Enter the regular hours: "))
overtimeHours = float(input("Enter the overtime hours: "))
# Do calculations
totalPay=((wage*regularHours)+((wage*overtimeHours)*1.5))
# display results
print("The total weekly pay is $" + str(totalPay))