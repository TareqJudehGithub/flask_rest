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

_, username, password = username_mapping[username_input]

print(password)

if password_input == password:
  print("True")
else:
  print("False")
