import os
import sys

def encrypt(target, output, master):
    lines_encrypted: list = []
    with open(target, 'r') as file:
        for line in file: # para cada registro do arquivo target
            line_encrypted: str = ""
            pointer: int = 0
            for char in line: # para cada caractere do registro
                if not char == "\n":
                    #line_encrypted += chr( (ord(char)+ord(master[pointer])+32) % 126 )
                    summ: int = ord(char)+ord(master[pointer])
                    line_encrypted += chr( ((summ-32)%(126-32+1)) + 32 )
                    pointer += 1
                    if pointer > len(master)-1: pointer=0
            lines_encrypted.append(line_encrypted + "\n")
    with open(output, 'w') as file:
        for line in lines_encrypted:
            file.write(line)
    os.remove(target)
    print(f"Arquivo '{target}' criptografado com sucesso com a chave-mestre para o arquivo '{output}'.")
    print(f"ATENÇÃO: o arquivo '{target}' foi apagado.")

def decrypt(target, output, master):
    lines_decrypted: list = []
    # descriptografar as linhas com a chave master e colocar em um array em memoria
    with open(target, 'r') as file:
        for line in file:
            pointer = 0
            line_dec: str = ""
            for char_enc in line:
                if not char_enc == "\n":
                    diff: int = (ord(char_enc) - 32) - ord(master[pointer])
                    line_dec += chr(((diff % (126 - 32 + 1)) + (126 - 32 + 1)) % (126 - 32 + 1) + 32)
                    pointer += 1
                    if pointer > len(master)-1: pointer=0
            lines_decrypted.append(line_dec + "\n")
    # escrever o arquivo descriptografado
    with open(output, 'w') as file:
        for line_dec in lines_decrypted:
            file.write(line_dec)
    print(f"Arquivo '{target}' descriptografado com sucesso para a chave mestre fornecida para '{output}'.")

def help():
    exec_name: str = sys.argv[0].split("/")[-1]
    print(f"python {exec_name} -help (para ajuda)")
    print(f"python {exec_name} -e <target_file_name> <output_file_name> <master_password> (para criptografar)")
    print(f"python {exec_name} -d <target_file_name> <output_file_name> <master_password> (para descriptografar)")

# rotina principal
if len(sys.argv) <= 1:
    help()
    sys.exit(-1)

option: str = sys.argv[1].lower()
match option:
    case "-e":
        if len(sys.argv) != 5:
            print("Sintaxe inválida! Opções:")
            help()
        else:
            encrypt(sys.argv[2], sys.argv[3], sys.argv[4])      
    case "-d":
        if len(sys.argv) != 5:
            print("Sintaxe inválida! Opções:")
            help()
        else:
            decrypt(sys.argv[2], sys.argv[3], sys.argv[4])
    case "-help":
        help()
    case _:
        print("Flag inválida! Opções: -help, -e, -d")