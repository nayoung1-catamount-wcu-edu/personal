usernames = ["Bernard", "Charlotte", "Jake"]
emailAddresses = ["bernard@catamount.wcu.edu", "charlotte@catamount.wcu.edu", "jake@catamount.wcu.edu"]

filenames = ["usernames.txt", "emailAddresses.txt"]

for filename in filenames:
  print("\nReading file: " + filename)
  try:
    with open(filename) as f:
      accountInfo = f.read()
      print(accountInfo)
  except FileNotFoundError: 
    print("Sorry, I can't find that file.")