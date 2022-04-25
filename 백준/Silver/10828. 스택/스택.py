import sys

n = int(sys.stdin.readline())

stack = []

for _ in range(n):
    word = sys.stdin.readline().split()
    command = word[0]
    
    if command == "push":
        value = word[1]
        stack.append(value)
        
    elif command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
            
    elif command == 'size':
        print(len(stack))
        
    elif command == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
            
    elif command == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])