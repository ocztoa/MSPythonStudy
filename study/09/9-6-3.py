import random

me=random.randint(1,6)
computer=random.randint(1,6)
print("나:",me)
print("컴퓨터:",computer)
<<<<<<< HEAD

=======
>>>>>>> 7e6ec35679269274de91b1c2a0126cbec6b7b96d
if me>computer:
    print("나의 승리!")
elif me<computer:
    print("컴퓨터의 승리!")
else:
    print("무승부!")