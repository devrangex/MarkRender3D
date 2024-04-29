import random

while True:
    # 1부터 10 사이
    a = random.randrange(1, 10 + 1)
    # 1부터 10사이
    b = random.randrange(1, 10 + 1)
    
    # 사칙연산 랜덤(1부터 3까지)
    # 1일경우 +
    # 2일경우 -
    # 3일경우 *
    op = int(random.randrange(1, 3+1))
    
    # 사칙연산 결과를 담을 변수
    c = 0
    
    #1, 2, 3 일 경우 각각 연산을 해준다.
    if op == 1:
        print(a," + ",b, "=")
        c = a + b
    elif op == 2:
        print(a," - ",b, "=")
        c = a - b
    elif op == 3:
        print(a," * ",b, "=")
        c = a * b
    
    # 정답 입력
    d = input('정답은?')
    
    # end 입력시 종료
    if d == 'end':
        break
    # str로 변환한 이유는 결과값이 -연산일때 같이 계산해주기 위함
    elif d == str(c):
        print('정답입니다.')
    else:
        print('오답입니다.')
    