# Ivo Nunes nº20202567
import ast
import random

# lista para modificar letras em minusculas
alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# lista para modificar letras em maiusculas
alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

option = ""


# Trazer a Key do dicionario de descodificacao
def get_key(letter, res):
    for key, value in res.items():
        if letter == value:
            return key


# funcao para codificar string do ficheiro
def encode(string, inp):
    try:
        string = "".join([item for item in string])
        print(f"Normal text: {string}")
        dif_letters = []
        # criar lista para de todas as letras sem serem repetidas
        for letter in string:
            if letter not in dif_letters:
                dif_letters.append(letter)
        decode_dict = {}
        verify = []
        for item in dif_letters:
            if item.isupper():
                random.seed(len(alphabet_upper))
                new_letter = random.choice(alphabet_upper)
                # enquanto a nova letra for igual a letra antiga e já existir na lista de verificação ele vai continuar a
                # fazer a escolha randomica da lista de maiusculas
                while new_letter == item or new_letter in verify:
                    new_letter = random.choice(alphabet_upper)
                # adiciona ao dicionario para poder executar o decode posteriormente
                decode_dict[item] = new_letter
                verify.append(new_letter)
            elif item.islower():
                random.seed(len(alphabet_upper))
                new_letter = random.choice(alphabet_lower)
                # enquanto a nova letra for igual a letra antiga e já existir na lista de verificação ele vai continuar a
                # fazer a escolha randomica da lista de minusculas
                while new_letter == item or new_letter in verify:
                    new_letter = random.choice(alphabet_lower)
                decode_dict[item] = new_letter
                verify.append(new_letter)
            else:
                # se o item for um caracter especial seja ele com acento um espaço etc.. vai adicionar igual
                decode_dict[item] = item
                verify.append(item)
        encoded_string = ""
        # percorre a string se a letra estiver no dicionario e a key do dicionario for igual a letra ele adiciona a letra
        encoded_string = "".join([decode_dict[item] if item in decode_dict else item for item in string])
        # escreve num ficheiro o dicionario para poder efetuar o decode
        with open(f"decode_files/{inp}_decode_dict.txt", mode="w") as file:
            # decode_dict = {value: key for key, value in decode_dict.items()}
            file.write(str(decode_dict))
        # escreve num ficheiro a string codificada
        with open(f"encode_files/{inp}.txt", mode="w") as file:
            file.write(encoded_string)
            print(f"Encoded text: {encoded_string}")
    # se o ficheiro nao existir imprime a frase em baixo
    except FileNotFoundError:
        print("This file doesn't exist")
    # se por algum motivo originar um erro de Tipo
    except TypeError:
        print("Input Type error")


# Descodificar a String
def decode(string, inp):
    try:
        string = "".join([item for item in string])
        print(f"Encoded text: {string}")
        # Abrir o dicionario para executar o decode
        with open(f"decode_files/{inp}_decode_dict.txt", mode='r') as file:
            file = file.read()
            # converte a string em um dicionario
            res = ast.literal_eval(file)
        # Adiciona a letra descodificada que é a key do decode dict
        decoded_string = "".join([get_key(letter, res) for letter in string])

        # retorna a string descodificada
        print(f"Decoded text: {decoded_string}")
        with open(f"normal_files/{inp}.txt", mode="w") as normal_file:
            normal_file.write(decoded_string)
    # se o ficheiro nao existir imprime a frase em baixo
    except FileNotFoundError:
        print("This file was never Encoded")
    # se por algum motivo originar um erro de Tipo
    except TypeError:
        print("Input Type error")


# Le o ficheiro para codificar ou descodificar e retorna uma string
def read_file(inp):
    try:
        with open(f"{inp}.txt", mode="r") as text:
            string = text.readlines()
            return string
    # se o ficheiro nao existir imprime a frase em baixo
    except FileNotFoundError:
        print("File does not exist or was never encoded.\nProgram will restart.")


while option.upper() != 'X':
    # Introduza o nome do ficheiro apenas sem .txt
    inp = input("Write the name of the file you want to open whitout extension: ")
    # Escolher a opção pretendida
    option = input("Choose an option [ D ] for decode or [ E ] for encode, [ X ] to end the program: ")
    # Se a opcao for E codifica a string o ficheiro tem de estar na pasta raiz do projeto
    if option.upper() == 'E':
        result = read_file(inp)
        encode(result, inp)
    # Se a opcao for D descodifica a string o ficheiro tem de ter sido codificado uma vez
    if option.upper() == 'D':
        result = read_file(f'encode_files/{inp}')
        decoded = decode(result, inp)

print("\n\nProgram ended Goodbye\n\n")
