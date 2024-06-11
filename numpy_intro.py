import numpy as np
seznam = [1,5,3]

s=np.array(seznam)
s=s*3
print(s)

seznam = [1,5,3]
vystup = []

for i in seznam:
    ii = i*3
    vystup.append(ii)
print(vystup)

print(seznam)
seznam[1]=100
print(seznam)

vystup =list(map(lambda x: x*3,seznam))
print(vystup)

a=np.full(shape=(3,4,), fill_value=5,dtype=int)
b=np.full(shape=(4,3), fill_value=3,dtype=int)

print(a @ b)