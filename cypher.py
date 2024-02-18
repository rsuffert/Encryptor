import os

def encrypt(target, output, master):
    lines_encrypted: list = []
    with open(target, 'r') as file:
        for line in file: # para cada registro do arquivo target
            line_encrypted: str = ""
            pointer: int = 0
            for char in line: # para cada caractere do registro
                if not char == "\n":
                    line_encrypted += chr( (ord(char)+ord(master[pointer])+32) % 126 )
                    pointer += 1
                    if pointer > len(master)-1: pointer=0
            lines_encrypted.append(line_encrypted + "\n")
    with open(output, 'w') as file:
        for line in lines_encrypted:
            file.write(line)
    os.remove(target)
    print(f"\nArquivo '{target}' criptografado com sucesso com a chave-mestre para o arquivo '{output}'.")
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
                    line_dec += chr( (ord(char_enc)-ord(master[pointer])-32) % 126 )
                    pointer += 1
                    if pointer > len(master)-1: pointer=0
            lines_decrypted.append(line_dec + "\n")
    # escrever o arquivo descriptografado
    with open(output, 'w') as file:
        for line_dec in lines_decrypted:
            file.write(line_dec)
    os.remove(target)
    print(f"\nArquivo '{target}' descriptografado com sucesso para a chave mestre fornecida para '{output}'.")
    print(f"ATENÇÃO: o arquivo '{target}' foi apagado.")

# rotina principal
master_pw:        str = input("Digite a senha mestre: ")
target_file_name: str = input("Digite o nome do arquivo texto (.txt) sobre o qual operar (deve estar nesta pasta): ") + ".txt"
output_file_name: str = input("Digite o nome do arquivo de destino, sem a extensão (será criado nesta pasta): ") + ".txt"
enc_or_dec:       str = input("Encriptar ou decriptar [E/D]? ").upper()
match enc_or_dec:
    case "E": encrypt(target_file_name, output_file_name, master_pw)
    case "D": decrypt(target_file_name, output_file_name, master_pw)
    case _:   print("Opção inválida! Digite apenas 'E' ou 'D'.")