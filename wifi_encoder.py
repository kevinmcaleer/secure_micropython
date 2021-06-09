from encode import encode, to_csv

wifi_username = 'My Local Wifi'
wifi_password = 'password'
salt = 'AkSE4C*&4£FgBlzf£d!@2'

to_csv('wifi_username.dat',encode(wifi_username,salt))
to_csv('wifi_password.dat',encode(wifi_password,salt))