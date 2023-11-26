import csv    
f = open('MSPythonStudy\PROJECT\data.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
text=(input("날짜를 알고 싶은 사건의 이름:"))
history = {}
for line in rdr:
    history[line[0]] = line[1]
f.close() 
print(history[text])
