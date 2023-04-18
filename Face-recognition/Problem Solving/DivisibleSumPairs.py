newArr = []
n = 6
k =3
ar = [1, 3, 2, 6, 1, 2]
for i in range(n):
    for x in range(n):
        if (ar[i]+ar[x]) % k == 0:
            if [i,x] and [x,i] not in newArr and x!=i:
                newArr.append([i,x])
print(newArr)
print(len(newArr))