"""Questo script fa chiamate a funzioni"""
def f3(x_value):
    """f3 returns a value"""
    global x
    x = 2 * x
    my_value = 4    
    return x_value**2 + my_value + x

def f2(x_value):
    my_value = 0.5
    """f2 returns a value"""
    return f3(x_value*2)+my_value

def f1(x_value):
    """f1 returns a value"""
    return f2(x_value)+1
x = 2
my_value = f1(x)
print(my_value)