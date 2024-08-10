user_db = {
    'Maheedhar1679' : 'github16',  #error occured cause u used comparison operator
     'user2' : 'password',
}

def verify_user(username, password):
    if username in user_db :
        if user_db[username] == password:
            return "Login successful"
        else:
            return "Incorrect password"
    else:
          return "Invalid credentials"


username_input = input("Enter username: ")
password_input = input("Enter password: ")

result = verify_user(username_input,password_input)
print(result)