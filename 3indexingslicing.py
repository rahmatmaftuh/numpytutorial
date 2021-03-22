import numpy as np

a = np.arange(10)**2 #dia kaya [1, 2, 3, 4] dikuadratin per element karena element wise

print(a)

#mengambil nilai
print("elemen ke 7 dari a adalah", a[6])
print("elemen akhir dari a adalah",a[-1])

#slicing
print("elemen dari 1-6 adalah", a[0:6]) #[start,end]
print("element dari 4 sampai akhir adalah", a[4:])
print("elemen dari awal sampai 5 adalah", a[:5])

#iterasi
for i in a:
	print("nilai :", i)