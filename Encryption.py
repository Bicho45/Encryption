import string

def encrypt(msg, num):
    alphabet = string.ascii_lowercase
    #word = input("Please type a word: ").lower()
    encrypted_word = ""
    for letter in msg:
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            new_position = (original_position+int(num))%26
            encrypted_word += alphabet[new_position]
            if letter.isupper():
                encrypted_word = encrypted_word.upper()
            else:
                encrypted_word = encrypted_word.lower()
        else:
            encrypted_word += letter
    print(encrypted_word)

def decrypt(msg, num):
    alphabet = string.ascii_lowercase
    encrypted_word = ""
    for letter in msg:
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            new_position = (original_position-int(num))%26
            encrypted_word += alphabet[new_position]
            if letter.isupper():
                encrypted_word = encrypted_word.upper()
            else:
                encrypted_word = encrypted_word.lower()
        else:
            encrypted_word += letter
    print(encrypted_word)

question = input("Encrypt or Decrypt? ").lower()
msg = input("Enter a message: ")
num = input("Enter a shift number: ")
if question == "encrypt":
    encrypt(msg, num)
elif question == "decrypt":
    decrypt(msg, num)
else:
    print("Please try again")
