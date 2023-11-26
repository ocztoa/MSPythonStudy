from datetime import datetime
<<<<<<< HEAD
=======

>>>>>>> 7e6ec35679269274de91b1c2a0126cbec6b7b96d
today=datetime.now()

print("%s년"%today.year)
print("%s월"%today.month)
print("%s일"%today.day)
print("%s시"%today.hour)
print("%s분"%today.minute)
print("%s초"%today.second)

<<<<<<< HEAD
string=today.strftime("%Y/%m/%d %H::%M:%S")
=======
string=today.strftime("%Y/%m/%d %H:%M:%S")
>>>>>>> 7e6ec35679269274de91b1c2a0126cbec6b7b96d
print(string)