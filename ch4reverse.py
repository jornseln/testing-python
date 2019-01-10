# Reverse Cipher
# https://www.nostarch.com/crackingcodes/ (BSD Licensed)

message = 'Three can keep a secret, if two of them are dead.'
translated = ''

i = len(message) - 1
while i >= 0:
    translated = translated + message[i]
    i = i -1

print('This is an ecrypted message:')
print(translated)

# For decrypting the message, concatenate letters from the ciphertext starting from the end
decrypted = ''
i = len(translated) - 1
while i >= 0:
    decrypted = decrypted + translated[i]
    i = i - 1

print('This is the decrypted message:')
print(decrypted) 