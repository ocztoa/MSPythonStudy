<<<<<<< HEAD:io/~06 C.E.S/E6-7.py
person={"name":"홍길동","age":30,"family":5,"children":["선미","성진","소영",],"pets":["강아지","고양이","이구아나"]}
=======
person={"name":"홍길동","age":30,"family":5,"children":["선미","성진","소영"],"pets":["강아지","고양이","이구아나"]}
>>>>>>> 6286ae282f41c4e9ee3d9dae9f976d8f015b7da2:io/C.E.S/E6-7.py

for key in person:
    if key=="pets":
        for name in person[key]:
            print(name,end="/")