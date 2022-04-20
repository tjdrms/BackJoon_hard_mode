nums = { x for x in range(2, 10001) if x == 2 or x%2 == 1}
for odd in range(3, 101, 2):
    nums -= {i for i in range(2*odd, 10001, odd) if i in nums}
    
t = int(input())
for _ in range(t):
    n = int(input())
    half = n//2
    for x in range(half, 1 ,-1):
        if (n-x in nums) and (x in nums):
            print(x, n-x)
            break