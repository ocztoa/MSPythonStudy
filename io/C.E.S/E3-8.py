a=int(input("첫번째 숫자를 입력하세요:"))
b=int(input("두번째 숫자를 입력하세요:"))
print("원하는 연산은?")
c=input("+ ,-,*,/ 중 하나를 선택하세요:")

if c=="+" :
    print("%d+%d=%d"%(a,b,a+b))

if c=="-" :
    print("%d-%d=%d"%(a,b,a-b))

if c=="*" :
    print("%d*%d=%d"%(a,b,a*b))

if c=="/" :
    print("%d/%d=%.2f"%(a,b,a/b))

else : 
    print("선택 오류!")