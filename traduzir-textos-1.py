from translate import Translator

s=Translator(from_lang='english',to_lang='portuguese')

texto=str(input('Digite um texto para ser traduzido: '))

res=s.translate(texto)

print(res)
