import time

current_time=time.localtime(time.time())
print("게임시간시작:",time.strftime("%l:%M:%S%p",current_time))