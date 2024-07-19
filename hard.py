fib = [1, 2]
while fib[-1]< 10000:
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
def Fib_to_dec(s):
    s = s[::-1]
    res = 0
    for i in range(len(s)):
        res += int(fib[i]) * int(s[i])
    return res
count = 0
for num in range(1,1001):
    r = dec_to_Fib(num)
    if r[-1] == '0':
        r = r + '10'
    else:
        r = r + '01'
    if 100 <= Fib_to_dec(r) <= 200:
        count += 1
print(count)
