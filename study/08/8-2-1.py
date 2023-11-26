def is_prime(n):
    prime=True   #prime의 초깃값은 True
    if n>1:   #n이 2부터 시작
        for i in range(2,n):   #n:2~n-1
            if n%1==0:   #i로 나눈 나머지가 0이면
                prime=False   #prime을 False로 설정
            
    return prime

number=int(input("수를 입력하세요:"))

if is_prime(number):
    print("소수이다!")
else:
    print("소수가 아니다!")