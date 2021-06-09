def convert(s):
    # converts a list into a string
    new = ""
    for x in s:
        new += x
    return new

def from_csv(filename):
    # read in a CSV file and output the contents as a string
    f = open(filename,'r')
    file_text = f.readline()
    string_array = []
    file_text.strip("'")
    file_text.strip(',')
    for character in file_text:
        if character != ',' and "'":
            string_array.append(character)
    f.close()
    print("Read in CSV file:", filename)
    return convert(string_array)

def decode(encoded_text, salt):
    # decode the contents of encrypted text, using the salt
    plaintext = []
    count = 0
    for character in encoded_text:
        temp_string = ord(character) - ord(salt[count])
        if temp_string < 0:
            temp_string += 255
        # print(temp_string)
        
        plaintext.append(chr(temp_string))
        if count < len(salt)-1:
            count += 1
        else:
            count = 0
        
    return convert(plaintext)