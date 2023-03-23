from pathlib import Path
from PyPDF2 import PdfReader

PASTA_RAIZ = Path(__file__).parent
PASTA_ORIGINAIS = PASTA_RAIZ / 'pdfs'
PASTA_NOVA = PASTA_RAIZ / 'arquivos_novos'

RELATORIO_BANCO = PASTA_ORIGINAIS / 'R20230317.pdf'

PASTA_NOVA.mkdir(exist_ok=True)

reader = PdfReader(RELATORIO_BANCO)
#print(reader)
page0 = reader.pages[0]


with open(PASTA_NOVA / page0.images[0], 'rb') as imagem:
    ...