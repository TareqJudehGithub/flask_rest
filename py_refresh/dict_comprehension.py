users = [
    (0, "Bob", "password"),
    (1, "Rolf", "pass123@"),
    (2, "Sarah", "pa$$sda@")
  ]


# get user name as key, with rest of elements as values
username_mapping = {ele[1]: ele for ele in users}
print(username_mapping, end="\n")


username_input = input("username: ")
password_input = input("password: ")

if  username_input in username_mapping:
  _, username, password = username_mapping[username_input]

else:
  print("User does not exist") 

if password_input == password:
  print("True")
else:
  print("False")



# practice
print("\n")
print("practice", end="\n\n")

# add user name to a new usernames list:
usernames = [user[1] for  user in users]
print(usernames)

# add passwords to a new passwords list:
passwords = [password[2] for password in users]
print(passwords)

# now combine both newly created list into one tuple 

users_v2 = zip(usernames, passwords)
# for i, x in users_v2:
#   print(i, x)


# new usernames dict with the following structure:
# usernames_data = { "name": "username", "password": "password"}

usernames_data = dict()
for user, password in users_v2:
  usernames_data[user] = password
 
print(usernames_data)

usernames_data = {user: password for (user, password ) in users_v2}

