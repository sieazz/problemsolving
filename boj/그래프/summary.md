# 그래프
## 그래프 탐색
DFS(재귀, 스택) / BFS(큐)

## Cycle
그래프 탐색 도중 이미 방문했던 vertex를 다시 방문했을 경우  

Cycle의 길이: 9466   
Cycle의 개수: 10451

## 이분그래프
연결된 두 vertex가 서로 다른 그룹에 속해있어야 함  
탐색하면서 그룹이 지정되지 않은 vertex의 그룹을 지정해주고, 이미 지정된 vertex의 경우 위 조건을 만족하는 지 확인  

1707
## Union-Find
Disjoint set을 나타내는 자료구조
1. 배열 이용  
Edge들을 탐색해가며 edge의 두 vertex를 포함하는 set들의 vertex들을 같은 set에 포함되도록 하기  
2. Tree 이용   
Edge들을 탐색해가며 edge의 두 vertex를 포함하는 tree 두개를 하나로 연결해주기(한 tree의 root를 다른 tree의 root에 연결)  

연결요소: 11724
