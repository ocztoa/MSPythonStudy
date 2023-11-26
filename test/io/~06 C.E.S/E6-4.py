year_sale={"2016":237,"2017":98,"2018":158,"2019":233,"2020":120}

big_year=2016
biggest=year_sale["2016"]
for key in year_sale:
<<<<<<< HEAD:io/~06 C.E.S/E6-4.py
    if year_sale[key]>big_year:
        bog_year=key
        biggest=year_sale[key]

print("판매량이 가장 많은 해ㅣ%s년"%big_year)
=======
    if year_sale[key]>biggest:
        big_year=key
        biggest=year_sale[key]

print("판매량이 가장 많은 해:%s년"%big_year)
>>>>>>> 6286ae282f41c4e9ee3d9dae9f976d8f015b7da2:io/C.E.S/E6-4.py
print("판매량:%d대"%biggest)