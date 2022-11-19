from cryptography.fernet import Fernet

 #this provides the master key
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
'''
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd= input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key) #encryption module

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('password.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + '\n')

while True:
    mode= input("Would you like to add a new password or view existing ones (view, add)? you can press q to quit. ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue