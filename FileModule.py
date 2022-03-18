import os
from CaesarModule import CaesarCipher

def read_file(file_name) -> list:
    lines = []
    try:
        print("Preparing file content for encryption...")
        exisiting_file = open(file_name, 'r')
        begin_read = True
        while begin_read:
            line = exisiting_file.readline()
            if not line:
                begin_read = False
            else:
                lines.append(line)

        exisiting_file.close()
    except IOError:
        print("File Not found. Enter file with absolute or relative path")
        print()
    
    if lines:
        print("Completed file preparation...")
    return lines



def write_file(file_name, contents, shift):
    file_parts = os.path.splitext(file_name)
    encrypted_file_name = file_parts[0] + "_encrypt_" + file_parts[1]

    try:
        if not bool(contents):
            print("Content of file seems empty")
            return
        
        print("Creating encrypted file")
        create_enc_file = open(encrypted_file_name, 'a')

        for line in contents:
            cipher = CaesarCipher(line, shift).caesar_encryption()
            create_enc_file.write(cipher)
        
        print("Encrypted file name [{}] completed".format(encrypted_file_name))
        create_enc_file.close()
    except IOError:
        print("File can not be created")


def encrypt_file(file_name, shift):
    contents = read_file(file_name)
    if contents:
        write_file(file_name, contents, shift)