# for loop
print ('loop range from 0 to 5:')
for x in range(5):
    print(x)
print()

# for loop with if condition
print ('loop range with condition:')
for x in range(5):
    if (x is 1):
        continue
    if (x > 3):
        break
    print(x)
print()

# while loop
print ('while loop:')
x = 0
while (x < 5):
    print(x)
    x += 1
print ()

# zip looping
# zip return the iterator. 
# We need to convert into list before access.
s1 = {2, 3, 1}
s2 = {'b', 'a', 'c'}

print('s1:', s1)
print('s2:', s2)
zipped = zip(s1, s2)
print('zipped:', zipped)
print('type(zipped):', type(zipped))
print('list(zip(s1, s2)):', list(zip(s1, s2)))
