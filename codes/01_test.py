# 이것은 나의 첫 파이썬 코드

print('신난다 코딩!')
print("신난다 코딩!!")

a = 1234
b = 1234
print(a*b)

## 흐름 제어
age = int(input('너의 나이는?'))

if age >= 18 : 
    print('입장')
    print('3관으로 가세요')
else :
    print('입장이 불가합니다.')
    print('티켓 환불은 1층으로')

## 반복
for i in range(2, 11, 2) :
    print(i)

## 함수