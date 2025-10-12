import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
random.shuffle(key)


input_text = input("Enter a value to encrypt: ")
cipher_text = ""

for letter in input_text:
    index = chars.index(letter)
    cipher_text += key[index]

print (f"encrypted message{cipher_text}")
print(f"Base input : {input_text}")