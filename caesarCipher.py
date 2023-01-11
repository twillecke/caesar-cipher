#This program encrypts english messages by shifting each letter therein by some number of places. For instance, he might write A as B, B as C, C as D  

#BUGS: NOT CASE SENSITIVE;

import string

alphabet = list(string.ascii_lowercase) #declare variable alphabet as a lowercase alphabet list
alphabet_len = len(alphabet) #total lenght of the alphabet
print(f"{alphabet} Total Lenght: {alphabet_len}")

k = int(input("Please input a key-number for encryption: ")) #encription key. k = number of letters to shift; ex: if k = 1, then a = b

message = input("Please input a message to be ciphered: ")

print(f"Encription key is: {k}")
print(f"Message: {message}")

message_list = list(message.lower()) # turns string to lower case and split string letters in a list
cyphered_message_list = []
cyphered_message = ""

#print(message_list)

for i in range(len(message_list)): #iterates through each letter of the "message"
    if message_list[i] in alphabet:
        index = alphabet.index(message_list[i]) #shows in which index of the alphabet list the "message" letter is;

        if (index + k) < (alphabet_len - 1):
            cyphered_letter = alphabet[index + k]
            cyphered_message_list.append(cyphered_letter) #appends the result to a list "cyphered_message_list"
            print(f"Message Letter: {message_list[i]} Alphabet Index: {index} Cyphered Letter: {cyphered_letter}")
        elif (index + k) == alphabet_len:
            cyphered_letter = alphabet[0]
            cyphered_message_list.append(cyphered_letter) #appends the result to a list "cyphered_message_list"
        else:
            cyphered_letter = alphabet[(index + k) - alphabet_len]
            cyphered_message_list.append(cyphered_letter) #appends the result to a list "cyphered_message_list"
    else:
        cyphered_letter = message_list[i]
        cyphered_message_list.append(cyphered_letter)
        print(f"Message Letter: {message_list[i]} Alphabet Index: None Cyphered Letter: None")
        
for j in cyphered_message_list: #converts list to string
        cyphered_message += j

print(f"Cyphered message: {cyphered_message}")









    

    
