from aes_like import aes_menu
from des_like import des_menu
from rsa_logic import rsa_menu

def main():
    while True:
        print("\n==============================")
        print(" Text Encryption System ")
        print("==============================")
        print("1. AES Encryption (CBC)")
        print("2. DES Encryption (CBC)")
        print("3. RSA Encryption (OAEP)")
        print("4. Exit")

        ch = input("Enter choice: ")

        if ch == "1":
            aes_menu()
        elif ch == "2":
            des_menu()
        elif ch == "3":
            rsa_menu()
        elif ch == "4":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
