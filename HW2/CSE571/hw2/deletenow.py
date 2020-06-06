# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 03:55:27 2019

@author: yaochungliang
"""

__metaclass__=type
class Employee:
    
    raise_amt = 1.04
    num_of_emps = 0
    def __init__(self,first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email= first + '.'+last +'@company.com'
        Employee.num_of_emps += 1
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
    @classmethod
    def from_string(cls,emp_str):
        first,last,pay= emp_str.split('-')
        return cls(first,last,pay)
    @staticmethod
    def is_workday(day):
        if day.weekday()==5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amt=1.10
    def __init__(self,first, last, pay,prog_lang):
        super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay)
        self.prog_lang =prog_lang

class MAnager(Employee):
    
    def __init__(self,first, last, pay, employees=None):
        #super().__init__(first,last,pay)
        #Employee.__init__(self,first,last,pay)
        if employee is None:
            self.employees = []
        
        
dev_1=Developer("corey","dick",50000,"Java")
dev_2=Developer("papa",'man',60000,"python")


print(dev_1.email)
dev_1.apply_raise()
print(dev_1.prog_lang)
+


#print(help(Developer))

#print(dev_1.email)



#emp_1=Employee("corey","dick",50000)
#emp_2=Employee("papa",'man',60000)



#
#import datetime
#my_date=datetime.date(2016,07,11)
#print(Employee.is_workday(my_date)