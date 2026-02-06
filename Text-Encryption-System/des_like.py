from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def des_menu():
    print("\n--- DES Encryption ---")

    key_hex = input("Enter Key (8 bytes HEX): ")
    iv_hex = input("Enter IV (8 bytes HEX): ")

    key = bytes.fromhex(key_hex)
    iv = bytes.fromhex(iv_hex)

    msg = input("Enter message: ").encode()

    cipher = DES.new(key, DES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(msg, DES.block_size))

    print("\nEncrypted (HEX):", binascii.hexlify(ciphertext).decode())

    cipher_dec = DES.new(key, DES.MODE_CBC, iv)
    plain = unpad(cipher_dec.decrypt(ciphertext), DES.block_size)

    print("Decrypted:", plain.decode())
