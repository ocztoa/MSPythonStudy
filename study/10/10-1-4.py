import os 

if os.path.exsist("sample.txt"):
    os.remove("sample.txt")
else:
    print("파일이 존재하지 않음!")