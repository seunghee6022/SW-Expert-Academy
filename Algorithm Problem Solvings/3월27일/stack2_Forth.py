import sys
sys.stdin = open('t.txt','r')

T = int(input())
for tc in range(1,T+1):
    formula = [x for x in input().split()]
    stack = []
    for f in romula :
        if f.isdecimal(): 
            stack.append(int(f))
        else :
            if len(stack)>=2 :
                while len(stack)>=2 :
                    if f in ['+','-','/','*']:
                        p2 = stack.pop()
                        p1 = stack.pop()
                        if f == '+' : stack.append(p1+p2)
                        elif f == '-' : stack.append(p1-p2)
                        elif f == '*' : stack.append(p1*p2)
                        elif f == '/' : stack.append(p1//p2)
                    else : result = 'error'; break
                            
                if f == . : result = 'error'; break
            else :
                result = 'error'
