class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age)
        self.job = job

    def job(self):
        if self.job:
            print("%s has a job now" % self.name)
        elif not self.job:
            print("%s has been fired" % self.name)


class Programmer(Employee):
    def __init__(self, name, age, job, programming):
        super(Programmer, self).__init__(name, age, job)
        self.working = programming

    def program(self):
        if self.working:
            print("%s is working. Don\'t try and bother them" % self.name)
        elif not self.working:
            print("%s got done with work early" % self.name)


programmer = Programmer("Marina", 20, True, True)
print(programmer.name)
print(programmer.age)
(Employee.job(programmer))
(programmer.program())
