def discount(price,discount)-> int:
    newpice = (price*discount)/100
    v = price - newpice
    return v

print(discount(50,10))