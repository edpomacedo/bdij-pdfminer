import os
from pdfminer.high_level import extract_text

pasta_entrada = 'input'
pasta_saida = 'output'

# Lista todos os arquivos na pasta de entrada com extensão .pdf
arquivos_pdf = [arquivo for arquivo in os.listdir(pasta_entrada) if arquivo.endswith('.pdf')]

# Loop através de cada arquivo PDF
for arquivo_pdf in arquivos_pdf:
    caminho_do_pdf_entrada = os.path.join(pasta_entrada, arquivo_pdf)
    
    # Extrai o texto do PDF
    texto_extraido = extract_text(caminho_do_pdf_entrada)

    # Cria o nome do arquivo de saída
    nome_arquivo_saida = arquivo_pdf.replace('.pdf', '.txt')
    caminho_do_txt_saida = os.path.join(pasta_saida, nome_arquivo_saida)

    # Salva o texto extraído em um arquivo de texto na pasta de saída
    with open(caminho_do_txt_saida, 'w', encoding='utf-8') as arquivo_saida:
        arquivo_saida.write(texto_extraido)

    print(f'Texto extraído de {arquivo_pdf} e salvo em {nome_arquivo_saida}.')
