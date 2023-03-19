"""
Andy Huang
3/19/2023
Brute Force Ceasar Cipher in Python
"""

alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = 'Come over here Watson'
key = 3


def encrypt(n, plaintext):
    result = ''
    for l in plaintext:
        try:
            if l.isupper():
                index = ALPHABET.index(l)
                newIndex = (index + n) % 26
                result += ALPHABET[newIndex]
            else:
                index = alphabet.index(l)
                newIndex = (index + n) % 26
                result += alphabet[newIndex]
        except ValueError:
            result += l
    return result


cipherText = encrypt(key, message)


def bruteForce(ciphertext):
    result = [''] * 26
    for l in ciphertext:
        try:
            if l.isupper():
                index = ALPHABET.index(l)
                for i in range(len(result)):
                    newIndex = (index - i) % 26
                    result[i] += ALPHABET[newIndex]
            else:
                index = alphabet.index(l)
                for i in range(len(result)):
                    newIndex = (index - i) % 26
                    result[i] += alphabet[newIndex]
        except ValueError:
            for i in range(len(result)):
                result[i] += l
    return result


for i, j in enumerate(bruteForce(cipherText)):
    print("{:2d}: {}".format(i, j))
