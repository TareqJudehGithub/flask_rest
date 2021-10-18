"""
username/password validation
"""

def user_pass_validator():
  users_data = [
    (1, "goldie", "goldielocks"),
    (2, "peter", "IluvMyCookie"),
    (3, "elhog", "hundred_tomato")
  ]

  username_mapping = {user[1]: user for user in users_data }

  while True:
    username_input = input("username: ").lower()

    # Check if user exists
    if  username_input in username_mapping:
      password_input = input("password: ")
      _, username, password = username_mapping[username_input]

      # check user password
      if  password_input == password:
        return f"Welcome back, {username}!"
        break

      else:
        print("Invalid username or password!")
        

    else:
      print("User does not exist")
      continue

if __name__ == '__main__':
  print(user_pass_validator())
