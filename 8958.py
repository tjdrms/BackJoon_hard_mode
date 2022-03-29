n=int(input())
for i in range(n):
    b=input()
    OX_list=list(b)
    sum=0
    count=1
    for i in OX_list:
        if i=="O":
            sum+=count
            count+=1
        else:
            count=1
    print(sum)
