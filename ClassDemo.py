class Employee:

    def __init__(self,first_name,last_name,salary):
        self.first = first_name
        self.last = last_name
        self.sal= salary
        self.email = first_name + '.' + last_name + '@company.com'


    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp1 =  Employee('krishna','polavarapu',25000)
print(emp1.email)
		#new comment added
        print(emp1.fullname())
# print(Employee.fullname(emp1))

# emp2 =  Employee()
# emp1.first_name = 'krishna'
# emp1.last_name = 'polavarapu'
# emp1.salary =  40000

# emp2.first_name = 'prasad'
# emp2.last_name = 'polavarapu'
# emp1.salary = 30000

# print(emp1.salary)
# print(emp2.last_name)
