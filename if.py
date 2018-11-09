""" score = 80
if score > 70:
    print('합격')
    print('축하합니다.')
elif score == 70:
    print('합격도 아니고 불합격도 아님!')
else:
    print('불합격')
    print('다음 기회에 응시해주세요')
 """


""" score = 100
if score >= 90:
    print('당신의 A학점입니다.')
elif score >= 80:
    print('당신의 B학점입니다.')
elif score >= 70:
    print('당신의 C학점입니다.')
elif score >= 60:
    print('당신의 D학점입니다.')
else:
    print('당신의 F학점입니다.') """


""" for i in range(1, 100): # 1~99까지 for문 반복
    print(i) """

""" for i in range(10):
    print(i) """

fruits = ['오렌지', '사과', '바나나']
""" for x in fruits:
    print(x) """

""" for i in range(0,3):
    print(fruits[i]) """

""" i, sum = 0, 0
while (i >= 0):
    i += 1
    if (i > 10 and i < 20): # i가 11~19사이는 sum을 실시하지 않는다.
        continue
    sum += i
    if ( i == 100):
        print("End!!", sum)
        break """

# 1 ~ 100 까지의 합을 구하라.
""" sum, i = 0, 0                   ## sum = 0
for i in range(0, 100):             ## for i in range(100):
    i += 1                          ## sum = sum + i + 1
    sum += i                        ## print(sum)
print("total sum = ", sum)

i, sum = 0, 0                       ## sum, i = 0, 0
while (i <= 100):                   ## while(i < 100):
    i += 1                          ##   i += 1
    sum += i                        ##   sum  += i
print("total sum = ", sum) """      ## print(sum)

# 1 ~ 100 까지의 홀수의 합을 구하라.
""" i, sum = 0, 0                  
for i in range(100):               ## sum = 0
    if ( i % 2 == 0):              ## for i in range(100): 
        continue                   ##   if(i % 2 == 1):
    else:                          ##    sum = sum + (i + 1)
        sum += i                   ## print(sum)
print("total sum = ", sum)  """ 

""" i, sum = 0, 0                  ## sum, i = 0, 0
while (i <= 99):                  ## while(i < 100):
    i += 1                         ##   i = i + 1
    if (i % 2 == 0):              ##   if(i % 2 == 1):
        continue                   ##      sum = sum + i
    else:                          ## print(sum)
        sum += i
print("total sum = ", sum) """

 ## i, sum = 0, 0
 ## if( i <= 100 and i % 2 == 1) continue필요없음.
 ## sum += i
 ## if ( i == 101):
 ## print("end", sum)
 ## break


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