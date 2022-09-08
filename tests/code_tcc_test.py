# import docx2txt
# import os
#
#
# def index():
#     dirPath = r"C:\Users\cairo\OneDrive\Área de Trabalho\tcc_test"
#     result = next(os.walk(dirPath))[2]
#
#     texto = []
#     palavras = []
#     for i in result:
#         texto = docx2txt.process(fr"C:\Users\cairo\OneDrive\Área de Trabalho\tcc_test\{i}").lower()
#         palavras = ['python', 'inglês']
#
#     return {'texto': texto, 'palavras': palavras, 'result': result}