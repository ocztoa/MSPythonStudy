import time

tm=time.localtime(time.time())
string=time.strftime("%Y-%m-%d %l:%M:%S%p",tm)
print(string)