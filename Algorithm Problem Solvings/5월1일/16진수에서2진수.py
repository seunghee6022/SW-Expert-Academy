def convert(num):
    if num.isdisit():
        num = int(num)
    else :
        num = 10 + ord(num.upper()) - ord('A')

    temp = ""
    for j in range(3,-1,-1):
        temp += '1' if (num & (1<<j)) else '0'

