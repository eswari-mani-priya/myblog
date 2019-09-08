# __author__ == "Priya"

import os
import base64
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC as pbk

class GenerateKey():
    def __init__(self, password):
        self.password = password

    def key(self):
        salt = b'os.urandom(16)' # Additional input that safeguards password in storage
        kdf = pbk(algorithm=hashes.SHA256(),
                  length=32,
                  salt=salt,
                  backend=default_backend(),
                  iterations=100000)
        key = base64.urlsafe_b64encode(kdf.derive(self.password))
        return key