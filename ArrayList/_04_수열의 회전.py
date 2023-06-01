# 입력 크기가 10만 이상이면 효율성을 생각하자
# 배열은 파이썬의 list를 사용하면 된다.
# 연산할 때에 deque를 사용했다면 리턴할 때에는 list로 변환한다.

from collections import deque

def solution(nums, k):
    answer = deque(nums)

    for i in range(k):
        answer.append(answer.popleft())

    return list(answer)

print(solution([3, 7, 1, 5, 9, 2, 8], 3))
print(solution([2, 12, 2, 1, 3, 3, 9], 2))
print(solution([1, 2, 5, 4, 6, 7, 9], 6))
print(solution([1, 3, 6, 8, 14, 2, 1, 7], 5))
