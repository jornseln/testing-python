# Transposition Cipher Encryptio
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8

    ciphertext = encryptMessage(myKey, myMessage)

    # Print the encrypted string in ciphertext to the screen, with
    # a | (pipe) after it in case there are spaces at the end of the encrypted message:
    print(ciphertext + '|')

    # Copy the encrypted string in ciphertext to the clipboard:
    pyperclip.copy(ciphertext)

def encryptMessage(key, message):
    # Each string in ciphertext represents a column in the grid:
    ciphertext = [''] * key

    # Loop through each column in ciphertext:
    for column in range(key):
        currentIndex = column

        # Keep looping until currentIndex goes past the message length:
        while currentIndex < len(message):
            # Place the character at currentIndex in message at the 
            # end of the current column in the ciphertext list:
            ciphertext[column] += message [currentIndex]

            # Move currentIndex over:
            currentIndex += key
            # print(ciphertext) # for watching the program flow and how these loops work
            # the while-loop will build a single entry in the ciphertext at a time, starting with ciphertext[0]
            # which will end up being Ceno. This is message[0] + message[8] + message [16] + message[24].
            # The while-loop will end at message[32] because it is > len(message).

    # Convert the ciphertext list into a single string value and return it:
    return ''.join(ciphertext) # for watching how this works, replace the blank string, ie. return '&'.join(ciphertext). It is basically just merging all the entries in the list to a single string.

# If ch7transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function:
if __name__ == '__main__':
    main()