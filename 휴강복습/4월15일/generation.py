
# N = int(input())
# result = []
# want = list(map(int,input().split()))
# print(want)
# for i in range(len(want)//2):
#     temp = [want[2*i+0]]*want[2*i+1]
#     result.extend(temp)
#     N -= want[2 * i + 1]
# if N :
#     result.extend([18]*N)
# print(len(result),result)
#
# with open('t2.txt', 'wb') as f:
#     for item in result:
#         f.write("%s\n" % item)


temp = [13, 13, 13, 13, 13, 3, 3, 3, 3, 3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 2, 2, 2, 2, 2, 2, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 55, 55, 55, 55, 55, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18, 18]
for i in range(len(temp)) :
    temp[i] = str(temp[i])
print(len(temp))
print(' '.join(temp))
