"""
>>> myadd(3,7.15)
10.15
"""
import math
def myadd(a,b):
    """
    Возвращает сумму
    """
    return a+b

def mysub(a,b):
    '''
    >>> mysub(12,10)
    2
    '''
    return a-b

def mymul(a, b):
    '''
    >>> mymul(2,3)
    6
    '''
    return a * b

def mydiv(a, b):
    if b == 0:
        return 0
    else:
        return a / b

def myqrt3(a):
    return math.pow(a, 1/3)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
