# 1 ~ 100 중에서 소수(약수가 1과 자기자신)의 합을 구하시오.

sum = 0
for i in range(1, 100):
    i += 1
    if(i == 2):
        sum += i
        continue
    elif(i % 2 == 0):
        continue
    else:
        for j in range(2, i):
            if(i % j == 0):
                break
            elif(j == i - 1):
                sum += i
print("total sum of prime numbers is {:d}.".format(sum))


""" arr = [i ** 2 for i in range(0, 20, 2)]
print(arr)

lst = []
for i in range(0, 20, 2):
    i = i ** 2
    lst.append([i])

lst = ['사과', '배']
outs = [f for f in lst if f != '사과'] """

cmd = input("Input>> ") ## 입력한 값은 str형이 된다.
print(cmd)

cmds = cmd.split(' ')
print(cmds)


