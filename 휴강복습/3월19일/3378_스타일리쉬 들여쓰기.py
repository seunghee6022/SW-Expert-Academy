import sys
sys.stdin = open('t.txt','r')

T = int(input())
for tc in range(1,T+1):
    p,q = map(int,input().split())

    master=[]
    real_RSC = [0]*3
    RCS = [0]*3
    for i in range(p):
        line = input()
        flag = True
        for l in line:
            while flag:
                
            if l == '(':
                RCS[0]+=1
            elif l == '{':
                RCS[1] += 1
            elif l == '[':
                RCS[2] += 1
            elif l == ')':
                RCS[0] -= 1
            elif l == '}':
                RCS[1] -= 1
            elif l == ']':
                RCS[2] -= 1
        master.append(['('*RCS[0]+'{'*RCS[1]+'['*RCS[2]])



