import msvcrt
import time

def main():
    print("=== Keystroke Awareness Demo (Windows) ===")
    print("Keys are read ONLY while this console is focused.")
    print("Press ESC to exit.\n")

    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            timestamp = time.strftime("%H:%M:%S")

            # ESC key
            if key == b'\x1b':
                print("\n[!] Exiting demo.")
                break

            # Printable characters
            if 32 <= key[0] <= 126:
                print(f"[{timestamp}] Key: '{key.decode()}'")
            else:
                print(f"[{timestamp}] Control key: {key[0]}")

if __name__ == "__main__":
    main()
