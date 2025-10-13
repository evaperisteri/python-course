def decrypt_message(message: str):
    decrypted_message = ""
    for char in message:
        if not char.isnumeric():
            decrypted_message += char
    return decrypted_message

def main():
    strange_message = "432H3525el523l52o5 523C532F52"
    decryption = decrypt_message(strange_message)
    print(decryption)

if __name__ == "__main__":
    main()