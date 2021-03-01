a = [1,2,3,5,13,16,22,25,29,31,37,45,56,64,74,75,86,89,96,99]

def findnum(a,num):
    n = len(a)
    low = 0
    high = n - 1
    mid = (high + low)//2
    while(high > low and a[mid] != num):
        if a[mid] > num:
            high = mid - 1
            mid = (high + low)//2
        else:
            low = mid + 1
            mid = (high + low)//2
    if a[mid] == num:
        return mid
    else:
        return None

num = 343
b = findnum(a,num)
print(num,'is at',b,'of list a.')
