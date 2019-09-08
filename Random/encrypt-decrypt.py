# __author__ == "Priya"

from cryptography.fernet import Fernet
from Random.get_key import GenerateKey


class EncryptDecrypt():
    def __init__(self):
        # Get File/folder name from User and change into bytes
        self.choice = input("You want to Encrypt(e)/Decrypt(d): ")
        self.file = input("Enter File path to encrypt: ")
        self.password = input("Enter password for encryption: ").encode()
        self.key = GenerateKey(self.password).key()
        self.f = Fernet(self.key)
        if self.choice == 'e':
            self.encrypt()
        else:
            self.decrypt()

    def read_data(self, file):
        with open(file, 'rb') as fdata:
            return fdata.read()

    def write_data(self, data, file):
        with open(file, 'wb') as fdata:
            fdata.write(data)
        return True

    def encrypt(self):
        data = self.read_data(self.file)
        encrypted_data = self.f.encrypt(data)
        write = self.write_data(encrypted_data, self.file)
        if write:
            print("Successfully Encrypted given file!")

    def decrypt(self):
        data = self.read_data(self.file)
        decrypted_data = self.f.decrypt(data)
        write = self.write_data(decrypted_data, self.file)
        if write:
            print("Successfully Decrypted given file!")


if __name__ == "__main__":
    EncryptDecrypt()