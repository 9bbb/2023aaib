a = [1,1,2,3,5,8,12,21]
a = [1,1]
for i in range(2,40):
  a.append( a[i-1 + a[i-2] ])
    a[i] = a[i-1] + a[i-1 + a[i-2]
print(a)