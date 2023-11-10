from math import sqrt
def circle_or_square(circler , squarea):
    d = sqrt(squarea)
    v = d * 4 
    circled = 3.14 * circler * 2 
    if circled > v :
        return True 
    else : 
        return False 
print(circle_or_square(8, 144))