import sys
sys.stdin = open('암호_input.txt.','r')
# 원형연결리스트 문제

def printlist(lst):
    cur = lst.head
    for _ in range(lst.size):
        print(cur.data, end='->')
        cur = cur.next
    print()

def printreverse(lst):
    print("#{}".format(tc),end=' ')
    cur = lst.tail
    if lst.size <= 10:
        for _ in range(lst.size-1):
            print(cur.data, end=' ')
            cur = cur.pre

    else :
        for _ in range(9):
            print(cur.data, end=' ')
            cur = cur.pre
    print(cur.data)

def makeNode(lst,arr):
    prev = None
    for i in arr:
        new = Node(i, prev)

        if lst.head == None :
            lst.head = lst.tail = new

        else :
            prev.next = new
            lst.tail = new
        prev = new
        mylist.size += 1
    #원형 연결 리스트 만들기 -> 꼬리와 헤드 잇기
    lst.head.pre = lst.tail
    lst.tail.next = lst.head


def search(lst,M,K):
    cur = lst.head
    for _ in range(K):
        for _ in range(M):
            cur = cur.next
        if cur == lst.head :

            new = Node(cur.data + cur.pre.data, lst.tail, lst.head)
            lst.tail.next = new
            lst.head.pre = new
            lst.tail = new
        else:
            new = Node(cur.data + cur.pre.data, cur.pre, cur)
            cur.pre.next = new
            cur.pre = new
        cur = new
        lst.size+=1






T = int(input())
for tc in range(1,T+1):
    N, M, K = map(int, input().split())
    arr = [int(x) for x in input().split()]

    class Node():
        def __init__(self, d = 0, p = None, n = None):
            self.data = d
            self.pre = p
            self.next = n

    class LinkedList():
        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0
    mylist = LinkedList()
    makeNode(mylist, arr)
    search(mylist, M, K)
    printreverse(mylist)