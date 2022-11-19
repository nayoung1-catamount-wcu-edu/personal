""" import math

# request the input
radius =float(input("enter the spere's  radius: "))

# compute the results
diameter = 2 * radius
circumference = diameter * math.pi
surfaceArea = 4 * math.pi * radius * radius

#dispaly the results
print("diameter:", diameter)
print("circumference:", circumference)
print("surface area:", surfaceArea)"""



"""wcuResidenceHalls = ['albright', 'benton', 'balsam', 'noble']
print(wcuResidenceHalls)

tooFar = 'norton'
wcuResidenceHalls.append(tooFar)
print(wcuResidenceHalls)
print('\nThe Residence Hall ' +tooFar.title() + " is too far away from the Forsyth building.")"""


#8/26
"""wcuResidenceHalls = ['albright', 'benton', 'balsam', 'noble']
print(wcuResidenceHalls)

poppedAlbright = wcuResidenceHalls.pop(0)
poppedBenton = wcuResidenceHalls.pop(0)
print(str(poppedAlbright) + ' and ' + str(poppedBenton) + ' are adjacent to each other.')"""

#8/31
"""wcuResidenceHalls = ['walker', 'scott', 'harrill']

def print_wcuResidenceHalls_titlecase():
    for wcuResidenceHall in wcuResidenceHalls:
        wcuResidenceHalls_titlecase = wcuResidenceHall.title()
        print(wcuResidenceHalls_titlecase)

print_wcuResidenceHalls_titlecase()"""

wcuResidenceHalls = ['walker', 'scott', 'harrill']

def save_file():
    f = open("WCU_Residence_Halls.txt", 'a')
    for wcuResidenceHall in wcuResidenceHalls:
        f.write(wcuResidenceHall + '\n')
    f.close

save_file()