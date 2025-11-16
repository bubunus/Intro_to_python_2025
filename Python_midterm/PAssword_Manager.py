import random
import bcrypt


def encrypt(password):
    
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password_bytes, salt)
    return hashed.decode('utf-8')


def simple_encrypt(password, key="secret"):
    encrypted = ""
    for i in range(len(password)):
        encrypted += chr(ord(password[i]) ^ ord(key[i % len(key)]))
    return encrypted.encode('utf-8').hex()

def simple_decrypt(encrypted_hex, key="secret"):
    encrypted = bytes.fromhex(encrypted_hex).decode('utf-8')
    decrypted = ""
    for i in range(len(encrypted)):
        decrypted += chr(ord(encrypted[i]) ^ ord(key[i % len(key)]))
    return decrypted


def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!@#$%"
    
    password = ""
    for i in range(12):
        if i < 6:
            password += random.choice(letters)
        elif i < 10:
            password += random.choice(numbers)
        else:
            password += random.choice(symbols)
    
    return password


def check_master_login(username, password):
    try:
        
        file = open("master.txt", "r")
        lines = file.readlines()
        file.close()
        
        
        saved_username = lines[0].replace("\n", "")
        saved_password_hash = lines[1].replace("\n", "")
        
        
        if username == saved_username:
            
            password_bytes = password.encode('utf-8')
            hash_bytes = saved_password_hash.encode('utf-8')
            if bcrypt.checkpw(password_bytes, hash_bytes):
                return True
        
        return False
        
    except:
        
        file = open("master.txt", "w")
        file.write(username + "\n")
        hashed = encrypt(password)
        file.write(hashed + "\n")
        file.close()
        print("Master account created")
        return True


def load_passwords():
    passwords = {}
    try:
        file = open("passwords.txt", "r")
        lines = file.readlines()
        file.close()
        
        for line in lines:
            parts = line.strip().split(",")
            domain = parts[0]
            username = parts[1]
            encrypted_pass = parts[2]
            passwords[domain] = [username, encrypted_pass]
    except:
        pass
    
    return passwords


def save_passwords(passwords):
    file = open("passwords.txt", "w")
    for domain in passwords:
        username = passwords[domain][0]
        encrypted_pass = passwords[domain][1]
        file.write(domain + "," + username + "," + encrypted_pass + "\n")
    file.close()


def find_password(passwords):
    print("\n--- Find Password ---")
    domain = input("Enter domain/app name: ")
    
    if domain in passwords:
        username = passwords[domain][0]
        encrypted = passwords[domain][1]
        password = simple_decrypt(encrypted)
        
        print("\nFound")
        print("Domain: " + domain)
        print("Username: " + username)
        print("Password: " + password)
    else:
        print("Not found")


def add_password(passwords):
    print("\n--- Add Password ---")
    domain = input("Enter domain or app name: ")
    
    if domain in passwords:
        print("Error: This domain already exists")
        return
    
    username = input("Enter username: ")
    
    choice = input("Generate password? y/n: ")
    if choice == "y":
        password = generate_password()
        print("Generated password: " + password)
    else:
        password = input("Enter password: ")
    
    encrypted = simple_encrypt(password)
    passwords[domain] = [username, encrypted]
    save_passwords(passwords)
    print("Password added!")


def change_password(passwords):
    print("\n--- Change Password ---")
    domain = input("Enter domain/app name: ")
    
    if domain not in passwords:
        print("Error: Domain not found!")
        return
    
    choice = input("Generate password? y/n: ")
    if choice == "y":
        password = generate_password()
        print("Generated password is: " + password)
    else:
        password = input("Enter new password: ")
    
    username = passwords[domain][0]
    encrypted = simple_encrypt(password)
    passwords[domain] = [username, encrypted]
    save_passwords(passwords)
    print("Password is changed")


print("===== PASSWORD MANAGER =====\n")

username = input("Master Username: ")
password = input("Master Password: ")

if check_master_login(username, password):
    print("Login successful\n")
    
    passwords = load_passwords()
    
    while True:
        print("\n===== MENU =====")
        print("1. Find password")
        print("2. Add password")
        print("3. Change password")
        print("4. Exit")
        
        choice = input("\nChoose option: ")
        
        if choice == "1":
            find_password(passwords)
        elif choice == "2":
            add_password(passwords)
        elif choice == "3":
            change_password(passwords)
        elif choice == "4":
            print("Goodbye")
            break
        else:
            print("Invalid choice")
else:
    print("Wrong username or password")
    