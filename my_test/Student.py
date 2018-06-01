class Student():

    def __init__(self,name,city):
        self.name=name
        self.city=city
        print("My name is %s and come from %s"%(name,city))

    def talk(self):
        print("Hello,51zxw")

print("Student.__doc__:",Student.__doc__)
print("Student.__name__:",Student.__name__)
print("Student.__module__:",Student.__module__)
print("Student.__bases__:",Student.__bases__)
print("Student.__dict__:",Student.__dict__)


