# 정확성과 효율성을 고려한 코드 O(nlogn)
# 정렬 후 자신과 인접한 수들만 비교하면 된다. (작은 차를 구하는 것이기 때문에)
def solution(nums):
    answer = []
    n = len(nums)
    minN = 1000000000
    nums.sort() # 오름차순 정렬 (O(nlogn))

    for i in range(1, n): # O(n)
        # 0번째 요소는 1번째 요소에서 비교되기 때문에 반복문에서 제외해도 된다.
        # i에서 i의 앞 요소를 빼준 값을 diff에 넣는다.
        # 오름차순 정렬 되어있기 때문에 절대값 연산은 필요 없다.
        diff = nums[i] - nums[i - 1]
        # 최소 차이 값이 minN에 담긴다.
        minN = min(minN, diff)

    for i in range(1, n): # O(n)
        # 최소 차이 값과 같은 요소의 쌍을 찾는다.
        diff = nums[i] - nums[i - 1]
        if diff == minN: # 최소 차이 값과 같다면 answer에 담는다.
            answer.append([nums[i-1], nums[i]])

    return answer

print(solution([3, 8, 1, 5, 12]))
print(solution([2, 1, 3, 5, 4]))
print(solution([5, 10, 15, 20, 25, 11]))
print(solution([2, 4, 3, 1, 5, 7, 8, 12, 13, 15, 23]))
print(solution([100, 200, 300, 400, 120, 130, 135, 132, 121]))