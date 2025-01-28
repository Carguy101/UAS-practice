import numpy as np
import random
"""a=np.array([1,2,3])
print(a)

#get dimension
print(a.ndim)

#datatype
print(a.dtype)"""

"""b=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(b[0,3])
print(b[0,:])
print(b[:,3])
b[0,3]=20"""

"""#3-d array
c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)
print(c[1,0,1])
print(c[:,1,:])"""

"""#all same
d=np.zeros((2,3))
print(d)
e=np.ones((2,3))
f=np.full((3,2),78)  #dimension and number which we want to fill
print(f)"""

"""print(np.random.rand(4,2))

print(np.identity(3))"""

"""
1-d array:
axis 0=entire row,only one dimension
2-d array:
axis 0= vertically,axis 1= horizontally
3-d array:
axis 0=depth, axis 1= operates along row at each depth level,axis 2=operates along column at each depth level
"""
"""arr=np.array([[1,2,3]]) #by putting 2 square brackets,array is 2-d now, so can use axis 1 as well
r1=np.repeat(arr,3,axis=0)
print(r1)
r2=np.repeat(arr,3,axis=1)
print(r2)"""

"""z=np.ones((5,5))
for i in range(1,4):
    for j in range(1,4):
        z[i,j]=0
z[2,2]=9
print(z)"""

"""#maths
a=np.array([1,2,3,4])
b=np.array([1,2,3,1])
print(a+2)
print(a-2)
print(a*2)
print(a+b)
print(a*b)  #this is element-wise

u=np.array([[1,2,3],[4,5,6]])
v=np.array([[1,2],[3,4],[5,6]])
p=np.ones((3,3))
print(np.matmul(u,v))
print(np.linalg.det(p))"""

"""arr1=np.array([[1,2,3,4],[5,6,7,8]])
arr2=arr1.reshape((4,2))
arr3=arr1.reshape(2,2,2)
print(arr1)
print(arr2)
print(arr3)   #no of elements before and after must be same


#for column vectors
a=np.array([[10],[20],[30]])
print(a)

#stacking vectors
v1=np.array([1,2,3,4])
v2=np.array([5,6,7,8])
print(np.vstack([v1,v2]))
print(np.vstack([v1,v2,v2]))
print(np.hstack([v1,v2]))"""

file_data=np.genfromtxt("demo.txt",delimiter=',')
print(file_data)      #default datatype is float
print(file_data.astype(int))

#boolean masking and advanced indexing
print(file_data>50)
print(file_data[file_data>2])     #this makes an array of all numbers greater than 2
#can index with a list in numpy
a=np.array([1,2,3,4,5,6,7])
print(a[[1,3,5]])
print((file_data>1)&(file_data<6))

a=np.identity(3)
print(np.linalg.inv(a))

