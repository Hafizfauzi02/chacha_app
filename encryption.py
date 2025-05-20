from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

KEY = os.urandom(32)  # 256-bit key
NONCE = os.urandom(12)  # 96-bit nonce

def encrypt_message(message):
    message = message.encode()
    algorithm = algorithms.ChaCha20(KEY, NONCE)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(message)
    return ct.hex(), NONCE.hex()

def decrypt_message(ciphertext_hex, nonce_hex):
    ciphertext = bytes.fromhex(ciphertext_hex)
    nonce = bytes.fromhex(nonce_hex)
    algorithm = algorithms.ChaCha20(KEY, nonce)
    cipher = Cipher(algorithm, mode=None, backend=default_backend())
    decryptor = cipher.decryptor()
    pt = decryptor.update(ciphertext)
    return pt.decode()
