"""This program encrypts english messages by shifting each letter therein by some number of places. For instance,
he might write A as B, B as C, C as D"""

# MISSING FEATURES: NOT CASE SENSITIVE;

import string

alphabet = list(string.ascii_lowercase)  # declare variable alphabet as a lowercase alphabet list
alphabet_len = len(alphabet)  # total length of the alphabet
print(f"Reference Alphabet:\n {alphabet} \nTotal Length: {alphabet_len}")

while True:

    try:
        k = int(input("\nPlease input a key-number for encryption: "))  # k = number of letters to shift; ex: if k = 1, then a = b
        break

    except ValueError:
        print('This is not a number.')

message = input("Please input a message to be ciphered: ")

print(f"Encryption key is: {k}")
print(f"Message: {message}\n")

message_list = list(message.lower())  # turns string to lower case and split string letters in a list
cyphered_message_list = []
cyphered_message = ""

print("Encryption:\n")

for i in range(len(message_list)):  # iterates through each letter of the "message"
    if message_list[i] in alphabet:
        index = alphabet.index(message_list[i])  # shows in which index of the alphabet list the "message" letter is;
        cyphered_letter = alphabet[(index + k) % alphabet_len]
        cyphered_message_list.append(cyphered_letter)  # appends the result to a list "cyphered_message_list"
        print(f"Message Letter '{message_list[i]}' is Alphabet Index: {index}. Then ciphered Letter is: {cyphered_letter}")

    else:
        cyphered_letter = message_list[i]
        cyphered_message_list.append(cyphered_letter)
        print(f"Message Letter: {message_list[i]} Alphabet Index: None Cyphered Letter: None")

for j in cyphered_message_list:  # converts list to string
    cyphered_message += j

print(f"\nCyphered message: {cyphered_message}")
