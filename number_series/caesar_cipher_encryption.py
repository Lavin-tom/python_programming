#! /usr/bin/python3

# The Caesar cipher is a type of substitution cipher that is one of the simplest and most widely known encryption techniques.
# It is a monoalphabetic cipher, where each letter in the plaintext is shifted a certain number of places down the alphabet.
# For example, with a shift of 1, A would be replaced by B, B would become C, and so on. 
# The Caesar cipher can be easily broken and is not considered secure, but it still serves as an introduction to the idea of substitution ciphers and cryptography in general.


a = int(input("enter shift no for caesar_cipher encryption : "))

b = "hello"

b = list(b)                              # convert str into list

for i in range(0, len(b)):
    b[i] = chr(ord(b[i]) + a)            # ord function convert it into ascii and again convet into char

b = ''.join(b)                          # join list data into a string
print(b)
