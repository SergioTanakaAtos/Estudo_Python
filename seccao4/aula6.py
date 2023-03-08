import os 
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'C:\\Users\\A899160\\Teste\\'
caminho_arquivo += 'aula.txt'


# arquivo =open(caminho_arquivo,'w')

# arquivo.close()

#context manager 
with open(caminho_arquivo, 'w+', encoding="utf8") as arquivo:

    arquivo.write("linha 1\n")
    arquivo.write("linha 2\n")
    arquivo.writelines(
        ('linha 3ççç\n',
         'linha 4')
    )
    arquivo.seek(0,0)
    print(arquivo.read())
    print('lendo')
    arquivo.seek(0,0)
    print(arquivo.readline(),end="")
    print(arquivo.readline().strip())
    print("readlines")
    for linha in arquivo.readlines():
        print(linha.strip())   

print("#" * 40)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())


# os.unlink(caminho_arquivo)
# os.remove(caminho_arquivo)
# os.rename(caminho_arquivo,'aula2')