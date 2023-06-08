from collections import Counter
# 홀수개인 문자가 한 개면 문자 길이 만큼 팰린드롬을 만들 수 있다.
# 홀수가 여러 개면 홀수개인 문자 개수 만큼 전체 문자열 길이에서 뺀다.
# 하나의 홀수개인 문자는 가운데에 배치해서 그대로 사용할 수 있기 때문에 +1
def solution(str):
    sH = Counter(str)
    odd = 0

    for key in sH:
        if sH[key] % 2 == 1:
            odd += 1

    return len(str) - odd + 1 if odd > 0 else len(str)

print(solution("abcbbbccaaeee"))
print(solution("aabbccddee"))
print(solution("fgfgabtetaaaetytceefcecekefefkccckbsgaafffg"))
print(solution("aabcefagcefbcabbcc"))
print(solution("abcbbbccaa"))