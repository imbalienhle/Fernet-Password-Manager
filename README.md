# Fernet-Password-Manager
A secure password manager built using python that encrypts and stores user passwords using fernet encryption

NOTE: Passwords are encrypted before they're saved to a file so they cannot be read without encryption key
FEATURES IT PROVIDES
-Command line interface
-Generates and stores encryption keys
-Encrypt and stores passwords for different websites
-Retrieve saved passwords

Tech stack
-Python
-Cryptography library(Fernet encryption)

How Fernet Passowrd Manager works:
Option 1-Creates a file(key.key) with a key used to encrpt and decrypt passwords
Option 2-The program loads the key so it can encrypt passwords
Option 3-Creates a file that stores passwords of sites
Option 4-Loads all the stored passwords into memory
Option 5-Adds a new password(for a new site or replaces the one of existing site)
Option 6-Retrives password from passwordFile
Option 0-Exit

Security Notes
1.Without the key or creating the key passwords cannot be decrypted
