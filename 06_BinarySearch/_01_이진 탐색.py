# 이진 탐색
# 이진 탐색의 선행 조건: 정렬된 자료
# O(n)으로 하면 효율성 저하
# O(n): 최대 1억번
# O(logn): 27번

def solution(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        if target > nums[mid]:
            left = mid + 1
        elif target < nums[mid]:
            right = mid - 1

    return -1


print(solution([2, 5, 7, 8, 10, 15, 20, 24, 25, 30], 8))
print(solution([-3, 0, 2, 5, 8, 9, 12, 15], 0))
print(solution([-5, -2, -1, 3, 8, 9, 12, 17, 23], 2))
print(solution([3, 6, 9, 12, 17, 29, 33], 3))
print(solution([1, 2, 3, 4, 5, 7, 9, 11, 12, 15, 16, 17, 18], 18))
