SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz '
MAX_KEY_SIZE = len(SYMBOLS)


def get_mode():
    while True:
        mode = input("Do you wish to encrypt or decrypt a message?")
        mode = mode.lower()

        if mode == "encrypt" or mode == "decrypt":
            return mode
        else:
            print('Enter either "encrypt" or "decrypt"')


def get_message():
    message = input("Enter your message:\n")
    return message


def get_key():
    key = 0
    while True:
        key = int(input("Enter the key number (1-%s)" % MAX_KEY_SIZE))

        if key >= 1 and key <= MAX_KEY_SIZE:
            return key


def get_translated_message(mode, message, key):
    translated = ''

    if mode == "decrypt":
        key = -key

    for i in message:
        symbol_index = SYMBOLS.find(i)
        symbol_index += key

        if symbol_index >= len(SYMBOLS):
            symbol_index -= len(SYMBOLS)
        elif symbol_index < 0:
            symbol_index += len(SYMBOLS)
        translated += SYMBOLS[symbol_index]

    return translated


mode = get_mode()
message = get_message()
key = get_key()
print("Your translated text is:")
print(get_translated_message(mode, message, key))
