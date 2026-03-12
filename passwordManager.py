#PASSWORD MANAGER

#imports fernet encryption from the cryptography library
from cryptography.fernet import Fernet

class PasswordManager:

    def __init__(self):
        self.key=None #stores encryption key
        self.password_file=None #stores path to password file
        self.password_dict={} #stores passwords

#Create a new encryption key and stores it to a file
    def create_key(self, path):
        self.key=Fernet.generate_key() #Generate a secure encryption key
        with open(path, 'wb') as f:
            f.write(self.key)

    def load_key(self, path):
        with open(path, 'rb') as f:
            self.key=f.read()

    def create_password_file(self, path, initial_values=None):
        self.password_file=path

        if initial_values is not None:
            for key, values in initial_values.items():
                self.add_password(key, values)

    def load_password_file(self, path):
        self.password_file=path

        with open(path, 'r') as f:
            for line in f:
                site, encrypted=line.split(":")
                self.password_dict[site]=Fernet(self.key).decrypt(encrypted.encode())

    def add_password(self, site, password):
        self.password_dict[site]=password

        if self.password_file is not None:
            with open(self.password_file, 'a+') as f:
                encrypted= Fernet(self.key).encrypt(password.encode())
                f.write(site + ":" + encrypted.decode()+ "\n")

    def get_password(self,site):
        return self.password_dict[site]
    
def main():
    password={
        "email" : "1234567",
        "facebook" : "FaithAlone08",
        "youtube" :"helloworld123",
        "something" : "FaithAlone09"
    }

    pm=PasswordManager()

    print("""what do you want to do?
        (1) Create a new key
        (2) Load an existing key
        (3) Create new password file
        (4) Load existing password file
        (5)Add a new password
        (6)Get a password
        (q)Quit
        """)
    
    done=False

    while not done:
            choice=input("Enter your choice: ")
            if choice=="1":
                path=input("Enter path: ")
                pm.create_key(path)
            elif choice =="2":
                path=input("Enter path: ")
                pm.load_key(path)
            elif choice == "3":
                path = input("Enter path: ")
                pm.create_password_file(path, password)
            elif choice=="4":
                path = input("Enter path: ")
                pm.load_password_file(path)
            elif choice =="5":
                site=input("Enter the site: ")
                password=input("Enter the password: ")
                pm.add_password(site, password)
            elif choice == "6":
                site =input("what site do you want the password for: ")
                print(f"passoword for {site} is {pm.get_password(site)}")
            elif choice=="q":
                done=True
                print("Bye")
            else:
                print("Invalid choice!")

if __name__=="__main__":
    main()
    
