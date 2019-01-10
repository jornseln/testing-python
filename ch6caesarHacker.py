# Caesar Cipher Hacker
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = 'guv6Jv6Jz!J6rp5r7Jzr66ntrM'
#message = 'RTHAIIT1337EU'
#message = 'En oktobermorgen fikk vi pulsen til å øke var det en hackeR som hadde lykkes med forsøkeT men en HAI I en TWeeT er ikke særlig 1337. løser du gåtEn bør dU vurdere å søke'
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'
#SYMBOLS = ''
#for i in range(32,126):
    #SYMBOLS += chr(i)
    #i += 1
#print(SYMBOLS)


# Loop through every possible key:
for key in range(len(SYMBOLS)):
    # It is important to set translated to the blank string that the
    # previous iteration's value for translated is cleared
    translated = ''

    # The rest of the program is almost the same as the Caesar program:

    # Loop through each symbol in message:
    for symbol in message:
        if symbol in SYMBOLS:
            symbolIndex = SYMBOLS.find(symbol)
            translatedIndex = symbolIndex - key

            # Handle the wraparound:
            if translatedIndex < 0:
                translatedIndex = translatedIndex + len(SYMBOLS)

            # Append the decrypted symbol:
            translated = translated + SYMBOLS[translatedIndex]

        else:
            # Append the symbol without encrypting/decrypting:
            translated = translated + symbol
    # Display every possible decryption:
    print('Key #%s: %s' % (key, translated))


