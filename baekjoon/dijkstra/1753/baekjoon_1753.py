import sys
import heapq

# 그냥 input() 보다 빠르다고 함
input = sys.stdin.readline

# 정점의 개수와 간선의 개수
n, m = map(int, input().split())
# 출발 노드
k = int(input())
INF = float('inf')

graph = [[] for _ in range(n+1)]

# 간선의 개수 만큼
for _ in range(m):
		# 출발 노드, 도착 노드, 웨이트
    u, v, w = map(int, input().split())
		# 출발 노드 인덱스에 (도착노드, 웨이트) 저장
    graph[u].append((v, w))

# 탐색 전에 graph 리스트 탐색하면서 도착 노드가 같을 때 웨이트 오름차순 sort
for u in range(1, n + 1):
    graph[u] = sorted(set(graph[u]), key=lambda x: x[1])


def dijkstra(start):
    # 거리 리스트 생성
    distance = [INF] * (n + 1)
    # 시작 인덱스 0으로 시작 (시작->시작)
    distance[start] = 0
		# 힙 리스트 생성 (웨이트, 시작인덱스)
    queue = [(0, start)]
		# 힙 리스트에 요소가 남아있을 때까지
    while queue:
				# 지금까지 탐색한 거리, 현재 인덱스
        dist, now = heapq.heappop(queue)
				# 지금까지 탐색한 거리가 이전에 저장된 경로의 거리보다 크다면
				# 이전에 저장된 경로를 유지
        if distance[now] < dist:
            continue
				# 지금까지 탐색한 경로의 길이가 더 짧다면
				# 다음 인덱스까지의 거리들을 보면서
        for v, w in graph[now]:
						# 지금 인덱스에서 다음 인덱스로 바로 가는 거리가
            alt = dist + w
						# 다음 인덱스까지의 원래 저장된 경로보다 짧다면
            if alt < distance[v]:
								# 원래 저장된 경로를 새 경로로 교체
                distance[v] = alt
								# 새로운 다음 경로를 힙 리스트에 업데이트
                heapq.heappush(queue, (alt, v))

    return distance

distance = dijkstra(k)

for i in range(1, n + 1):
    print("INF" if distance[i] == INF else distance[i])