usernames = ("admin", "user1", "user2", "user3", "user4")
#usernames = ()

if usernames:
  for username in usernames:
    if username == "admin":
      print("Hello", (username),"welcome to the administration portal.")
    else:
      print("Welcome back,", (username))
else:
  print("No Users Exist")