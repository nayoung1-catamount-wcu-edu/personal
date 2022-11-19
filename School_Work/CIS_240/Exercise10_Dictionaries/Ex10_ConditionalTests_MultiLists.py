currentUsers = ["mary", "tasha", "beth", "julian", "mark"]
newUsers = ["deanna", "Tasha", "ODO", "julian", "Jake"]

currentUsersLower = []
for user in currentUsers:
  currentUsersLower.append(user.lower())

for newUser in newUsers:
  if newUser.lower() in currentUsersLower:
    print("Sorry, " + newUser + " that name is already in use.")
  else:
    print("Great, " + newUser + " that name is still available.")