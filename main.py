#Cesar Cunha Ziobro
"""
você  deverá  criar  um  programa,  utilizando  a 
linguagem  Python, C, ou C++.  Este  programa,  quando  executado,  irá  determinar  se  uma  string de 
entrada  faz  parte  da  linguagem  𝐿    definida  por  𝐿 = {𝑥 | 𝑥 ∈
 {𝑎,𝑏}∗ 𝑒 𝑐𝑎𝑑𝑎 𝑎 𝑒𝑚 𝑥 é 𝑠𝑒𝑔𝑢𝑖𝑑𝑜 𝑝𝑜𝑟 𝑝𝑒𝑙𝑜 𝑚𝑒𝑛𝑜𝑠 𝑑𝑜𝑖𝑠 𝑏} segundo o alfabeto  Σ={𝑎,𝑏,𝑐}.  
O  programa  que  você  desenvolverá  irá  receber  como  entrada um arquivo de texto  (.txt) 
contendo várias strings. A primeira linha do arquivo indica quantas strings estão no arquivo de texto de 
entrada. As linhas subsequentes contém uma string por linha.  A seguir está um exemplo das linhas que 
podem existir em um arquivo de testes para o programa que você irá desenvolver: 
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
            return f"{a}: Não pertence"
        if a[letra] == 'a':
            if recebeB(a, letra):
                pass
            else:
                return f"{a}: Não Pertence"
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