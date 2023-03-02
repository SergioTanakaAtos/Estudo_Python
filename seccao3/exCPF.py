import re 
import sys 

#cpf = input("informe seu CPF")\
#    .replace('.', '')\
#    .replace(' ', '')\
#   .replace('', '')
entrada = input("informe seu cpf:")
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada
             )

repetido = entrada == entrada[0] * len(entrada)
if repetido:
    print("Dados sequenciais")
    sys.exit()

#primeiro digito 
nove_digitos = cpf[:9]
cont_regressivo = 10 

resultado_digito1 = 0
for numero in nove_digitos:
    resultado_digito1 += int(numero) * cont_regressivo
    cont_regressivo -= 1 
digito1 = (resultado_digito1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0

#segundo digito 

dez_digitos = nove_digitos + str(digito1)
cont_regressivo2 = 11 
resultado_digito2 = 0

for numero in dez_digitos:
    resultado_digito2 += int(numero) * cont_regressivo2
    cont_regressivo2 -= 1
digito2 = (resultado_digito2 * 10) % 11  
digito2 = digito2 if digito2 <=9 else 0 

cpf_calc = f'{nove_digitos}{digito1}{digito2}'

if cpf == cpf_calc:
    print("cpf válido")
else:
    print("cpf inválido")

