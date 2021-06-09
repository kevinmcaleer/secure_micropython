from encode import encode, to_csv
from decode import decode, from_csv

# run the decode library to get our secret back

username = "This is a really big secret"
password = "this should be complex too"
salt = "Its like another secret"

secure_username = encode(username, salt)
secure_password = encode(password, salt)

print("-"*50)
print("Encrypted string")
print(secure_username)
print(secure_password)
to_csv('uname.csv', secure_username)
to_csv('pname.csv', secure_password)
print("-"*50)

p_username = from_csv('uname.csv')
p_password = from_csv('pname.csv')
plain_username = decode(p_username, salt)
plain_password = decode(p_password, salt)

print("-"*50)
print("Decrypted string")
print(plain_username)
print(plain_password)
print("-"*50)