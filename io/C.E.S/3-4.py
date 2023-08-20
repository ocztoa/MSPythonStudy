a=int(input("첫번째 숫자를 입력하세요:"))
b=int(input("두번째 숫자를 입력하세요:"))
c=a+b
print("%d+%d=%d" %(a,b,c))
if c%3==0 :
    print("%d은(는) 3의 배수이다." %c)
else :
    print("%d은(는) 3의 배수가 아니다." %c)
