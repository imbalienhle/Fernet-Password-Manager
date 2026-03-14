# import Fernet encryption from the cryptography library
from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self):
        self.key = None                 # stores encryption key
        self.password_file = "passwordFile.txt"  # file where passwords are saved
        self.password_dict = {}         # dictionary to store passwords in memory


    # Create a new encryption key and save it to a file
    def create_key(self):
        self.key = Fernet.generate_key()        # generate a secure key

        with open("key.key", "wb") as f:        # create a file called key.key
            f.write(self.key)                   # write the key into the file

        print("Key created and saved as key.key")


    # Load an existing encryption key from file
    def load_key(self):
        with open("key.key", "rb") as f:        # open key.key
            self.key = f.read()                 # read the key

        print("Key loaded successfully")

    def create_password_file(self, initial_value=None):
        if initial_value is not None:
            for site, password in initial_value.items():
                self.add_password(site, password)
    
     
    # Load passwords from the password file
    def load_password_file(self):

        try:
            with open(self.password_file, "r") as f:
                for line in f:
                    site, encrypted = line.split(":")

                    decrypted = Fernet(self.key).decrypt(
                        encrypted.encode()
                    ).decode()

                    self.password_dict[site] = decrypted

            print("Passwords loaded")

        except FileNotFoundError:
            print("No password file found.")


    # Add a new password
    def add_password(self, site, password):
        if self.key is None:
            print("Error:Encryption key not loaded.Create(Option 1) and load a key(Option 2) first")
            return
        self.password_dict[site] = password

        with open(self.password_file, "a") as f:
            encrypted = Fernet(self.key).encrypt(password.encode())
            f.write(site + ":" + encrypted.decode() + "\n")

        print("Password added successfully")


    # Get a password
    def get_password(self, site):

        if site in self.password_dict:
            return self.password_dict[site]
        else:
            return "No password found for this site."


def main():

    # default site passwords
    passwords = {
        "facebook": "facebook123",
        "twitter": "twitter123",
        "youtube": "youtube123"
    }

    pm = PasswordManager()

    print("""
What do you want to do?

1 - Create a new key
2 - Load existing key
3 - Create password file
4 - Load password file
5 - Add new password
6 - Get password
0 - Exit
""")

    done = False

    while not done:

        choice = input("Enter option: ")

        if choice == "1":
            pm.create_key()

        elif choice == "2":
            pm.load_key()

        elif choice == "3":
            pm.create_password_file(passwords)

        elif choice == "4":
            pm.load_password_file()

        elif choice == "5":
            site = input("Enter site: ")
            password = input("Enter password: ")
            pm.add_password(site, password)

        elif choice == "6":
            site = input("Enter site name: ")
            print("Password:", pm.get_password(site))

        elif choice == "0":
            done = True
            print("Goodbye!")

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()
