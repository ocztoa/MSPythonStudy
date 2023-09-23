a=int(input("성적을 입력하세요:"))

while a!="q" :
    if a>=90 and a<=100 :
        print("등급:수")

    elif a>=80 and a<=89 :
        print("등급:우")

    elif a>=70 and a<=79 :
        print("등급:미")

    elif a>=60 and a<=69 :
        print("등급:양")

    elif a>=0 and a<=59 :
        print("등급:가")

    x=input("계속하시겠습니까?(중단:q,계속:y)")

    if x=="q":
        break

    a=int(input("성적을 입력하세요:"))