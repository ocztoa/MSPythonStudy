temp={"월":15.5,"화":17.0,"수":16.2,"목":12.9,"금":11.0,"토":10.5,"일":13.3}

smallest=temp["월"]
<<<<<<< HEAD:io/~06 C.E.S/S6-2.py
=======

>>>>>>> 6286ae282f41c4e9ee3d9dae9f976d8f015b7da2:io/C.E.S/S6-2.py
for key in temp:
    if temp[key]<smallest:
        day=key
        smallest=temp[key]

<<<<<<< HEAD:io/~06 C.E.S/S6-2.py
print("요일:%s,최저기온:%.1f"%(day,smallest))
=======
print("요일:%s,최저 기온:%.1f"%(day,smallest))
>>>>>>> 6286ae282f41c4e9ee3d9dae9f976d8f015b7da2:io/C.E.S/S6-2.py
