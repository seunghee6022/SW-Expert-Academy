import sys
sys.stdin = open('t.txt','r')

def printlist(lst):
    cur = lst.head
    while cur != None:
        print(cur.data, end='->')
        cur = cur.next
    print()

def listpick(lst,idx):
    if idx >= lst.size :
        return -1
    cur = lst.head
    for i in range(idx):
        cur = cur.next
    return cur.data

def Insert(lst,idx,new):

    # 빈 리스트일 때
    if lst.head == None:
        lst.head = lst.tail = new
    #빈 리스트 아니고, 맨 앞 삽입
    elif idx == 0 :
        new.next = lst.head
        lst.head = new

    #마지막에 삽입
    elif idx >= lst.size :
        lst.tail.next = new
        lst.tail = new
        new.next = None

    #중간에 삽입할 때
    else :
        cur = lst.head
        for _ in range(idx-1):
            cur = cur.next
        new.next = cur.next
        cur.next = new

    lst.size+=1

    return

def Delete(lst, idx):

    #빈 리스트일 때
    if lst.head == None : return

    #첫번째 값 삭제
    elif idx == 0:
        lst.head = lst.head.next

    #마지막 값 삭제
    elif idx == lst.size-1 :
        cur = lst.head
        while cur.next != None:
            cur = cur.next

        lst.tail = cur
        cur.next = None

    #중간 값 삭제
    else :
        cur = lst.head
        for _ in range(idx-1):
            cur = cur.next
        cur.next = cur.next.next
    lst.size -= 1
    return

def ChangeData(lst,idx,val):
    cur = lst.head
    for _ in range(idx):
        cur = cur.next
    cur.data = val
    return


T = int(input())
for tc in range(1,T+1):
    N, M, L = map(int,input().split())
    arr = [int(x) for x in input().split()]

    class Node():
        def __init__(self, d = 0, n = None ):
            self.data = d
            self.next = n

    class LinkedList():
        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0

    mylist = LinkedList()

    #링크리스트 생성하기
    pre, cur = None, None
    for i in range(-1,-N-1,-1):
        cur = Node(arr[i],pre)
        pre = cur

        if i == -1:
            mylist.tail = cur
        elif i == -N:
            mylist.head = cur
    mylist.size = N

    for i in range(M):
        require = [x for x in input().split()]
        if require[0] == 'D' :
            Delete(mylist,int(require[1]))
        elif require[0] == 'C' :
            ChangeData(mylist,int(require[1]),int(require[2]))
        else :
            Insert(mylist, int(require[1]), Node(int(require[2])))

    print("#{} {}".format(tc,listpick(mylist,L)))