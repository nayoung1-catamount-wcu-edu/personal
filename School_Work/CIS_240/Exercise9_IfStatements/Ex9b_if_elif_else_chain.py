usernames = ("admin", "Julian", "Wilson", "Candace", "Pete")
#usernames = ()

if usernames:
  for username in usernames:
    if username == ("admin"):
      print("Hello", (username),"welcome to the administration portal.")
    if username == ("Wilson"):
      print("Greeings,", (username))
    if username == ("Candace"):
      print("Salutaions,", (username))
    if username == ("Julian"):
      print("Welcome back,", (username))
  else:
      print("Good morning,", (username))
else:
  print("No Users Exist")