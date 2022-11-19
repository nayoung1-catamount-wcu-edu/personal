# Declare Variables
primeRentalCost = 2
nonprimeRentalCost = 3
# Get Values for Variables
int(primeRentalCost) == 2
int(nonprimeRentalCost) == 3
numberPrimeVideos = int(input("Enter amount of Prime Videos: "))
numberNonPrimeVideos = int(input("Enter amount of NonPrime Videos: "))
# Do Calculations
totalPrimeCost = int(primeRentalCost * numberPrimeVideos)
totalNonPrimeCost = int(nonprimeRentalCost * numberNonPrimeVideos)
totalCost = int(totalPrimeCost + totalNonPrimeCost)
# Display Results
print("The total cost is $" + str(totalCost))