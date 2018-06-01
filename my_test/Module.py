import random
from time import sleep

from Student import Student

#print(time.ctime())
num=random.randint(1,800)
print(num)
sleep(3)
print("Sleep over!")

stu1=Student('Yxp','XA')
stu1.talk()

stu2=Student('Jack','beijing')
stu2.talk()