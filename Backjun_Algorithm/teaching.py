import sys
sys.stdin = open('teaching.txt','r')

n , k = map(int, input().split())
basic = set(('a','n','t','i','c'))
k -= 5
words = []
letters = set()

for i in range(n):
    word = input()[4:-4]
    temp = set()
    for w in word:
        if w not in basic :
            temp.add(w)
            letters.add(w)
    words.append(temp)

check = []
l =len(letters)
for i in range(1<<l):
    temp = []
    for j in range(1<<l+1):
        if i&(1<<j) :
            print(letters[j], end = "")
            temp.extend(list(letters)[j])
            if len(temp)==k : break
    check.append(temp)

MAX = 0
for ch in check :
    count = 0
    for word in words :
        if word - set(ch) == set() : count+=1
    if MAX < count: MAX = count
print(MAX)