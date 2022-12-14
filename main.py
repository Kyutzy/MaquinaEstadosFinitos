#Cesar Cunha Ziobro
"""
vocΓͺ  deverΓ‘  criar  um  programa,  utilizando  a 
linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irΓ‘  determinar  se  uma  string de 
entrada  faz  parte  da  linguagem  πΏ    definida  por  πΏ = {π₯ | π₯ β
 {π,π}β π ππππ π ππ π₯ Γ© π πππ’πππ πππ ππππ πππππ  ππππ  π} segundo o alfabeto  Ξ£={π,π,π}.  
O  programa  que  vocΓͺ  desenvolverΓ‘  irΓ‘  receber  como  entrada um arquivo de texto  (.txt) 
contendo vΓ‘rias strings. A primeira linha do arquivo indica quantas strings estΓ£o no arquivo de texto de 
entrada. As linhas subsequentes contΓ©m uma string por linha.  A seguir estΓ‘ um exemplo das linhas que 
podem existir em um arquivo de testes para o programa que vocΓͺ irΓ‘ desenvolver: 
3 
abbaba 
abababb 
bbabbaaab 
"""

import os
letras = ["a", "b", "c"]
def ler_arquivo(arquivo): #start
    conteudo = ""
    with open(arquivo, 'r') as arquivo:
        for line in arquivo:
            conteudo += line
    return conteudo.split("\n")

def recebeA(a:str):
    for letra in range(len(list(a))):
        if a[letra] not in letras:
            return f"{a}: NΓ£o pertence"
        if a[letra] == 'a':
            if recebeB(a, letra):
                pass
            else:
                return f"{a}: NΓ£o Pertence"
    return f"{a}: Pertence"

def recebeB(b, num):
    try:
        if b[num] == 'b':
            return True
        if b[num+1] == 'b' and b[num+2] == 'b':
            return f"{b}: Pertence"
        else:
            return False
    except IndexError:
        return False


if __name__ == "__main__":
    try:
        for file in os.listdir("./"):
            if file.endswith(".txt"):
                arquivo = ler_arquivo(file)
                numero = int(arquivo[0])
                for palavra in range(numero):
                    print(recebeA(arquivo[palavra+1]))
    except IndexError:
        print("File Overflow")