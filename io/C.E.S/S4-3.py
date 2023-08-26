start=int(input("시작 수를 입력해주세요:"))
end=int(input("끝 수를 입력해주세요:"))
a=start

while a<=end+1 :
    prime_yes=True
    for i in range(2,a): # 2부터 a(소수인지 알고싶은 수)-1까지 중에 a의 약수가 있는지
        # a의 약수가 있다는 건 ? a를 그 수로 나눴을떄 나누어 떨어지는지 
        if a%i==0:
            prime_yes=False
            break

    if prime_yes:
        print(a,end=" ")

    a=a+1