from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

def rsa_menu():
    print("\n--- RSA Encryption ---")

    key = RSA.generate(2048)

    public_key = key.publickey()
    private_key = key

    print("\nPublic Key:\n", public_key.export_key().decode())

    msg = input("\nEnter message: ").encode()

    cipher_enc = PKCS1_OAEP.new(public_key)
    ciphertext = cipher_enc.encrypt(msg)

    print("\nEncrypted (Base64):", base64.b64encode(ciphertext).decode())

    cipher_dec = PKCS1_OAEP.new(private_key)
    plain = cipher_dec.decrypt(ciphertext)

    print("Decrypted:", plain.decode())
