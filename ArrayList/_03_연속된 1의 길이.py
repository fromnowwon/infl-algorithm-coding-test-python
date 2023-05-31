def solution(nums):
    cnt = 0
    answer = 0

    for x in nums:
        if x == 1:
            cnt += 1
        else:
            answer = max(answer, cnt)
            cnt = 0

    # 마지막 요소까지 끝났을 때, 1이면 answer와 cnt를 비교하는 로직이 적용되지 않으므로
    # 한 번 더 비교해준다.
    answer = max(answer, cnt)

    return answer

print(solution([1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1]))
print(solution([0, 0, 1, 0, 1, 0, 0]))
print(solution([1, 1, 1, 1, 1]))
print(solution([1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1]))