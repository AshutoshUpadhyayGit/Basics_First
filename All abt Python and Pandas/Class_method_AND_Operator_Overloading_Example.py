
class Employee:
    amount = 5000

    def __init__(self, first, second, sal, post):
        self.first = first
        self.second = second
        self.sal = sal
        self.post = post

    def increment(self):
        if self.post == 'Developer':
            return self.sal + self.amount
        else:
            return self.sal + Employee.amount

    @classmethod
    def from_preprocessing(cls, emp_str):
        first, second, sal, post = emp_str.split("-")
        return cls(first, second, int(sal), post)

    # Operator Overloading
    def __add__(self, other):
        first = self.first + other.first
        post = self.post + other.post
        return "{0}({1},{2})".format("Employee", first, post)


e1 = Employee.from_preprocessing("Ashu-Upa-500000000-Developer")
e1.amount = 7000
print("Incremented salary for : " + e1.first + " is: " + str(e1.increment()))

e2 = Employee.from_preprocessing("Raj-Sin-10000000-Manager")
print("Incremented salary for : " + e2.first + " is: " + str(e2.increment()))

print(e1 + e2)
print(type(e1 + e2))