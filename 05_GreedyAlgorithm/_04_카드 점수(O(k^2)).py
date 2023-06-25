# 정확성만 고려한 방식
def solution(nums, k):
    answer = 0
    n = len(nums)
    for i in range(k+1):
        sumN = 0
        for j in range(i): # 맨 앞부터 돌기
            sumN += nums[j]
        for j in range(n-k+i, n): # 중간부터 돌기
            sumN += nums[j]
        answer = max(answer, sumN)

    return answer


print(solution([2, 3, 7, 1, 2, 1, 5], 4))
print(solution([1, 2, 3, 5, 6, 7, 1, 3, 9], 5))
print(solution([1, 30, 3, 5, 6, 7], 3))
print(solution([1, 2, 15, 3, 6, 7, 8, 9], 5))
print(solution([12, 5, 6, 12, 34, 35, 13, 3, 7, 8, 9], 7))
