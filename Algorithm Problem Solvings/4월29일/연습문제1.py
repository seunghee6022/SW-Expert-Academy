num='0000000111100000011000000111100110000110000111100111100111111001100111'
l = len(num)
result = 0
ii = 0
for i in reversed(range(len(num))):
    if ii < 7 :
        if num[i] == '1':
            result += 2**ii
            ii+=1
        if ii == 6 :
            print(result, end=' ')
            ii = 0
            result = 0

