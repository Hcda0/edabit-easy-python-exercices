def is_curzon(num):
    v= int(2**num + 1)
    s= int(2* num + 1) 
    z = v/s
    if z.is_integer() :
        return True 
    else : 
        return False 

print(is_curzon(14))