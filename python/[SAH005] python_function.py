## Try This 이름, 나이, 성별을 입력받아서 "당신의 이름은 {}, 나이는 {}, 성별은 {}입니다." 출력하기

user_input = input("이름, 나이, 성별을 입력하여 주세요. >>>  ")
print("당신이 입력하신 정보는 {} 입니다.".format(user_input))
message = "당신의 이름은 {}, 나이는 {}, 성별은 {}입니다."
user_infor = user_input.split(',')
print(message.format(user_infor[0], user_infor[1], user_infor[2]))

## Try This 두 수를 입력받아, 사칙연산을 수행하는 계산 프로그램을 만드시오.

number_input = input("계산할 식을 입력하여 주세요. ex) 3 + 4 >>> ")
print("당신이 입력하신 계산식은 {} 입니다.".format(number_input))
equation = number_input.split(' ')
if equation[1] == '+':
    rusult = equation[0] + equation[2]
elif equation[1] == '-':
    result = equation[0] - equation[2]
elif equation[1] == '*':
    result = equation[0] * equation[2]
elif equation[1] == '/':
    result = equation[0] / equation[2]
else:
    print("잘못된 수식입니다. 다시 확인하시고 입력해주세요.")

print(number_input, ' = ', )