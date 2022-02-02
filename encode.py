import random
import copy

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode_string(encode_dict, result, name_file, seed):
    encoded_string = ""
    for letter in result:
        if letter in encode_dict:
            encoded_string += encode_dict[letter]
        else:
            encoded_string += letter
    with open(f"{name_file}_encoded.txt", mode="w") as file_encoded:
        file_encoded.write(f"{encoded_string}\n")
        file_encoded.write(str(seed))
    print(f"Encoded String: {encoded_string}")

def create_dict(result, name_file):
    seed = random.randint(0, len(alphabet))
    random.seed(seed)
    alphabet_code = copy.copy(alphabet)
    random.shuffle(alphabet_code)
    encode_dict = {}
    for i in range(len(alphabet)):
        encode_dict[alphabet[i]] = alphabet_code[i]
    print(encode_dict)
    encode_string(encode_dict, result, name_file, seed)

try:
    name_file = input("Insert your file name to encode: ")
    with open(f"{name_file}.txt") as file:
        result = file.read()
except FileNotFoundError:
    print("Program will end the file you typed in does not exist.")
print(f"Normal string: {result}")
create_dict(result, name_file)





