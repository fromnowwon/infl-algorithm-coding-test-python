# 최솟값의 위치
# O(n)으로 가능
# 배열의 길이가 10만이 넘어가면 O(n2)으로 연산하면 안 되고, O(nlogn) 또는 O(n)으로 연산해야 한다.

# 연산 방법
# 1. minNumber 변수를 10000000으로 초기화 한다. (최대 정수 값이 10000000이기 때문에)
# 2. if nums[i] < minNumber일 때 minNumber에 nums[i]를 넣는다.
# 3. minNumber가 교체될 때마다 answer 변수에 인덱스 i를 넣는다.

def solution(nums):
    answer = 0
    minNumber = 1000000000
    n = len(nums)
    for i in range(n):
        if nums[i] < minNumber:
            minNumber = nums[i]
            answer = i

    return answer

print(solution([7, 10, 5, 3, 2, 15, 19]))
print(solution([-12, 12, 30, -15, -5, 3, 9, -11, 14]))
print(solution([17, 11, 5, 8, 23, 29, 19, 12, 25, 16, 2]))
print(solution([7, 5, 12, -9, -12, 22, -30, -35, -21]))
