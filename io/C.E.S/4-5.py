number=input("숫자를 입력하세요:")

total=0

for a in number :
    a=int(a)
    if a%2!=0 :
      total=total+1

print("홀수의 개수:%d개"%total)