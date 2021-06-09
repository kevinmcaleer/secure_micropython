from decode import decode, from_csv
salt = 'AkSE4C*&4£FgBlzf£d!@2'

username = decode(from_csv('wifi_username.dat'),salt)
password = decode(from_csv('wifi_password.dat'),salt)
print(username)
print(password)