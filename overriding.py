#1

class Employee:
    def __init__(self, nm , sal):
        self.name=nm
        self.salary=sal
    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
        
class SalesOfficer(Employee):
    def __init__(self, nm, sal, inc):
        super().__init__(nm, sal)
        self.incnt = inc
    def getSalry(self):
        return self.salary + self.incnt
        
e1 = Employee("Harsh",10000)
print("Total salary for {} is Rs {}".format (e1.getName(),e1.getSalary()))
s1 = SalesOfficer("Yash",20000, 2000)
print("Total salary for {} is Rs {}".format(s1.getName(),s1.getSalary()))        
    
#2 seek & get

class car:
    def __init__(self,a=40):
        self.speed = a
        def get_speed(self):
            return self.speed
        def set_speed(self,a):
            self.speed = a
        return
    