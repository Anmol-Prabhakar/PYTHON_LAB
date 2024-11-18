def length(num):
    len = 0
    while(num!=0):
        len = len + 1
        num //= 10
    return len

lower = 1
upper = 1000

for num in range(lower, upper + 1):
    sum = 0
    temp = num
    len = length(num)

    while(temp>0):
        digit = temp%10
        sum += digit ** len
        temp //=10

    if(num == sum): print(num)