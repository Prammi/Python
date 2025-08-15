import numpy as np


a=[[1,2,3,4,5],[1,2,3,4,5],[1,2,3,4,5]]
np_array=np.array(a)
print(np_array)

#python range
#step is always a positive integer
a=np.arange(0,10,2)
print(a)


a=np.arange(0,10)
print(a)


a=np.arange(0,10,-2)
print(a)

## evenly space number over an closed interval
a=np.linspace(0,10,10)
print(a)


a=np.linspace(0,1,10)
print(a)

#logarithimic space array take 10^1-> 10^3 wiht 3 points
# np.logspace(start power ,end power, evenly spaced items)
arr=np.logspace(1,3,3)
print(arr)

#array of zeros 
# 1D
arr=np.zeros(10)
print(arr)
#2D
arr=np.zeros([2,3])
print(arr)
#3D
arr= np.zeros([3,3,3])
print(arr)


#array of ones  # default value = float     
# 1D
arr=np.ones(10)
print(arr)
#2D
arr=np.ones([2,3])
print(arr)
#3D
arr= np.ones([3,3])
print(arr)


#array of ones wiht Dtype =int
# 1D
arr=np.ones(10,dtype=int)
print(arr)
#2D
arr=np.ones([2,3],dtype=int)
print(arr)
#3D
arr= np.ones([3,3,3],dtype=int)
print(arr)



#array of full wiht Dtype =int
# 1D
arr=np.full(10,2,dtype=int)
print(arr)
#2D
arr=np.full([2,3],2,dtype=int)
print(arr)
#3D
arr= np.full([3,3,3],2,dtype=int)
print(arr)

#list comprehension equivalent
rows, cols = 3, 4
array_2d = [[0 * j for j in range(cols)] for i in range(rows)]
print(array_2d)
array_2d=[0]*3
print(array_2d)

arr=np.zeros([3,4],dtype=int)
print(arr)

#empty array 
arr= np.empty([2,3])
print(arr)


print("************************ RAND RANDN RANDINT ************************")


arr= np.random.rand(0,1)
print(arr)


#RANDOM VALUES  gives either a random value if nothing is metioned or gives an array with random values between 0 and 1
arr= np.random.rand()#single value 
print(arr)

arr= np.random.rand(0,1) # empty array
print(arr)

arr= np.random.rand(1,1) #[] array with [[one cell]]
print(arr)

arr= np.random.rand(2,3) # 2D array with [[a,b,x],[a,b,x]]
print(arr)

arr= np.random.rand(10) #1D array with ten elements
print(arr)



#RANDOM VALUES with Normal distribution
arr= np.random.randn()#single value 
print(arr)

arr= np.random.randn(0,1) # empty array
print(arr)

arr= np.random.randn(1,1) #[] array with [[one cell]]
print(arr)

arr= np.random.randn(2,3) # 2D array with [[a,b,x],[a,b,x]]
print(arr)

arr= np.random.randn(10) #1D array with ten elements
print(arr)


#RANDOM VALUES with integers
print("random")
arr= np.random.randint(2,5)
print(arr)

arr= np.random.randint(0,1) 
print(arr)

arr= np.random.randint(10,100) 
print(arr)

arr= np.random.randint(10,100, size=(2,3)) 
print(arr)



######
#Datatype
print("************************ DTYPE ************************")

arr= [1,2,3,4,5]
a=np.array(arr)
print(a.dtype) #### default of int data type is 64
a=np.array(arr,dtype=np.uint8)
print(a.dtype)
print(arr)

print("************************ TYPECASTING ************************")

#typecasting

a=[1,2,3,4,6]
npa=np.array(a) #default data type is int64
npa=npa.astype(np.float16) #type casting to float
print(npa)

#2d array casting 
twoDaray=[[1,2,3,4,6],[1,2,3,4,6]]
npa=np.array(twoDaray)
npa=npa.astype(np.str_) ### important no string but use str_
print(npa)


print("************************ RESHAPE VS RAVEL vs FLATTEN ************************")

# reshape an array 
#the length = m*n for reshape 
# if for example len(A)=6 then reshape can only be 3*2 or 6*1 or 1*6
#each one will be an individual array 
arr=[1,2,3,4,5,6]
npa=np.array(arr)

npa1=npa.reshape(2,3)
npa_1=np.reshape(npa,shape=(2,3))
print(npa_1)
npa_2=np.reshape(npa_1,shape=(3,2))
print(npa_2)
npa_3=np.reshape(npa_1,shape=(1,6))
print(npa_3)






#diff between ravel and flatten is ravel may or may not 

# - ravel() returns a view of the array (if possible), making it more memory-efficient but changes may affect the original array.
# - flatten() always returns a copy, ensuring data isolation but using more memory.

# RAVEL - converts multi dimension array to singel

arr=[1,2,3,4,5,6]
npa=np.array(arr)
npa_1=np.reshape(npa,shape=(2,3))
print(npa_1)
npa_2=np.ravel(npa_1)
print(npa_2)


# FLATTEN - converts multi dimension array to singel
arr=[1,2,3,4,5,6]
npa=np.array(arr)
npa_1=np.reshape(npa,shape=(2,3))
print(npa_1)
npa_2=npa_1.flatten()
print(npa_2)

#######
# ARITHEMATIC OPEARATION
######
print("************************ ARITHEMATIC OPERATION ************************")
a=np.array([1,2,3,4])
b=np.array([4,3,2,1])
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)

print("************************ UNIVERSAL FUNCTION OR UNFUC ************************")

a=np.array([1,4,9,16])
b=np.array([1,2])
print(np.sqrt(a))
print(np.exp(b)) # basically e^a[i  21  ]

print(np.log(a))

print("************************ TRIGNOMETRIC ************************")
angles=[0,np.pi/6, np.pi/2]
print(np.sin(angles))
print("************************ slicing ************************")

a=np.array([1,2,3,4,5,6])
print(a[::-1])
print(a[::1])
print(a[1:4:1])
print(a[1:4:-1])
print(a[-1:-4:-1])

a= np.array([[1,2,3],[4,5,6],[7,8,9]])
#matric slicing is row slicing followed by col slicing
print(a[0:2,0:2])
print(a[:,:]) #full array
print(a[0:3,1:]) #r*c slicing as per index


print("************************ LOOPING ************************")
a= np.array([[1,2,3],[4,5,6],[7,8,9]])

for i in np.nditer(a):
    print(i)

for index,value in np.ndenumerate(a):
    print("index="+str(index) +" "+ "value="+str(value))
    print(f"index={index} value={value}")
    

print("************************ VIEW vs copy ************************")
a= np.array([[1,2,3],[4,5,6],[7,8,9]])
rv= np.ravel(a)
a1=rv[0:2]
a1[0]=100
print(a1)
print(rv)
print(a)
print(np.shares_memory(a1,a))
print(np.shares_memory(rv,a))

a= np.array([[1,2,3],[4,5,6],[7,8,9]])
rv= np.ravel(a)
a2=rv[0:2].copy()
a2[0]=100
print(a2)
print(rv)
print(a)
print(np.shares_memory(a2,a))
print(np.shares_memory(rv,a))

a= np.array([[1,2,3],[4,5,6],[7,8,9]])
flat=np.arange(1,10)
a3=flat[0:2].copy()
a3[0]=100
print(a3)
print(flat)
print(a)
print(np.shares_memory(a3,a))
print(np.shares_memory(flat,a))
print(np.shares_memory(flat,a3))


a= np.array([[1,2,3],[4,5,6],[7,8,9]])
realFlat=a.flatten()
a4=realFlat[0:2]
a4[0]=100
print(a4)
print(realFlat)
print(a)
print(np.shares_memory(realFlat,a))
print(np.shares_memory(a4,realFlat))
print(np.shares_memory(a,a4))



print("************************ MATRIX TRANSPOSE ************************")
a= np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a.T) # for 2 D arrays 
print(a.transpose()) # for higher dimension arrays

a= np.arange(24).reshape(2,3,4) #cheat code for developing 2 block 3 row and 4 col array
# or
a = np.array([
  [[ 0,  1,  2,  3],
   [ 4,  5,  6,  7],
   [ 8,  9, 10, 11]],

  [[12, 13, 14, 15],
   [16, 17, 18, 19],
   [20, 21, 22, 23]]
])

# default order is 2*3*4 here ie block * row * col in the index order 0,1,2
firstTranspose=a.transpose(2,1,0) #this means the tranpose is number of col=block; number of row= row; number of col =block from original array final order is (4*3*2 x)
print(firstTranspose) 


print("************************ CONCAT ************************")
a=np.array([1,3])
b=np.array([2,4])
print(np.concatenate((a,b))) #important that concatenate takes input as tuple(a,b) not a,b
print(np.concatenate((np.concatenate((a,b)),np.concatenate((a,b)))))

a=np.array([[1,2],[3,4]])
b=np.array([[11,12],[13,14]])
print(np.concatenate((a,b)))
print(np.hstack((a,b)))
print(np.concatenate((a,b),axis=1))#same as horizontal stacking with axis as 1
print(np.vstack((a,b)))
print(np.concatenate((a,b),axis=0)) #same as vertical stacking with axis as zero

#3d concat
arr1= np.arange(24).reshape(2,3,4)
arr2= np.arange(24,48).reshape(2,3,4)
vstack=np.vstack((arr1,arr2))
print(vstack)
print(vstack.shape)
hstack=np.hstack((arr1,arr2))
print(hstack)
print(hstack.shape)


print("************************ SPLIT ************************")
arr1= np.arange(12).reshape(3,4)
print(np.hsplit(arr1,2))
print(np.vsplit(arr1,3))
print(np.split(arr1,1))

#splitting in 3d model
arr = np.arange(8).reshape(2, 2, 2)
print(arr)

print(np.array_split(arr, 2, axis=0 )) #block level
print(np.array_split(arr, 2, axis=1 )) #row level
print(np.array_split(arr, 2, axis=2)) #column level

print("************************ repear ************************")
arr=np.array([1,2,3])
print(np.repeat(arr,2))
arr=np.array([1])
print(np.repeat(arr,10))
print(np.ones(10)) #same same but diff

arr=np.array([2])
print(np.repeat(arr,10))
print(np.full(10,2)) #same same but diff

arr=np.array([[1,2,3],[4,5,6]])
print(np.repeat(arr,3))
print(np.repeat(arr,3,axis=0))
print(np.repeat(arr,3,axis=1))




arr3d = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])

print(np.repeat(arr3d, 2, axis=0))
print(np.repeat(arr3d, 2, axis=1))
print(np.repeat(arr3d, 2, axis=2))


print("************************ AGGREGATE FUNCTION ************************")
arr=np.array([3,2,1])
arr2=np.array([10,11,12])

print(np.sum(arr))
print(np.average(arr))
print(np.mean(arr))
print(np.median(arr))
# print(np.mode(arr))
print(np.max(arr))
print(np.maximum(arr,arr2))
print(np.min(arr))
print(np.sort(arr))

#boradcasting 
arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[3], [0]])
np.maximum(arr1, arr2)


arr=np.arange(8).reshape(2,2,2)
print(np.sum(arr,axis=0))
print(np.sum(arr,axis=1))
print(np.sum(arr,axis=2))
arr= np.array([1,2,3])
print(np.cumsum(arr))
print(np.cumprod(arr))

print("************************ CODITIONAL OPERATION FUNCTION ************************")
arr=np.array([1,2,4,5,6])
print(np.where(arr>4 ,"high","low"))

arr=np.array([1,2,3,4,5,6]).reshape(2,3) #2d compare
print(np.where(arr>4 ,"high","low"))


arr=np.array([1,2,4,5,6])
print(arr[np.where(arr>4)])
print(np.where(arr>4))

arr=np.array([1,2,4,5,6])
print(np.argwhere(arr>3))

arr=np.array([1,2,3,4,5,6]).reshape(2,3) #2d compare
print(arr)
print(np.argwhere(arr>3)) #position w.r.t arr ie 2 array

arr=np.arange(0,8).reshape(2,2,2)
print(np.argwhere(arr>4)) # co ordinates w.r.t 3 D array


arr=np.array([1,2,4,5,6])
print(np.logical_or(arr>2 , arr<5))

arr=np.array([1,2,3,4,5,6]).reshape(2,3) #2d compare
print(arr)
print(np.logical_or(arr>2 , arr<5)) #position w.r.t arr ie 2 array

arr=np.arange(0,8).reshape(2,2,2)
print(np.logical_or(arr>2 , arr<5)) # co ordinates w.r.t 3 D array




arr=np.array([1,2,4,5,6])
print(np.logical_and(arr>2 , arr<5))

arr=np.array([1,2,3,4,5,6]).reshape(2,3) #2d compare
print(arr)
print(np.logical_and(arr>2 , arr<5)) #position w.r.t arr ie 2 array

arr=np.arange(0,8).reshape(2,2,2)
print(np.logical_and(arr>2 , arr<5)) # co ordinates w.r.t 3 D 
print(arr[np.logical_and(arr>2 , arr<5)])

arr=np.array([0,1,0,2,3,0,4,0,5])
print(np.nonzero(arr)) #gives the index of non zero elements 
print(arr[np.nonzero(arr)]) # gives the non zero values


print("************************ BROADCASTING ************************")
print("same array size or size =1")
arr=np.array([1,2,3,4,5,6,7,8,9,10])
arr= 10+arr
print(arr)
arr2=[[1],[2],[3]]
arr=arr+arr2
print(arr)
status=np.array(['minor','major'])
agearray=np.array([15,18,22,26,27,39])
arr=np.where(agearray>18,status[1],status[0])
print(arr) 




print("************************ VECTORIZATION ************************")
arr=np.array([1,2,3,4,5,6])
print(arr *2)


arr=np.array([1,2,3,4,5,6])
print(arr >2)

def quad(x):
    return x**2+x*2+1
arr=np.array([1,2,3,4,5,6])
vfunc= np.vectorize(quad)
print(vfunc(arr))
