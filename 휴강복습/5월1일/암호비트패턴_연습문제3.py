# code = '0DEC'
code ='0269FAC9A0'

pattern = {'0':'001101','1':'010011','2':'111011','3':'110001','4':'100011','5':'110111','6':'001011','7':'111101','8':'011001','9':'101111'}

mapping = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
           '8': '1000', '9': '1001', 'A': '1010','a': '1010', 'B': '1011','b': '1011', 'C': '1100','c': '1100', 'D': '1101','d': '1101', 'E': '1110', 'e': '1110','F': '1111','f': '1111'}

pw = ''
for i in range(len(code)):
    pw+=mapping[code[i]]

result = []
idx = len(pw)-1
while idx :
    if pw[idx] == '1':
        if pw[idx-5:idx+1] in pattern.values() :
            p = [key for (key, value) in pattern.items() if value == pw[idx-5:idx+1]]

            result.append(p[0])
        idx = idx-6
    else :
        idx-=1

print(', '.join(result[::-1]))