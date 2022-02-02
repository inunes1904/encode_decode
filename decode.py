import random
import copy

seed = 0
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Trazer a Key do dicionario de descodificacao
def get_key(letter, decode_dict):
    for key, value in decode_dict.items():
        if letter == value:
            return key


def decode_string(result, seed):
    random.seed(seed)
    alphabet_code = copy.copy(alphabet)
    random.shuffle(alphabet_code)
    decode_dict = {}
    for i in range(len(alphabet)):
        decode_dict[alphabet[i]] = alphabet_code[i]
    decoded_string = "".join([letter if letter not in decode_dict else get_key(letter, decode_dict) for letter in result])
    return decoded_string


name_file = input("Insert the name of the file you want to decode: ")


with open(f"{name_file}.txt", mode="r") as file_encoded:
    result = file_encoded.readlines()

if len(result) > 1:
    seed = int(result[1])
    result = result[0]
else:
    result = "".join([letter for letter in result])
    print(result)
print(f"Encoded Text: {result}")
decoded_string = decode_string(result, seed)
with open(f"{name_file}_decoded.txt", mode="w") as file_decoded:
    file_decoded.write(decoded_string)
    print(f"Decoded Text: {decoded_string}")