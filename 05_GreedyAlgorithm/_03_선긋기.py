# 시작점들을 우선 정렬한다.
# 0에서 가장 멀리 갈 수 있는 선을 찾는다.
# 0~첫번째선의 끝점이 시작점인 선들 중에서 가장 멀리 갈 수 있는 선을 찾는다.
def solution(m, nums):
    answer = 0
    n = len(nums) # 선의 개수
    nums.sort(key = lambda v : v[0])
    start = end = i = 0

    while i < n:
        while i < n and nums[i][0] <= start:
            end = max(end, nums[i][1])
            i += 1
        answer += 1
        if end == m:
            return answer
        start = end

    return answer

print(solution(12, [[5, 10], [1, 8], [0, 2], [0, 3], [2, 5], [2, 6], [10, 12], [7, 12]]))
print(solution(15, [[1, 10], [0, 8], [0, 7], [0, 10], [12, 5], [0, 12], [8, 15], [5, 14]]))
print(solution(20, [[3, 7], [5, 8], [15, 20], [0, 5], [7, 14], [3, 10], [0, 8], [13, 18], [5, 9]]))
print(solution(30, [[5, 7], [3, 9], [2, 7], [0, 1], [0, 2], [0, 3], [19, 30], [8, 15], [7, 12], [13, 20]]))
print(solution(25, [[10, 15], [15, 20], [5, 15], [3, 16], [0, 5], [0, 3], [12, 25]]))