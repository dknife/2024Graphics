for i in [1, 1.1, 'test', 1, 2, 3, 4, [1, 2, 3] ] :
    print(i)

presidents = ['이승만', '윤보선', '박정희', '최규하', '전두환', '노태우', '김영삼', '김대중', '노무현', '이명박', '박근혜', '문재인', '윤석열']

print(presidents)

for president in presidents:
    print(president)

print(presidents[3])

presidents.sort()
print(presidents)
