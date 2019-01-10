# Caesar Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

#The string to be encrypted/decrypted
message = 'This is my secret message'

# The encryption/decryption key
key = 13

#Whether the program encrypts or decrypts
mode = 'encrypt' # Set to either 'encrypt' or 'decrypt'

# Every possible symbol that can be encrypted
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

# Store the encrypted/decrypted form of the message:
translated = ''

for symbol in message:
    # Note: Only symbols in the SYMBOLS string can be encrypted/decrypted.
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)

        # Perform encryption/decryption
        if mode == 'encrypt':
            translatedIndex = symbolIndex + key
        elif mode == 'decrypt':
            translatedIndex = symbolIndex - key

        # The cipher works by incrementing the index of the 'SYMBOLS'
        # string by an integer specified in 'key'. If the symbol is
        # far enough into the string, 'key' can push the translatedIndex
        # beyond the length of the symbolIndex. Eg. the string is 66 long,
        # and shall encrypt '0' with key 13. 0 has an index of 60.
        # 60 + 13 = 73, which is higher than len(SYMBOLS). Hence the
        # wraparound, which results in 73 - 66 = 7 = 'H' is the decrypted
        # version of '0' with key = 13.
        # Handle wraparound, if needed:
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        # Append the symbol without encrypting/decrypting:
        translated = translated + symbol

# Output the translated string:
print(translated)
pyperclip.copy(translated)

