def produto_cartesiano(A,B):

    r = []

    for x in A:
        for y in B:
            r.append((x,y))
    
    return r


r = produto_cartesiano([0,1,2],['a','b'])
print(r)

