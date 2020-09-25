
#Tuples are just immutable lists. Use () instead of []
x = (1, 2, 3)
print ('len(x):', len(x))

y = (4, 5, 6)
print ('y[2]:', y[2])

listOfTuples = [x, y]
print ('listOfTuples:', listOfTuples)

(age, income) = "32,120000".split(',')
print('age:', age)
print('income:', income)