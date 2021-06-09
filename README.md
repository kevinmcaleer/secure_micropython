# Securing Python Code with mpy_cross

This project has 2 main files:
encode.py - has the encode and to_csv function 
decode.py - has the decode and from_csv function

`encode` will take some plaintext and a 'salt' - a string of characters to add to the plain text to scramble it.

`decode` will take some encrpted text and the salt, and will produce the original plaintext

`to_csv` will write out the encoded text to a filename of your choice
`from_csv` will read in the encoded text and provide the text in a string you can then pass to the `decoder` function

# MPY_CROSS
mpy_cross is a micropython cross-compiler; it can take a python module and compile it to byte code. This means that instead of the micropython script being plaintext that anyone can read, it is bytecode that only the micropython interpreter can read.
This is great for hiding the inner workings of our decode routine, and also for hiding the `salt` from potentional attackers.

The compiled .mpy file can be uploaded to the micropython device and treated just like a regular module/library. You can access all the libraries within the .mpy file, and the inner working of the file are hidden from the user.