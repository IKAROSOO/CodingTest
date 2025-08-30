# 네트워크 딜레이 타임 (Network Delay Time)

[문제 링크] : https://leetcode.com/problems/network-delay-time/

### 성능 요약

메모리 : 19.3 MB, 시간 : 455 ms

### 분류
1. 다익스트라 (Dijkstra)
2. 최단 경로 (Shortest Path)
3. 그래프 (Graph)
4. 우선순위 큐 (Priority Queue)

### 제출 일자

2025년 8월 30일 22:32

### 문제 설명

<p>
<code>n</code>개의 노드로 구성된 네트워크에서, <code>k</code>번 노드에서 신호를 보냈을 때 모든 노드가 신호를 받는 데까지 걸리는 최소 시간을 구하는 문제입니다. <code>times</code> 배열에는 각 신호가 <code>(출발 노드, 도착 노드, 걸리는 시간)</code> 형태로 주어집니다.
</p>

### 입력

<p>
<code>times</code>: <code>[u, v, w]</code> 형태의 간선 정보 리스트, <code>n</code>: 전체 노드의 개수, <code>k</code>: 신호를 처음 보내는 시작 노드가 함수의 인자로 주어집니다.
</p>

### 출력

<p>
모든 노드가 신호를 받는 데 걸리는 최소 시간을 정수형으로 반환합니다. 만약 모든 노드가 신호를 받는 것이 불가능하다면 -1을 반환합니다.
</p>