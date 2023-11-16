n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(0, m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)


def dfs(i):
	# 연결된 노드 탐색하면서
  for j in graph[i]:
		# 탐색하지 않은 노드가 있다면
    if not visited[j]:
			# 촌수를 더한다
      visited[j] = visited[i] + 1
			# 연결된 노드에 대해서 동일한 방법으로 탐색한다
      dfs(j)


dfs(a)

if visited[b] == 0:
  print(-1)
else:
  print(visited[b])