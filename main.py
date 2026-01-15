import numpy as np

# arr = np.array([[['a', 'b', 'c'], ['d', 'e', 'f']],
#                 [['a', 'b', 'c'], ['d', 'e', 'f']]])


# word = arr[0, 0, 0] + arr[0,1,2]



# # print(word)

# array = np.array([[1,2,3,4],
#                   [5,6,7,8],
#                   [9,10,11,12],
#                   [13,14,15,16]])

# #array[start:end:step]

# # print(array[::2]) row

# # print(array[:, ::-1]) column

# print(array[2:, 2:])


####Arithmetic####


# array = np.array([1, 2, 3])

# print(array + 1)
# print(array - 1)
# print(array/5)
# print(array **3)

# print(np.sqrt(array))
# print(np.floor(array))

# print(np.pi)
# radii = np.array([1,2,3])

# print(np.pi * radii **2)

# array1 = np.array([1,2,3])
# array2 = np.array([4,5,6])

# print(array1 + array2)

# scores = np.array([12, 56, 77, 98])

# scores[scores<60] = 0

# print(scores > 60)

# print(scores)

##########BroadCasting#####

# array1 = np.array([[1,2,3,4],
#                    [5,6,7,8],
#                    [9,10,11,12],
#                    [13,14,15,16]])

# array2 = np.array([[1,2],[2,3],[3,4],[4,5]])
# print(array1.shape)
# print(array2.shape)

# print(array1*array2)

# array1 = np.array([[1,2,3,4,5,6,7,8,9,10]])
# array2 = np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

# print(array1.shape)
# print(array2.shape)

# print(array1*array2)

#####Aggregate FUNCTIONS

# array = np.array([[1,2,3,4,5],
#                   [6,7,8,9,10]])

# # print(np.sum(array))
# # print(np.mean(array))
# # print(np.std(array))
# # print(np.var(array))
# # print(np.min(array))
# # print(np.argmin(array))
# # print(np.argmax(array))
# print(np.sum(array, axis=1))

##### FILTERING ####

# ages = np.array([[21,17,16,87,45,15],
#                  [67,22,33,44,99, 17]])

# # teenagers = ages[ages<18]
# # adults = ages[(ages>18) & (ages<65)]
# # seniors = ages[ages>=65]
# # evens = ages[ages%2==0]
# # odds = ages[ages%2!=0]
# # print(odds)

# adults = np.where(ages >= 18, ages, 0)

# print(adults)

##### RANDOM #####

# rng = np.random.default_rng(seed=1)

# print(rng.integers(low=1, high=101, size=(3,2)))
# np.random.seed(1)

# print(np.random.uniform(low = -1, high = 1, size= (3,6)))



### SHUFFLE 
rng = np.random.default_rng()
# array = np.array([1,2,3,4,5])

# rng.shuffle(array)
# print(array)

fruits = np.array(['🍎', '🍊', '🍍'])
fruits = rng.choice(fruits, size=(2,3))
print(fruits)
