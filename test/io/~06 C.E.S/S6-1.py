temp={"월":15.5,"화":17.0,"수":16.2,"목":12.9,"금":11.0,"토":10.5,"일":13.3}
print("-"*50)
<<<<<<< HEAD:io/~06 C.E.S/S6-1.py
print("  월    화    수    목    금    토    일")
print("-"*50)


for key in temp:
=======
print("월   화   수   목   금   토   일")
print("-"*50)

for key in temp :
>>>>>>> 6286ae282f41c4e9ee3d9dae9f976d8f015b7da2:io/C.E.S/S6-1.py
    print("%6.1f"%temp[key],end="")

print()
print("-"*50)