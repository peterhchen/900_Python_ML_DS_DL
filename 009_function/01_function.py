def SquareIt(x):
    return x * x

print('SquareIt(2):', SquareIt(2))

#You can pass functions around as parameters
def DoSomething(f, x):
    return f(x)

print('DoSomething(SquareIt, 3):')
print(DoSomething(SquareIt, 3))

#Lambda functions let you inline simple functions
print('DoSomething(lambda x: x * x * x, 3):')
print(DoSomething(lambda x: x * x * x, 3))