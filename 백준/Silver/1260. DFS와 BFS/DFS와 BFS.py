from collections import deque

n,m,v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    m1, m2 = map(int, input().split())
    graph[m1][m2] = graph[m2][m1] = 1
    
def bfs(start_v):
    d = [start_v]
    queue = deque()
    queue.append(start_v)
    
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for w in range(len(graph[start_v])):
            if graph[v][w] == 1 and (w not in d):
                d.append(w)
                queue.append(w)

def dfs(start_v, d=[]):
    d.append(start_v)
    print(start_v, end=' ')
    
    for w in range(len(graph[start_v])):
        if graph[start_v][w] == 1 and (w not in d):
            dfs(w, d)
            
dfs(v)
print()
bfs(v)