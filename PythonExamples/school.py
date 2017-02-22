#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
Created on 2017年2月16日

@author: wangyong
'''
#class SubClassName (ParentClass1[, ParentClass2, ...]):
   #'Optional class documentation string'
   #class_suite

class Person():
    '''所有人员的基类'''
    sex = '男' # 公开变量
    __tel = '' # 私有变量
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def setAge(self,age):
        self.age = age
        
    def getAge(self):
        return self.age  
    
    def setName(self,name):
        self.name = name
        
    def getName(self):
        return self.name    
    
    def printInfo(self):
        print 'age:',self.getAge(),'name:',self.getName()

class  Teacher(Person):
    '''教师'''
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary        

    def setSalary(self,salary):
        self.salary = salary
        
    def getSalary(self):
        return self.salary   
    #重写 printInfo 方法
    def printInfo(self):
        print 'age:',self.getAge(),'name:',self.getName(),'salary:',self.getSalary()
        
class Student(Person):  
    
    tel = '189000000'
    __sex = '男' # 私有变量
    
    def __init__(self, name, score):  
        self.name = name  
        self.score = score    
        
    def getSex(self):
        return self.__sex   
              
if __name__ == '__main__':
    p = Person('tom','18')
    p.printInfo()
    p.setAge(20)
    p.setName('jack')
    p.printInfo()
    p.sex = '女'
    print p.sex 
    #print p.__tel # 报错，实例不能访问私有变量

    t = Teacher('obama',68,100)
    t.sex = '男'
    print t.sex 
    t.printInfo()
