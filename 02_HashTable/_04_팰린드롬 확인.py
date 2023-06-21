# 팰린드롬(회문)
# 모두 짝수개 있으면 무조건 팰린드롬 가능
# 홀수개인 문자가 하나 있다면 무조건 팰린드롬 가능
from collections import Counter
def solution(str):
    sH = Counter(str)
    odd = 0

    for key in sH:
        if sH[key] % 2 == 1:
            odd += 1

    return odd <= 1

print(solution("abacbaa"))
print(solution("abaaceeffkckbaa"))
print(solution("abcabbcc"))
print(solution("sgsgsgabaaaecececekefefkccckbsgaaffsgsg"))
print(solution("aabcefagcefbcabbcc"))