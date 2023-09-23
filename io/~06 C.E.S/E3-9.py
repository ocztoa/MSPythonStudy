a=int(input("점수를 입력하세요:"))

if a>=90 and a<=100 :
    print("-성적:%d점/등급:수"%a)

elif a>=80 and a<=89 :
    print("-성적:%d점/등급:우"%a)

elif a>=70 and a<=79 :
    print("-성적:%d/등급:미"%a)

elif a>=60 and a<=69 :
    print("-성적:%d/등급:양"%a)

elif a>=0 and a<=59 :
    print("-성적:%d/등급:가"%a)

else :
    print("입력 오류!")