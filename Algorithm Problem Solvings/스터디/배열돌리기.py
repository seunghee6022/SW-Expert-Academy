import sys
import itertools

sys.stdin = open("색종이붙이기.txt", "r")
# laod the input
N, M, K = map(int, sys.stdin.readline().split())
matrix_data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
rotation_data = [list(map(int, sys.stdin.readline().split())) for _ in range(K)]

# set a global maximum for finding the best
# minimum among all permutations
globalMinimum = 1 << 32


matrix_index = None
for perm in itertools.permutations(rotation_data):
    # recreate an index matrix inital values will be same
    # as coordinates matrix_index[5][4] = [5, 4]
    matrix_index = [[[x, y] for y in range(M)] for x in range(N)]
    # go through all single rotations in the permutation
    for rotation in perm:
        # load the rotation data and
        # correct the index
        r, c, s = rotation
        r -= 1
        c -= 1

        # start the rotation from inside to outside
        # and dont touch the center
        for s_ in range(1, s + 1):
            # upperleft
            # switch the value pair by pair
            for dy in reversed(range(c - s_ + 1, c + s_ + 1)):
                matrix_index[r - s_][dy], matrix_index[r - s_][dy - 1] = matrix_index[r - s_][dy - 1], \
                                                                         matrix_index[r - s_][dy]
            # lowerleft
            # switch the value pair by pair
            for dx in range(r - s_, r + s_):
                matrix_index[dx][c - s_], matrix_index[dx + 1][c - s_] = matrix_index[dx + 1][c - s_], matrix_index[dx][
                    c - s_]
            # lowerright
            # switch the value pair by pair
            for dy in range(c - s_, c + s_):
                matrix_index[r + s_][dy], matrix_index[r + s_][dy + 1] = matrix_index[r + s_][dy + 1], \
                                                                         matrix_index[r + s_][dy]
            # upperright
            # switch the value pair by pair
            # here we have to to one switching less because
            # it would bring the last one back to the original spot
            for dx in reversed(range(r - s_ + 2, r + s_ + 1)):
                matrix_index[dx][c + s_], matrix_index[dx - 1][c + s_] = matrix_index[dx - 1][c + s_], matrix_index[dx][
                    c + s_]

    # calculate the minimum for this permutation
    localMinimum = 1 << 32
    tempSum = 0

    print("\nPermutation: ", perm, ":")
    for x in range(N):
        tempSum = 0

        for y in range(M):
            # get the real data with the coordinates
            # from the index matrix
            idx, idy = matrix_index[x][y]
            tempSum += matrix_data[idx][idy]
            print(matrix_data[idx][idy], end="")
        print()
        if tempSum < localMinimum:
            localMinimum = tempSum
    print("Minimum:", localMinimum)
    if localMinimum < globalMinimum:
        globalMinimum = localMinimum

print(globalMinimum)