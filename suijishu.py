from random import randint
class Die():
    def __init__(self):
        self.sides=6

    def setlength(self,length):
        self.sides=length
        
    def roll_die(self):
        a=randint(1,self.sides)
        print('在1和你设置的长度之间的一个随机数为：'+str(a))



die=Die()
for b in range(1,11):
    die.roll_die()

die.setlength(10)
for b in range(1,11):
    die.roll_die()
        
