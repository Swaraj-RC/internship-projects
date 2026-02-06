from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

def aes_menu():
    print("\n--- AES Encryption ---")

    key_hex = input("Enter Key (16/24/32 bytes HEX): ")
    iv_hex = input("Enter IV (16 bytes HEX): ")

    key = bytes.fromhex(key_hex)
    iv = bytes.fromhex(iv_hex)

    msg = input("Enter message: ").encode()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(msg, AES.block_size))

    print("\nEncrypted (HEX):", binascii.hexlify(ciphertext).decode())

    # Decrypt
    cipher_dec = AES.new(key, AES.MODE_CBC, iv)
    plain = unpad(cipher_dec.decrypt(ciphertext), AES.block_size)

    print("Decrypted:", plain.decode())
