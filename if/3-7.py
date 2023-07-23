spend=int(input("구매금액은?"))
if 10000<=spend<50000 :
    rate=5.0
elif 50000<=spend<300000 :
    rate=7.5
elif 300000<=spend :
    rate=10.0
else :
    rate=0
discount=spend*rate/100
pay=spend-discount
print("구매금액:%.0f"%spend)
print("할인율:%.1f"%rate)
print("할인금액:%.0f"%discount)
print("지불금액:%.0f"%pay)

