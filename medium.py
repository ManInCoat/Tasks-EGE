fib = [1, 2]
while fib[-1]< 1000:
    fib.append(fib[-2] + fib[-1])
def dec_to_Fib(n):
    ik = 0
    res = ''
    for i in range(len(fib)):
        if fib[i] > n:
            ik = i - 1
            break
    for i in range(ik, -1, -1):
        if n >= fib[i]:
            res += '1'
            n = n - fib[i]
        else:
            res += '0'
    return res
mx = 0
for num in range(1,1001):
    r = dec_to_Fib(num)
    if r.count('1') % 2 == 0:
        r = r + '11'
    else:
        r = '11' + r
    if int(r, 2) > mx:
        mx = int(r, 2)
print(mx)
