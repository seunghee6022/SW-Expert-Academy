import sys
sys.stdin = open('dummy.txt','r')

def PassWord(k):
    if N//4 == k :
        return
    else :
        for p_i in range(k, N-((N//4)-1)+k, N//4):
            pw_sum = 0
            for i in range(N//4):
                idx = p_i + (N//4)-1 - i

                if PW[idx].isalpha():
                    num = ord(PW[idx]) - ord("A") + 10
                    pw_sum += num * (16 ** i)
                else:
                    pw_sum += int(PW[idx]) * (16 ** i)

            PWS.add(pw_sum)
        PassWord(k+1)

T = int(input())
for tc in range(1,T+1):
    N , K = map(int,input().split())
    temp = [x for x in input()]
    PW = temp[-((N//4)-1) :]+temp
    PWS = set()
    PassWord(0)
    result = sorted(list(PWS),reverse = True)
    print("#{} {}".format(tc, result[K-1]))