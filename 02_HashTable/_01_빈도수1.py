# direct-address table 방식 풀이
def solution (nums):
    answer = -1
    cnt = [0] * 1001 # 0~1000까지 숫자가 제한되어 있기 때문에 나올 수 있는 숫자의 최대 개수 만큼 배열을 미리 초기화

    for x in nums:
        cnt[x] += 1

    # for i in range(1, 1001):
    #     if cnt[i] == 1:
    #         answer = max(answer, i)

    # 큰 수부터 돈다
    # 최초로 발견된 1을 가진 key가 가장 큰 수이므로 바로 return
    for i in range(1000, 0, -1):
        if cnt[i] == 1:
            return i

    return answer

print(solution([3, 9, 2, 12, 9, 12, 8, 7, 9, 12]))
print(solution([2, 1, 3, 2, 1, 3, 4, 5, 4, 5, 6, 7, 6 ,7, 8, 8]))
print(solution([23, 56, 11, 67, 120, 560, 812, 960, 560, 777, 888, 960]))
print(solution([11, 73, 156, 789, 345, 156, 789, 345, 678, 555, 678]))
print(solution([1, 3, 1, 5, 7, 2, 3, 1, 5]))
