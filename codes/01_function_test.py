### 밑변과 높이를 받아 직각삼각형의 빗변을 계산하는 함수를 작성하라.

# 빗변 제곱 = 밑변 제곱 + 높이 제곱 (피타고라스 정리) 활용

# ==> 빗변 = 제곱근(높이 제곱 + 밑변 제곱)

import math


def main():
    밑변 = float(input('밑변은?'))
    print(밑변)

    높이 = float(input('높이는?'))
    print(높이)

    빗변 = 빗변계산함수(밑변, 높이) 
    print('빗변은 ', 빗변, '입니다')


def 빗변계산함수(a, b):
    빗변 = math.sqrt(a**2 + b**2)
    return 빗변

main()