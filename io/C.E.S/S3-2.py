hour1=int(input("첫번째 시간의 시를 입력하세요:"))
minute1=int(input("첫번째 시간의 분을 입력하세요:"))
hour2=int(input("두번째 시간의 시를 입력하세요:"))
minute2=int(input("두번째 시간의 분을 입력하세요:"))

if hour1<hour2 :
    first_hour=hour1
    first_minute=minute1
    second_hour=hour2
    second_hour=minute2

elif hour1<hour2 :
    if minute1<=minute2 :
        first_hour=hour1
        first_minute=minute2

elif hour1==hour2 :
    if minute1<=minute2:
        first_hour=hour1
        first_minute=minute1
        second_hour=hour2
        secod_minute=minute2
    else :
        first_hour=hour2
        first_minute=minute2
        second_hour=hour1
        secod_minute=minute1

else :
    first_hour=hour2
    first_minute=minute2
    second_hour=hor