unconfirmedTransactions = ["Subway", "Jack The Dipper", "Soul Infusion"]
confirmedTransactions = []

while unconfirmedTransactions:
  currentTransaction = unconfirmedTransactions.pop()
 
  if currentTransaction == "Jack The Dipper":
    print("Skipping user: " + currentTransaction)
    continue

  print("Verifying user: " + currentTransaction.title())
  confirmedTransactions.append(currentTransaction)

print("\nThe following users have been confimred:")
for confirmedTransactions in confirmedTransactions:
  print(confirmedTransactions.title())


