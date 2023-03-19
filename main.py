alphabet = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

message = 'Come over here Watson'
key = 3


def encrypt(n, text):
    result = ''
    for l in text:
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


def bruteForce(message):
    result = [''] * 26
    for l in message:
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


for i, j in enumerate(bruteForce(encrypt(key, message))):
    print("{:2d}: {}".format(i,j))
