a=int(input("수를 입력하세요:"))
if a<10 and a>=0 :
    print("%d은(는) 한자리 숫자이다."%a)
elif a>=10 and a<100 :
    print("%d은(는) 두자리 숫자이다."%a)
elif a>=100 and a<1000 :
    print("%d은(는) 세자리 숫자이다."%a)
else :
    print("오류! %d은(는) 범위(0~999) 이외의 숫자이다."%a)