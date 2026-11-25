D = {'favor' : 1, 'is' : 2, 'lowkey' : 3, 'so' : 4, 'goated' : 10,}

n = int(input("Enter n :"))

res = 0
for k in D.keys():
    if D[k] == n:
        res = res + 1

print("frequency of", n, "is :" + res)

'''
k = key
d[k] : value
'''