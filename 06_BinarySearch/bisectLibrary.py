from bisect import bisect_left, bisect_right

# 이진 탐색을 해주는 라이브러리
# bisect_left: low bound search
# bisect_right: upper bound search
def solution(nums, weight):
    answer = bisect_left(nums, weight)
    answer = bisect_right(nums, weight)
    return answer


print(solution([70, 80, 80, 80, 80, 90, 90, 90], 79))
