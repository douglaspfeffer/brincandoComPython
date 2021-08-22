#pip install translate

from translate import Translator

s=Translator(from_lang='portuguese',to_lang='english')

texto=str(input('Digite um texto para ser traduzido (inglês->português): '))

res=s.translate(texto)

print(res)
