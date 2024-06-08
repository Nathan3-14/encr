# Encryption and Decryption Functions
## Description
Some cool functions to encrypt text and decrypt it afterwards.
## Encryption Method
Given a string, the encryption algorithm creates a global offset from 0 to the length of the alphabet. The letter corresponding to this offset is placed at the beginning of the encrypted string.  
Then, for every letter in the given text, a random character offset is generated from 0 to the length of the alphabet.  
The character is then shifted by both the global and character offsets.
Appended to the string (in order) is the character corresponding to the offset and the encrypted character.  
This is repeated until the string is fully encrypted.

