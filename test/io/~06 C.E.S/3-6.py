a=int(input("수를 입력하세요:"))
<<<<<<< HEAD:io/C.E.S/3-6.py

if a // 10 == 0:
    print("%d은(는) 한자리 숫자이다."%a)

elif a // 100 == 0:
    print("%d은(는) 두자리 숫자이다."%a)

elif a // 1000 == 0 :
    print("%d은(는) 세자리 숫자이다."%a)

else :
    print("오류!%d은(는) 밤위(0~999) 이외의 숫자이다."%a)

=======
if a<10 and a>=0 :
    print("%d은(는) 한자리 숫자이다."%a)
elif a>=10 and a<100 :
    print("%d은(는) 두자리 숫자이다."%a)
elif a>=100 and a<1000 :
    print("%d은(는) 세자리 숫자이다."%a)
else :
    print("오류! %d은(는) 범위(0~999) 이외의 숫자이다."%a)
>>>>>>> a6428986612f42cb411aa56533c4269d2f1265f4:io/E/3-6.py
