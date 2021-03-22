import numpy as np

#membuat matrix dengan tipe data tertentu
a = np.array(([0,2,3], [4,5,6]), dtype=bool)

#membuat array dengan menggunakan function
def kuadrat(baris,kolom):
	return kolom**2

def jumlah(baris,kolom):
	return (baris + kolom)

#b = np.fromfunction(fungsi, ukuran matrix, tipe)
b = np.fromfunction(kuadrat, (2,10), dtype=int)
c = np.fromfunction(jumlah,(4,4), dtype = float)

#membuat array atau matrix dengan menggunakan iterasi
iterable = (x*x for x in range(5))
d = np.fromiter(iterable, dtype = int)

#multitype array

dtipe = [("nama", "S255"), ("tinggi", int)]

data = [("ucup",150), ("otong", 160), ("mario",180)]

e = np.array(data,dtype = dtipe)

print(kuadrat(2,6))
print(b)
print(c)
print(d)