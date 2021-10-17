"""
username/password validation
"""

users_data = [
  (1, "goldie", "goldielocks"),
  (2, "peter", "IluvMyCookie"),
  (3, "elhog", "hundred_tomato")
]

username_mapping = {user[1]: user for user in users_data }

print(username_mapping, end="\n")



while True:
  username_input = input("username: ").lower()

  if  username_input in username_mapping:
    password_input = input("password: ")
    _, username, password = username_mapping[username_input]

    if  password_input == password:
      print(f"Welcome back, {username}!")
      break

    else:
      print("Invalid username or password!")
      continue

  else:
    print("User does not exist")


