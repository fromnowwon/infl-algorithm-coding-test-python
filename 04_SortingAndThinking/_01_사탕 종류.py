
def solution(nums):
    n = len(nums)
    cnt = 1 # 첫번째 사탕은 무조건 카운트 되기 때문에
    nums.sort() # 정렬: o(nlogn)

    for i in range(1, n): # 선형 탐색: o(n)
        if nums[i - 1] != nums[i]:
            cnt += 1

    return cnt if cnt < n//2 else n//2 # 몫으로 정수가 반환되도록 '//'를 사용한다. ('/'만 사용하면 소수점까지 나올 수 있음)

print(solution([2, 1, 1, 3, 2, 3, 1, 2]))
print(solution([1, 3, 5, 7, 2, 3, 7, 5, 3, 2, 5, 7, 9, 12]))
print(solution([5, 5, 5, 5, 5, 5]))
print(solution([12, 23, 11, 3, 5, 23, 23, 23, 23, 23, 23, 23]))
print(solution([100, 200, 300, 400, 500, 600, 700, 800]))