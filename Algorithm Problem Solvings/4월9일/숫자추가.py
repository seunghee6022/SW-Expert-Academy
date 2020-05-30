import sys
sys.stdin = open('t.txt','r')

def printlist(lst,cur,idx):
    for i in range(idx):
        cur = cur.next
    return cur.data


def InsertAt(mylist,idx,val):
    new = Node(val)
    #빈 리스트일 때, 맨 앞에 삽입
    if mylist.head == None:
        if idx == 0 :
            mylist.head = mylist.tail = new
        else : return

    #맨 뒤에 삽입
    elif mylist.size <= idx:
        new.next = mylist.tail
        mylist.tail = new

    #중간에 삽입
    else :
        cur = mylist.head
        for _ in range(idx - 1):
            cur = cur.next
        new.next = cur.next
        cur.next = new

    mylist.size += 1


T = int(input())
for tc in range(1,T+1):
    N,M,L = map(int,input().split())
    arr = [int(x) for x in input().split()]

    class Node():
        def __init__(self,d=0,n=None):
            self.data = d
            self.next = n

    class LinkedList():
        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0

    mylist = LinkedList()

    pre, cur = None,None
    for i in range(-1,-N-1,-1):
        cur = Node(arr[i], pre)
        pre = cur
        if i == -1 :
            mylist.tail = cur
        elif i == -N:
            mylist.head = cur

    mylist.size = N

    #Insert
    for i in range(M):
        idx, val = map(int,input().split())
        InsertAt(mylist, idx, val)


    print("#{} {}".format(tc,printlist(mylist,mylist.head,L)))
