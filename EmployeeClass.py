# -*- coding: utf-8 -*-
"""
Created on Thu May 19 15:32:13 2022

@author: Cloud
"""

class Employee:
    def __init__(self,eid,ename,eloc,esal):
        self.eid = eid
        self.ename = ename
        self.eloc = eloc
        self.esal = esal
    def GetEmployee(self):
        print("Employee ID:",self.eid,"\nEmployee name:",self.ename,
              "\nEmployee location:",self.eloc,"\nEmployee salary:",self.esal)
        