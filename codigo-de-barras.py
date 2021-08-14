from os import write
from barcode import EAN13
from barcode.writer import ImageWriter

with open('arquivo.jpeg','wb') as f:
    EAN13('100000011111',writer=ImageWriter()).write(f)
