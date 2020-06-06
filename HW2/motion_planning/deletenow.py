# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 03:55:27 2019

@author: yaochungliang
"""


class Employee:
    
    raise_amt = 1.04
    num_of_emps = 0
    def __init__(self,first, last):
        self.first = first
        self.last = last
        self.email= first + '.'+last +'@company.com'
    @property
    def email(self):
        return "{}.{}@gggg.com".format(self.first,self.last)        
    @property
    def fullname(self):
        return "{} {}".format(self.first,self.last)
    @fullname.setter
    def fullname(self,name):
        first,last = name.split(' ')
        self.first=first
        self.last=last
        
        
emp_1.fullname = "coo loo"
emp_1=Employee("corey","dick")    

print(emp_1.first)
print(emp_1.email)
#print(emp_1.email())
print(emp_1.fullname())

#    def apply_raise(self):
#        self.pay = int(self.pay * self.raise_amt)
#    def __repr__(self):
#        return "Employee('{}','{}',{})".format(self.first,self.last,self.pay)
#    def __str__(self):
#        return '{} - {}'.format(self.fullname(),self.email)
#    def __add__(self, other):
#        return self.pay + other.pay
#    def __len__(self):
#        return len(self.fullname())
#emp_1=Employee("corey","dick",50000)
#
#emp_2=Employee("corey","dick",60000)
#
#
#print(1+2)
#print(int.__add__(1,2))
#print(str.__add__("a","b"))
#
#print(emp_1+emp_2)
#print('test'.__len__())
#print(len(emp_1))

#print(emp_1)
#print(repr(emp_1))
#print(str(emp_1))
#
#print(emp_1.__repr__())
#print(emp_1.__str__())

#    @classmethod
#    def set_raise_amt(cls,amount):
#        cls.raise_amt = amount
#    @classmethod
#    def from_string(cls,emp_str):
#        first,last,pay= emp_str.split('-')
#        return cls(first,last,pay)
#    @staticmethod
#    def is_workday(day):
#        if day.weekday()==5 or day.weekday() == 6:
#            return False
#        return True
#
#class Developer(Employee):
#    raise_amt=1.10
#    def __init__(self,first, last, pay,prog_lang):
#        super().__init__(first,last,pay)
#        #Employee.__init__(self,first,last,pay)
#        self.prog_lang =prog_lang
#
#class MAnager(Employee):
#    
#    def __init__(self,first, last, pay, employees=None):
#        #super().__init__(first,last,pay)
#        #Employee.__init__(self,first,last,pay)
#        if employee is None:
#            self.employees = []
#        
#        
#dev_1=Developer("corey","dick",50000,"Java")
#dev_2=Developer("papa",'man',60000,"python")
#
#
#print(dev_1.email)
#dev_1.apply_raise()
#print(dev_1.prog_lang)



#print(help(Developer))

#print(dev_1.email)



#emp_1=Employee("corey","dick",50000)
#emp_2=Employee("papa",'man',60000)



#
#import datetime
#my_date=datetime.date(2016,07,11)
#print(Employee.is_workday(my_date)