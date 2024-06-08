import random
from tqdm import tqdm

def clamp(i: int, max: int):
    while i >= max:
        i -= max
    return i

alphabet = "abcdefghijklmnopqrstuvwxyz 0123456789"

def encr(message: str) -> str:
    global_encr_offset: int = random.randint(0, len(alphabet)-1) #? 0(a)
    encrypted: str = f"{alphabet[global_encr_offset]}"

    # for char in tqdm(message):
    for char in message:
        if char in alphabet:
            char_index = alphabet.index(char)

            char_encr_index_offset = random.randint(0, len(alphabet)-1)
            char_encr_index_offset = clamp(char_encr_index_offset, len(alphabet))

            char_encr_index = char_index + char_encr_index_offset + global_encr_offset
            char_encr_index = clamp(char_encr_index, len(alphabet))

            char_encr = alphabet[char_encr_index]
        else:
            char_encr = ""
        
        
        encrypted += f"{alphabet[char_encr_index_offset] if char_encr != "" else ""}{char_encr}"

    return encrypted


def decr(encrypted: str) -> str:
    message = ""
    global_decr_offset = alphabet.index(encrypted[0])

    # for index, char in tqdm(enumerate(encrypted[1:])):
    for index, char in enumerate(encrypted[1:]):
        if index%2 == 0:
            char_decr_index = alphabet.index(char) + global_decr_offset
        else:
            char_decr = alphabet.index(char) - char_decr_index
            while char_decr < 0:
                char_decr += len(alphabet)
            message += alphabet[char_decr]

    return message

if __name__ == "__main__":
    test = "hello there!"
    test_encr = encr(test)
    
    print(test_encr)

    test_decr = decr(test_encr)
    
    print(test_decr)
