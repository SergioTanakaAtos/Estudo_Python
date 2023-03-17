from datetime import datetime
from dateutil.relativedelta import relativedelta

valor = 1000000
emprestimo = datetime(2020,12,20)
delta_anos = relativedelta(years= 5)
data_final = emprestimo + delta_anos

parcelas = []
data_parcela = emprestimo
while  data_parcela < data_final:
    parcelas.append(data_parcela)
    data_parcela += relativedelta(months= +1)

quant_parcelas = len(parcelas)

for i in parcelas:
    print(f'DATA: {i}, PARCELA:{valor/quant_parcelas:.2f}')
