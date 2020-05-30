import sys
sys.stdin = open('t2.txt','r')

N,H = map(int,sys.stdin.readline().split())
G = [0]*H
odd = [0]*H
even = [0]*H
obs = 0
for i in range(N):
    obs = int(input())
    if i % 2 :
        odd[obs-1]+=1
    else :
        even[obs-1]+=1

for i in range(H-2,-1,-1):
    even[i] += even[i+1]
    odd[i] += odd[i+1]

for i in range(H):
    G[i] = even[i] + odd[-i-1]

Min = min(G)
print(Min, G.count(Min))

