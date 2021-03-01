import numpy as np

n = 9
m = 50
successtimes = 0
drawtimes = np.zeros(10000)

for i in range(10000):
    collectionset = np.zeros(n)
    for j in range(m):
        k = np.random.randint(n)
        collectionset[k] = 1
        if np.sum(collectionset) == n:
            successtimes += 1
            drawtimes[i] = j
            break

rate = successtimes/10000
expection = np.sum(drawtimes)/10000
print('The rate of successfully collecting',n,'cards in',m,'draws is',rate*100,'%')
print('The expection of draws is',expection)
