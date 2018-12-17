## Try This 점수를 주면 학점을 보여주는 코드를 작성
import random

point = random.randrange(50, 100)
print("당신의 점수는 {:d}입니다.".format(point))
if point == 100:
    print("축하합니다. 당신은 수석입니다.\n당신의 학점은 A+ 입니다.")
elif point >= 90:
    print("당신의 학점은 A 입니다.")
elif point >= 80:
    print("당신의 학점은 B 입니다.")
elif point >= 70:
    print("당신의 학점은 C 입니다.")
elif point >= 60:
    print("당신의 학점은 D 입니다.")
else:
    print("당신은 이번 학기 과목 수료에 실패했습니다. 여행을 떠나세요.")

## Try This 1~100 까지의 합을 구하시오.
i, sum = 0, 0
while i <= 100:
    i += 1
    sum += i
print('1 ~ 100 까지의 합은 {:d}입니다.'.format(sum))

## Try This 1 ~ 100까지의 홀수의 합을 구하시오.
i, sum = 0, 0
while i <= 100:
    i += 1
    if i % 2 == 0:
        continue
    else:
        sum += i
print("1 ~ 100 까지의 홀수의 합은 {:d}입니다.".format(sum))

## Try This 1 ~ 100 까지의 소수의 합을 구하시오.
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
print("Total sum of prime numbers is {:d}.".format(sum))

sum = 0
for i in range(1, 101, 2):
    print(i)
    sum =+ i
    print("......", sum)
print(sum)