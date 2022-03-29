a=[]

for i in range(10):
    n=int(input())
    a.append(n % 42)
    
b=set(a)
print(len(b))
