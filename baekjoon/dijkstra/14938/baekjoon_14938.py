import sys
import heapq

input = sys.stdin.readline

# 지역 개수, 수색 범위, 경로 개수
n_node, dist_limit, n_route = map(int, input().split())

# 아이템의 수
n_items = list(map(int, input().split()))
n_items = [0] + n_items

INF = float('inf')
graph = [[] for _ in range(n_node+1)]

# 길이 개수만큼
for i in range(n_route):
    u, v, w = map(int,input().split())
		# 시작 인덱스에 (이동 지역, 웨이트) 저장
    # 양방향이라 두 번 수행
    graph[u].append((v, w))
    graph[v].append((u, w))

def dijkstra(start):
  # 거리 리스트 생성
  distance = [INF] * (n_node + 1)
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
          # 이전에 저장한 다음 인덱스까지 가는 경로보다 짧다면
          if alt < distance[v]:
              # 원래 저장된 거리를 새 거리로 교체
              distance[v] = alt
              # 새로운 경로를 힙 리스트에 업데이트
              heapq.heappush(queue, (alt, v))
  items = 0
  for i, dist in enumerate(distance):
		# 경로 중에 수색 범위보다 거리가 작은 경로에 한해서만 아이템 저장
    if dist <= dist_limit:
      items += n_items[i]
  return items

result = []
for start in range(1, n_node+1):
  items = dijkstra(start)
  result.append(items)

# 가장 아이템 많이 얻는 값 리턴
print(sorted(result)[-1])