import numpy as np

a = np.array(([1,2,3],
	  		  [4,5,6],
	  		  [7,8,9]))

print("matriks a dengan ukuran", a.shape) #cara 1
print("matriks a dengan ukuran", np.shape(a)) #cara 2

#transpose matrix = perubahan baris jadi kolom dan sebaliknya
print("transpose matrix a") #cara 1
print(np.transpose(a)) #cara 2
print(a.T) #cara 3

#flatten array = dijadiin matrix baris
print("flatten matrix a: ")
print(a.ravel())
print(np.ravel(a))

#reshape matrix, ini beda sama transpose
print("reshape matrix a: ")
print(a.reshape(9,1))

#resize matrix
print("resize matrix a: ")
a.resize(3,3)
print(a) 
