def func():
    global x
    x=200
    print(x)
    
x=100
func()
print(x)