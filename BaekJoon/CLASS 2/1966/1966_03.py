import sys
from collections import deque

# 테스트 케이스의 수 T를 입력받습니다.
T = int(sys.stdin.readline())

for _ in range(T):
    # 문서의 개수 N과 궁금한 문서의 인덱스 M을 입력받습니다.
    n, m = map(int, sys.stdin.readline().split())
    
    # 문서들의 중요도를 입력받아 리스트로 저장합니다.
    priorities = list(map(int, sys.stdin.readline().split()))
    
    # 큐(deque)를 생성하고, (중요도, 원래 인덱스)를 튜플로 묶어 저장합니다.
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    
    # 인쇄 순서를 카운트할 변수를 초기화합니다.
    count = 0
    
    while queue:
        # 큐의 가장 앞에 있는 문서를 꺼냅니다.
        current_doc = queue.popleft()
        
        # 큐에 남아있는 다른 문서들 중에 현재 문서보다 중요도가 높은 것이 있는지 확인합니다.
        # any() 함수는 하나라도 True가 있으면 True를 반환합니다.
        if any(current_doc[0] < other_doc[0] for other_doc in queue):
            # 중요도 높은 문서가 있다면, 현재 문서를 큐의 맨 뒤로 보냅니다.
            queue.append(current_doc)
        else:
            # 현재 문서가 가장 중요도가 높다면, 인쇄합니다.
            count += 1
            
            # 인쇄된 문서가 우리가 찾던 문서(원래 인덱스가 m)인지 확인합니다.
            if current_doc[1] == m:
                # 맞다면, 현재까지의 인쇄 순서를 출력하고 루프를 종료합니다.
                print(count)
                break
