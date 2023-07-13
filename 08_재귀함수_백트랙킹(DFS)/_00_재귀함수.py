def DFS1(n):
    if n == 0:
        return
    else:
        print(n, end=' ')
        DFS1(n - 1)

DFS1(5) # 5 4 3 2 1


# 재귀함수는 스택을 사용해서 작동한다.
def DFS2(n):
    if n == 0:
        return
    else:
        DFS2(n - 1)
        print(n, end=' ')

DFS2(5) # 1 2 3 4 5