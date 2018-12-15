print('Hello, World!')
message = 'Hello, World!'
print('message = ', message)
print('message[0:7] = ', message[0:7])
print('message[:7] = ', message[:7])
print('message[:-7] = ', message[:-7])
print('len(message) = ', len(message))
print('message[7:len(message)] = ', message[7:len(message)])
print('message.split(' ') = ', message.split(' '))

first, second = message.split(' ')
print('first = ', first)
print("second = ", second)
print('first * 3 + second = ', first * 3 + second)
print('first < second = ', first < second)

print('Num is using d {:05d}'.format(23))
print('Num is using f {:05f}'.format(23))
print('Num is using b {:05b}'.format(23))
print('Num is using o {:05o}'.format(23))
print('Num is using x {:05x}'.format(23))
print('Num is using % {:05%}'.format(23))
print('당첨확률은 {:.0%}입니다.'.format(.23))

## Introducing Python 2. int, str, variables
seconds_per_hour = 60 * 60
print('seconds_per_hour = 60 * 60 = ', seconds_per_hour)
print('1day = 24 * seconds_per_hour = {}'.format(24 * seconds_per_hour))
seconds_per_day = 24 * seconds_per_hour
print('seconds_per_day = ', seconds_per_day)
print('seconds_per_day / seconds_per_hour = {}'.format(seconds_per_day / seconds_per_hour))
print('seconds_per_day // seconds_per_hour = {}'.format(seconds_per_day // seconds_per_hour))