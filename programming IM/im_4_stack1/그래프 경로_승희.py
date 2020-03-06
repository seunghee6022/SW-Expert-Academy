T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    result = 0
    path = [[0] * (V + 1) for _ in range(V + 1)]

    for _ in range(E):
        i, j = map(int, input().split())
        path[i][j] = 1

    Start, End = map(int, input().split())
    stack, visited = [Start], [False] * (V + 1)
    visited[Start] = True
    next = Start

    while len(stack) > 0 or result == 0:
        for j in range(1, V + 1):
            if path[next][j] == 1 and visited[j] == False:
                stack.append(j)
                visited[j] = True
                next = j
                if j == End: result = 1; break
                break
        if len(stack) > 0:
            next = stack[-1]
            stack.pop(-1)

    print("#{} {}".format(tc, result))