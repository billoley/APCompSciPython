letters = "abcdefghijklmnopqrstuvwxyz"


def encrypt(m, k):
    new_message = ""
    for i in m:
        if i in letters:
            new_index = letters.find(i) + k
            while new_index >= 26:
                new_index -= 26
            new_message = new_message + letters[new_index]
        else:
            new_message = new_message + i
    return new_message


message = input("Enter your message. ").lower()
key = int(input("Enter your key to encrypt your message. "))

encrypted_message = encrypt(message, key)

print(encrypted_message)
