# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:23:11 2023

@author: Windows
"""

from pydantic import BaseModel
# 2. Class which describes Bank Notes measurements
class StudentInfo(BaseModel):
    sex: object 
    age: object 
    address: object
    famsize: object
    Pstatus: object
    Medu: int
    Fedu: int
    Mjob: object
    Fjob: object
    reason: object
    guardian: object
    traveltime: int
    studytime: int
    failures: int
    schoolsup: object
    famsup: object
    paid: object
    activities: object
    nursery: object
    higher: object
    internet: object
    romantic: object
    famrel: int
    freetime: int
    goout: int
    Dalc: int
    Walc: int
    health: int
    absences: int
    G1: int
    G2: int

    