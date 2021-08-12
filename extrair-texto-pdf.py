#pip install pymupdf
import fitz

#Abra o arquivo em PDF
#OBS: O arquivo em .PDF precisa estar na mesma pasta que o arquivo .py
with fitz.open('blog.pdf') as pdf:
    texto=''

    for pagina in pdf:
        texto=texto+pagina.getText()

print(texto)
