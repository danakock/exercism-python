def rotate(message, key):
    cipher = ''

    for symbol in message:
            if symbol.isalpha():
                num = ord(symbol)
                num += key

                if symbol.isupper():
                     if num > ord('Z'):
                         num -= 26
                elif symbol.islower():
                     if num > ord('z'):
                         num -= 26

                cipher += chr(num)
            else:
                cipher += symbol
    return cipher
