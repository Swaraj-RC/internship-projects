import msvcrt
from analyzer import analyze_password

def main():
    print("Password Strength Analyzer")
    print("Press ESC at the prompt below to exit.\n")

    while True:
        password = input("Enter password: ")

        strength, feedback = analyze_password(password)

        print(f"\nPassword Strength: {strength}")

        if feedback:
            print("Suggestions:")
            for f in feedback:
                print(f"- {f}")
        else:
            print("Your password is secure")

        print("\nPress ESC to exit or any other key to continue...")
        key = msvcrt.getch()

        if ord(key) == 27:   # ESC key
            print("\nExiting Password Analyzer.")
            break

        print("-" * 40)

if __name__ == "__main__":
    main()
