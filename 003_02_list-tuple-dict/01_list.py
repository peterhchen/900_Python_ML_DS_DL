x = [1, 2, 3, 4, 5, 6]
print('x:', x)              # [1, 2, 3, 4, 5, 6]
print('len(x):', len(x))    # 6
print('x[:3]:', x[:3])      # [1, 2, 3]
print('x[3:]:', x[3:])      # [4, 5, 6]

# start from index = -2, stop at end, step wit 1
print('x[-2:]:', x[-2:])    # [5, 6]

# start from 0, stop at before -1 (6), step with 1
print('x[:-1:]:', x[:-1:])  # [1, 2, 3, 4, 5]

# start from 0, stop at end, step with -1
print('x[::-1]:', x[::-1]) # [6, 5, 4, 3, 2, 1]

# merge two lists
print('x.extend([7, 8]):')
x.extend([7, 8])
print('x:', x) 
# [1, 2, 3, 4, 5, 6, 7, 8]

# append list
print('x.append(9):')
x.append(9)
print (x) 
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# merge list of two lists
y = [10, 11, 12]
print ('listOfLists = [x, y]:', )
listOfLists = [x, y]
print (listOfLists)
# [[1, 2, 3, 4, 5, 6, 7, 8, 9], [10, 11, 12]]

# print index of array
print ('y[1]:', y[1])

# sort
z = [3, 2, 1]
print ('before z:', z)
print('z.sort():')
z.sort()
print ('after sort z:', z)