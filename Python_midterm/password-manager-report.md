# Password Manager Python Midterm Davletaliyev

## Project Overview

A command-line password manager made in Python that allows users to securely store and manage passwords for different websites and applications. Users can  log in with a master account and can add or find or change stored passwords.

### Main features
- Authentification with Master login
- You can find the password by searching the doman or app name
- Add passwords or create a random one
- Change existing passwords
- Passwords are encrypted

---

##  Technical Implementation

### Storage
- **master.txt** - Stores master username and bcrypt-hashed password
- **passwords.txt** - Stores entries as `domain,username,encrypted_password`

### Encryption

**Master Password (bcrypt)**
- One-way hash function
- Includes automatic salt generation
- Prevents brute-force attacks

**Stored Passwords (XOR Cipher)**
- Reversible encryption using XOR operation
- Allows passwords to be decrypted for viewing
- Converts to hexadecimal for storage

### Core Functions
- `check_master_login()` - Authenticates user with bcrypt
- `load_passwords()` / `save_passwords()` - File operations
- `find_password()` - Search and display credentials
- `add_password()` - Create new entries with duplicate prevention
- `change_password()` - Update existing passwords
- `generate_password()` - Creates 12-character strong passwords

---

##  Evaluation

### Strengths 
- Passwords encrypted before storage
- Prevents duplicate entries
- Automatic password generation option

### Weaknesses 
- XOR encryption is not really secure
- Hardcoded encryption key
- Cannot delete passwords
- Limited error messages
- Interface implemented through a command line

### Potential Improvements
- Use stronger encryption 
- Add delete password option
- Ability to view all stored domains
- Better interface
---

##  Conclusion and Sources

The password manager successfully stores passwords and domain names with weak but working encryption.  While functional for learning purposes, it would need security improvements for an actual good program. Sources: Markdown: Basics. Daring Fireball: Markdown Basics. (n.d.). https://daringfireball.net/projects/markdown/basics  GeeksforGeeks. (2022, June 3). Hashing passwords in python with BCrypt. https://www.geeksforgeeks.org/python/hashing-passwords-in-python-with-bcrypt/ 
(Looked up some ideas from here)Abhijeetbyte. (n.d.). Abhijeetbyte/MYPmanager: The MYPmanager project allows users to securely store and manage their passwords and other sensitive information. GitHub. https://github.com/Abhijeetbyte/MYPmanager 
Muhamed, S. (2024, October 24). XOR cipher’s mechanism and techniques. Medium. https://medium.com/@salmamuhamed/xor-ciphers-mechanism-and-techniques-63b6786b5c75 

