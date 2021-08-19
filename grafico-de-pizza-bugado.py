#pip install matplotlib
#pip install numpy

import matplotlib.pyplot as plt
import numpy as np

#Valores do gráfico
a=np.array([55,15,32,15])

#Itens que estarão no gráfico
itens=['Setor 1','Setor 2','Setor 3','Setor 4']

#Espaço entre cada área do gráfico
espaço=[0.1,0,0,0]

#Constói o gráfico e exibe na tela
plt.pie(a,labels=itens,explode=espaço,shadow=True)
plt.show
