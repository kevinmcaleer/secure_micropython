def hash(hashed_message):
    clear = []
    for char in hashed_message:
        clear.append(int(char)+27)
    return clear

def secret_message():
    print("This is the secret message")
    hash("")