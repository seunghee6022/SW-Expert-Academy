import sys
sys.stdin = open('베이비진게임_input.txt','r')

def baby_gin(cards):
    player1, player2 = [0]*10, [0]*10
    f1, f2 = False, False
    for idx, card in enumerate(cards):
        if idx & 1:
            player2[card] += 1
        else:
            player1[card] += 1

        l1 = sum(player1)
        l2 = sum(player2)
        if l1 >= 3 and l2 >=3 :
            print(player1)
            print(player2)
            for i in range(l1-2):
                if player1[i] and player1[i+1] and player1[i+2]:
                    f1 = True
            for i in range(l2-2):
                if player2[i] and player2[i+1] and player2[i+2]:
                    f2 = True
            for i in range(l1) :
                if player1[i] == 3 :
                    f1 = True
            for i in range(l2):
                if player2[i] == 3 :
                    f2 = True

            if f1 and not f2 :
                print("#{} {}".format(tc, 1))
                return
            if f2 and not f1 :
                print("#{} {}".format(tc, 2))
                return
            if f1 and f2 :
                print("#{} {}".format(tc, 0))
                return
    if not f1 and not f2 :
        print("#{} {}".format(tc, 0))
        return

T = int(input())
for tc in range(1,T+1):
    cards = list(map(int,input().split()))
    baby_gin(cards)



