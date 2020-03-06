import sys
sys.stdin = open('teaching.txt','r')

#check : 배울 수 있는 단어들의 조합
#letters : basic제외 새로 배워야할 알파벳들
#words : 가르치는 단어들


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
list_lettter = list(letters)
l =len(letters)
for i in range(1<<l):
    temp = []
    flag = 0
    for j in range(1<<l+1):
        if i&(1<<j) :
            # print(*list_lettter[j], end=", ")
            flag+=1
            if flag <= k : temp.extend(list_lettter[j])
            else : break
    if flag > k : continue
    if len(temp) == k: check.append(temp)


#     print()
# print(check)
MAX = 0
empty = set()
for ch in check :
    count = 0
    ch_set = set(ch)
    for word in words :
        # print(set(ch) ,word,word - set(ch))
        if word - ch_set == empty : count+=1
    if MAX < count: MAX = count
print(MAX)