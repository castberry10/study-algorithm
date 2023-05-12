import sys
import heapq
# from collections import deque
input = sys.stdin.readline

# queue = deque()
n = int(input())
m = int(input())
inf = 10 ** 8
dp = [inf for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]
heap = []
prevnode = [[0] for _ in range(n + 1)] 

for i in range(m):
    a, b, c = map(int, input().split()) #출발, 도착, 시간
    graph[a].append((b, c))
    
start, end = map(int, input().split())
# queue.append(start)
def dijkstra():
    global start, end
    
    heapq.heappush(heap, (0, start))
    dp[start] = 0
    
    while heap:
        t, l = heapq.heappop(heap) #time, location  #현 위치 및 시간 
        if dp[l] < t:
            continue
        
        for lp, tp in graph[l]: #갈수 있는 버스(도착지, 소요시간)
            time = t + tp # 소요시간 + 경유지까지 간 시간 = 도착지까지가는 총 시간
            # print(dp)
            # print(dp[lp])
            # print(time)
            
            if dp[lp] > time: #이 지금까지의 도착지까지 가는 총 시간보다 빠르다면? 
                dp[lp] = time
                prevnode[lp] = l
                heapq.heappush(heap, (time, lp))
dijkstra()
# print("----[debug]---")
# print(n, m)
# print("start, end", start,":" ,end)
# print("graph:", graph)
# print("dp:", dp)
path = list()
temp = end
path.append(temp)
while temp != start:
    temp = prevnode[temp]
    path.append(temp)
path.reverse()

print(dp[end])
print(len(path))
print(*path)