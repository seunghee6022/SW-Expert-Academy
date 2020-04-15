import sys
sys.stdin = open('수열합치기_input.txt.','r')

def printlist(lst):
    cur = lst.head
    while cur != None:
        print(cur.data, end='->')
        cur = cur.next
    print()


def printreverse(lst):
    print("#{}".format(tc),end=' ')
    cur = lst.tail
    for _ in range(9) :
        print(cur.data, end=' ')
        cur = cur.pre
    print(cur.data)


def MakeNode(lst, arr):
    #first와 last를 만들어서 나중에 새로들어올 arr와 연결하기 용이
    first = last = Node(arr[0])
    for i in arr[1:]:
        new = Node(i, last)
        last.next = new
        last = new
    lst.size += len(arr)

    # 빈 노드일 때
    if lst.head == None :
        lst.head = first
        lst.tail = last

    # 빈 노드 아닐 때
    else :
        cur = lst.head
        while cur.next != None :
            if cur.next.data > arr[0] :
                break
            cur = cur.next

        # 맨 처음
        if cur.pre == None :
            last.next = cur
            cur.pre = last
            lst.head = first
        # 맨 마지막
        elif cur == lst.tail :
            cur.next = first
            first.pre = cur
            lst.tail = last
        # 중간
        else :
            last.next = cur.next
            cur.next.pre = last
            cur.next = first
            first.pre = cur

    #
    # print(lst.head.data, lst.tail.data)
    # printlist(lst)


T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())

    class Node():
        def __init__(self, d = 0, p = None, n = None):
            self.pre = p
            self.next = n
            self.data = d

    class LinkedList():
        def __init__(self):
            self.head = None
            self.tail = None
            self.size = 0

    mylist = LinkedList()


    for i in range(M):
        cur_arr = [int(x) for x in input().split()]
        MakeNode(mylist, cur_arr)
    # printlist(mylist)
    printreverse(mylist)

