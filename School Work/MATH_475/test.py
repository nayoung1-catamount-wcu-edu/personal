"""
def attractive_force():
    m_1 = float(input("Enter mass 1: "))
    m_2 = float(input("Enter mass 2: "))
    r = float(input("Enter distance between the two masses: "))
    G = float(format(6.6742e11, ".11f"))
    return print("\nThe attractive force between the two bodies is:", G * ((m_1 * m_2) / (r ** 2)), "newtons")

while True:
    attractive_force()
    exit()
"""

def attractive_force(m1, m2, r):
    F = 6.6742e11 * ((m1 * m2) / (r ** 2))
    return F