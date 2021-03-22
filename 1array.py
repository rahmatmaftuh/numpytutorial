import numpy as np

#membuat vector
a = np.array([1,2,3,4]) #bilangan bulat
b = np.array([1.5,3.5,4.7]) #bilangan desimal

#membuat vector dengan range
c = np.arange(1,10,0.5) #formatnya range = np.arrange(batasbawah,batasatas,beda)

#membuat linear space
d=np.linspace(1,10,3) #membuat 4 angka dari 1 sampai 10 dengan jarak yang sama

#membuat matrix
e = np.array(([1,2,3,4] , [4,5,6,0])) #formatnya np.array([(baris 1),(baris2)])

#matrix dengan nilai nol
f = np.zeros((5,1)) #f = np.zeros((baris, kolom))

#matrix dengan nilai satu
g = np.ones((5,5))

#matrix identitas
h1 = np.identity(5) 
h2 = np.eye(5)
print(e)