# ----------------------Index Sub Cipher----------------------
def encryptIndexSubstitutionCipher(text):
    encrypted_message = ""
    spited_message = list(message)
    abc = ""
    for each_chr in spited_message:
        orded = str(ord(each_chr) - 96)
        if int(orded) < 10:
            abc = "0" + orded + " "
            encrypted_message += abc
        else:
            encrypted_message += orded + " "
    encrypted_message = encrypted_message[:-1]
    return encrypted_message


def decryptIndexSubstitutionCipher(text):
    descrypted_message = ""
    encrypted_list = text.split(" ")
    for each in encrypted_list:
        descrypted_message += chr(int(each) + 96)
    return descrypted_message

# ----------------------Morse Code----------------------
morseCode = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..'
}


def encryptMorseCode(text):
    output = ""
    splited_message = list(message)
    for each_chr in splited_message:
        output += morseCode.get(each_chr) + " "
    output = output[:-1]
    return output


def decryptMorseCode(text):
    normal_message = ""
    splited_mose_code = output.split(" ")
    swapped_morseCode = dict([(value, key) for key, value in morseCode.items()])
    for each in splited_mose_code:
        normal_message += swapped_morseCode.get(each)
    return normal_message


# ----------------------Affine Cipher----------------------
def encryptAffineCipher(text, a, b):
    affine_text = ""
    splited_text = list(plain_text)
    for each in splited_text:
        x = ord(each) - 97
        new_x = (a * x + b) % 26
        affine_text += chr(new_x + 97)
    return affine_text


def decryptAffineCipher(text, a, b):
    normal_text = ""
    splited_affine_text = list(affine_text)
    for each in splited_affine_text:
        x = ord(each) - 97
        new_x = (pow(a, -1, 26) * (x - b)) % 26
        normal_text += chr(new_x + 97)
    return normal_text


# ----------------------Caesar Cipher----------------------
def encryptCaesarCipher(text, key1, key2):
    text = list(caesar_message)
    encrypted_caesar_message = ""
    for i in range(len(text)):
        if ord("A") <= ord(text[i]) <= ord("z"):
            if text[i].islower:
                if i % 2 == 0:
                    if ord(text[i]) > ord("z") - key1:
                        encrypted_caesar_message += chr(ord(text[i]) - (26 - key1))
                    else:
                        encrypted_caesar_message += chr(ord(text[i]) + key1)
                else:
                    if ord(text[i]) > ord("z") - key2:
                        encrypted_caesar_message += chr(ord(text[i]) - (26 - key2))
                    else:
                        encrypted_caesar_message += chr(ord(text[i]) + key2)
            elif text[i].isupper:
                if i % 2 == 0:
                    if ord(text[i]) + key1 > ord("Z"):
                        encrypted_caesar_message += chr(ord(text[i] + key1 - 26))
                    else:
                        encrypted_caesar_message += chr(ord(text[i]) + key1)
                else:
                    if ord(text[i]) + key2 > ord("Z"):
                        encrypted_caesar_message += chr(ord(text[i] + key2 - 26))
                    else:
                        encrypted_caesar_message += chr(ord(text[i]) + key2)
            else:
                encrypted_caesar_message += text[i]
        elif text[i].isnumeric():
            if i % 2 == 0:
                if int(text[i]) + key1 >= 10:
                    encrypted_caesar_message += str(int(text[i]) + key1 - 10)
                else:
                    encrypted_caesar_message += str(int(text[i]) + key1)
            else:
                if int(text[i]) + key2 >= 10:
                    encrypted_caesar_message += str(int(text[i]) + key2 - 10)
                else:
                    encrypted_caesar_message += str(int(text[i]) + key2)
        else:
            encrypted_caesar_message += text[i]
    return encrypted_caesar_message


def decryptCaesarCipher(text, key1, key2):
    text = list(encrypted_caesar_message)
    dencrypted_caesar_message = ""
    for i in range(len(text)):
        if 65 <= ord(text[i]) <= 122:
            if text[i].islower():
                if i % 2 == 0:
                    if ord(text[i]) < ord("a") + key1:
                        dencrypted_caesar_message += chr(ord(text[i]) - key1)
                    else:
                        dencrypted_caesar_message += chr(ord(text[i]) - key1)
                else:
                    if ord(text[i]) < ord("a") + key2:
                        dencrypted_caesar_message += chr(ord(text[i]) - key2 + 26)
                    else:
                        dencrypted_caesar_message += chr(ord(text[i]) - key2)
            elif text[i].isupper:
                if i % 2 == 0:
                    if ord(text[i]) < ord("A") + key1:
                        dencrypted_caesar_message += chr(ord(text[i]) + 26 - key1)
                    else:
                        dencrypted_caesar_message += chr(ord(text[i]) - key1)
                else:
                    if ord(text[i]) - key2 < ord("A"):
                        dencrypted_caesar_message += chr(ord(text[i]) + (26 - key2))
                    else:
                        dencrypted_caesar_message += chr(ord(text[i]) - key2)
            else:
                dencrypted_caesar_message += text[i]
        elif text[i].isnumeric():
            if i % 2 == 0:
                if int(text[i]) - key1 < 0:
                    dencrypted_caesar_message += str(int(text[i]) - key1 + 10)
                else:
                    dencrypted_caesar_message += str(int(text[i]) - key1)
            else:
                if int(text[i]) - key2 < 0:
                    dencrypted_caesar_message += str(int(text[i]) - key2 + 10)
                else:
                    dencrypted_caesar_message += str(int(text[i]) - key2)
        else:
            dencrypted_caesar_message += text[i]
    return dencrypted_caesar_message


# ----------------------Transposition Cipher----------------------
def encryptTranspositionCipher(text, key):
    text1 = text[:key]
    text2 = text[key:2 * key]
    text3 = text[2 * key:3 * key]
    text4 = text[3 * key:4 * key]
    text5 = text[4 * key:]
    result = ""
    for i in range(6):
        tt = None
        if i == 0:
            tt = text1[i] + text2[i] + text3[i] + text4[i] + text5[i]
        else:
            tt = text1[i] + text2[i] + text3[i] + text4[i]
        result += tt
    listed_result = list(result)
    first_result = ""
    second_result = ""
    thierd_result = ""
    fourth_result = ""
    fifth_result = ""
    sixth_result = ""
    final_result = ""
    for i in range(5):
        first_result += str(listed_result[i])
    for i in range(5, 9):
        second_result += str(listed_result[i])
    for i in range(9, 13):
        thierd_result += str(listed_result[i])
    for i in range(13, 17):
        fourth_result += str(listed_result[i])
    for i in range(17, 21):
        fifth_result += str(listed_result[i])
    for i in range(21, 25):
        sixth_result += str(listed_result[i])

    for i in range(5):
        final_result += first_result[i]
        if i <= 3:
            final_result += fourth_result[i]
    for i in range(4):
        final_result += second_result[i]
        final_result += fifth_result[i]
    for i in range(4):
        final_result += thierd_result[i]
        final_result += sixth_result[i]
    return final_result



def decryptTranspositionCipher(text, key):
    listed_transposition = list(encrypted_transposition)
    first_text = ""
    second_text = ""
    thierd_text = ""
    fourth_text = ""
    fifth_text = ""
    sixth_text = ""
    for i in range(0, 9, 2):
        first_text += listed_transposition[i]
        if i > 0:
            fourth_text += listed_transposition[i - 1]
    for i in range(9, 17, 2):
        second_text += listed_transposition[i]
        fifth_text += listed_transposition[i + 1]
    for i in range(17, 25, 2):
        thierd_text += listed_transposition[i]
        sixth_text += listed_transposition[i + 1]
    changed1 = first_text[0] + second_text[0] + thierd_text[0] + fourth_text[0] + fifth_text[0] + sixth_text[0]
    changed2 = first_text[1] + second_text[1] + thierd_text[1] + fourth_text[1] + fifth_text[1] + sixth_text[1]
    changed3 = first_text[2] + second_text[2] + thierd_text[2] + fourth_text[2] + fifth_text[2] + sixth_text[2]
    changed4 = first_text[3] + second_text[3] + thierd_text[3] + fourth_text[3] + fifth_text[3] + sixth_text[3]
    changed5 = first_text[4]
    decrypted_transposition = changed1 + changed2 + changed3 + changed4 + changed5
    return decrypted_transposition


message = input("enter substitution message for encrypt: ")
encrypted_message = encryptIndexSubstitutionCipher(message)
print(encrypted_message)
message1 = input("enter substitution message for dencrypt: ")
decrypted_message = decryptIndexSubstitutionCipher(message1)
print(decrypted_message)

morse_message = input("morse code for encypt: ")
output = encryptMorseCode(morse_message)
print(output)
morse_message1 = input("morse code for dencypt: ")
normal_message = decryptMorseCode(morse_message1)
print(normal_message)


a: int = 11
b: int = 5
plain_text = input("enter affine message for encrypt: ")
affine_text = encryptAffineCipher(plain_text, a, b)
print(affine_text)
plain_text1 = input("enter affine message for dencrypt: ")
normal_text = decryptAffineCipher(plain_text1, a, b)
print(normal_text)

caesar_message = input("enter caesar message for encrypt: ")
key1: int = 2
key2: int = 3
encrypted_caesar_message = encryptCaesarCipher(caesar_message, key1, key2)
print(encrypted_caesar_message)
caesar_message1 = input("enter caesar message for dencrypt: ")
decrypted_caesar_message = decryptCaesarCipher(caesar_message1, key1, key2)
print(decrypted_caesar_message)


#text = input("enter transposition message for encrypt: ")
#key: int = 6
#encrypted_transposition = encryptTranspositionCipher(text, key)
#print(encrypted_transposition)
#text2 = input("enter transposition message for dencrypt: ")
#decripted_transposition = decryptTranspositionCipher(text2, key)
#print(decripted_transposition)
