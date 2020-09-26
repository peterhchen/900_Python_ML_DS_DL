# ==
print('1 == 3:', 1 == 3)
print('1 == 1:', 1 == 1)
print()

# or, and, not
print('True or False:', True or False)
print('True and False:', True and False)
print('not True:', not True)
print()

# is
print('1 is 3:', 1 is 3)
print('1 is 1:', 1 is 1)
print()

# in
a = [1, 2]
if 1 in a:
    print ('1 in a')
print()

# not in
a = [1, 2]
if 3 not in a:
    print ('3 not in a')
print()

# if ... elif ... else:
if 1 is 3:
    print("How did that happen?")
elif 1 > 3:
    print("Yikes")
else:
    print("All is well with the world")
print ()

# Python does not have switch statement.
# python map to output by dictionary key-value pair.
def east(): return "East"
def west(): return "West"
def north(): return "North"
def south(): return "South"
# map the inputs to the function blocks
switch_case = {
          1 : east,
          2 : west,
          3 : north,
          4 : south
         }
print(switch_case[2]())