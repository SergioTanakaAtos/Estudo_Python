"""
introducao try/except 
try -> tentar executar o codigo 
except -> ocorreu um erro ao tentar executar 
"""
numero_str = input(
    "Vou dobrar o numero que você digitar"
    )
try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print("FLOAT", numero_float)
    print(f'O dobro de {numero_str} é {numero_float *2:.2f}')
except:
    print("isso nao e um numero ")


# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float *2:.2f}')
# else: 
#     print("isso nao e um numero")