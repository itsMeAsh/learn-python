def zero(f=None): #your code here
    #if f is None:
    #    return 0
    #return f(0)
    return 0 if f is None else f(0)

def one(f=None): #your code here
    #if f is None:
    #    return 1
    #return f(1)
    return 1 if f is None else f(1)
    
def two(f=None): #your code here
    #if f is None:
    #    return 2
    #return f(2)
    return 2 if f is None else f(2)

def three(f=None): #your code here
    #if f is None:
    #    return 3
    #return f(3)
    return 3 if f is None else f(3)

def four(f=None): #your code here
    #if f is None:
    #    return 4
    #return f(4)
    return 4 if f is None else f(4)

def five(f=None): #your code here
    #if f is None:
    #    return 5
    #return f(5)
    return 5 if f is None else f(5)

def six(f=None): #your code here
    #if f is None:
    #    return 6
    #return f(6)
    return 6 if f is None else f(6)

def seven(f=None): #your code here
    #if f is None:
    #    return 7
    #return f(7)
    return 7 if f is None else f(7)

def eight(f=None): #your code here
    #if f is None:
    #    return 8
    #return f(8)
    return 8 if f is None else f(8)

def nine(f=None): #your code here
    #if f is None:
    #    return 9
    #return f(9)
    return 9 if f is None else f(9)

def plus(x): #your code here
    return lambda y: y + x

def minus(x):
    return lambda y: y - x

def times(x):
    return lambda y: y * x

def divided_by(x):
    return lambda y: int(y / x)

if __name__=='__main__':
	print(seven(times(five())))
	print(four(plus(nine())))
	print(eight(minus(three())))
	print(six(divided_by(two())))
