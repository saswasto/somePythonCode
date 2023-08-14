from cryptography.fernet import Fernet


'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wd") as key_file:
        key_file.write(key)
        file.close()
        return key
'''
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input(":: What is the master password :: \n")
key = load_key() + master_pwd.byte
fer = Fernet(key)
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.realines():
            data = line.rstrip()
            user, passw = data.sprit("|")
            print("user:", user, "| password:",
                  fer.decrypt(passw.encode()).decode())


def add():
    name = input('Account Name: ')
    pwd = input("Password")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password or view a new ones(view, add),press q to quit?").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode:")
        continue