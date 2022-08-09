import os


def ler_arquivo(arquivo): #start
    conteudo = ""
    with open(arquivo, 'r') as arquivo:
        for line in arquivo:
            conteudo += line
    return conteudo.split("\n")

def avaliar(a):
    for letra in a:
        if letra == 'a':
            return recebeA(a)
        elif letra == 'b':
            return recebeB(a, 0)

def recebeA(a:str):
    for letra in range(len(list(a))):
        if a[letra] == 'a':
            if recebeB(a, letra):
                pass
            else:
                return f"{a}: Não Pertence"
    return f"{a}: Pertence"

def recebeB(b, num):
    try:
        if b[num] == 'b':
            return f"{b}: não pertence"
        elif b[num+1] == 'b' and b[num+2] == 'b':
            return True
        return False
    except IndexError:
        return False


if __name__ == "__main__":

    for file in os.listdir("./"):
        if file.endswith(".txt"):
            print(f"------ Leitura do Arquivo {file} ------")
            arquivo = ler_arquivo(file)
            numero = int(arquivo[0])
            for palavra in range(numero):
                print(avaliar(arquivo[palavra+1]))
            print(f"------ Fim da Leitura do Arquivo {file} ------")