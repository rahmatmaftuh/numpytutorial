import numpy as np

a = [1,2,3,4] #list dari python
b = [5,6,7,8] #list dari python

anp = np.array([1,2,3,4]) #array dari numpy
bnp = np.array([5,6,7,8]) #array dari numpy

#penjumlahan
hasil = a + b
hasilnp = anp + bnp #kalo di array, element wise namanya penjumlahan per elemen

#pengurangan
#hasil1 = a - b #list gabisa dikurangin list
hasilnp1 = anp - bnp

#perkalian 
hasil2 = a * b #list gabisa dikali list
hasilnp2 = anp * bnp 

#pembagian
hasil3 = a / b #list gabisa dikali list
hasilnp3 = anp / bnp

kuadrat
hasil4 = anp**2

print(hasilnp1)