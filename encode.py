import os

def convert(s):
    # converts a list into a string
    new = ""
    for x in s:
        new += x
    return new

def encode(plaintext, salt):
    # encodes plain text using a salt key
    secure_string = []
    count = 0
    for character in plaintext:
        num = ord(character) + ord(salt[count])
        if num > 255:
            num -= 255
        secure_string.append(chr(num))
        if count < len(salt)-1:
            count += 1
        else:
            count = 0
    return convert(secure_string)

def to_csv(filename, secure_string):
    # write out the string to a file
    f = open(filename,'w')
    for character in secure_string:
        # f.write("'")
        f.write(character)
        f.write(",")
    f.close()
    print("Wrote out CSV files:", filename)

