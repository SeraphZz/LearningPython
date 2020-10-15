def FindMinandMax(L):
    if L == []:
        return(None,None)
    else:
        min = L[0]
        max = L[0]
        for i in L:
            if i > max:
                max = i
            if i < min:
                min = i
        return(min,max)

a = [2,34,4,54,6,57,7687,9,89,8,0]
b = [x*x for x in range(1,11)]
print(FindMinandMax(a))