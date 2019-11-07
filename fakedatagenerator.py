#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 13:03:06 2019

@author: ubuntu
"""

from faker import Faker
import pandas as pd
import random
import numpy as np
from dateutil.relativedelta import relativedelta
from datetime import date


class fakedata:
    
    def binomial(n=1, p=20):
        return np.random.binomial(n,p)

    def exponential():
        return np.random.exponential()
    
    def normal(loc=1, scale=100):
        return np.random.normal(loc, scale)
        
    def poisson():
        return np.random.poisson()
    
    def uniform():
        return np.random.uniform()
    
    def beta(a=1, b=1):
        return np.random.beta(a, b)
    
    def gamma(shape=2, scale=1.0):
        return np.random.gamma(shape, scale)
    
    def multinomial():
        return np.random.multinomial()
    
    def __init__ (self, startemployee_id):
        self.startemployee_id = startemployee_id
        self.distributions = [
            self.binomial,
            self.exponential,
            self.normal,
            self.poisson,
            self.uniform,
            self.beta,
            self.gamma,
            self.multinomial
            ]    
        
    def Fakedatagenerator(self, distributionNameList=[normal], 
                          distColumnNameList=['NewColumn'], 
                          numberOfFields=10,
                          savecsv=True,
                          filename='output'):
        df = pd.DataFrame()
        fake = Faker()
        gender = ['M', 'F']
        
        for number in range(numberOfFields):
            sex = random.choice(gender)
            for distributionName in distributionNameList:
                dist_type = distributionName
            new_profile = fake.profile(sex=sex)
            new_profile['longitude'] = float(new_profile["current_location"][0])
            new_profile['latitude'] = float(new_profile["current_location"][1])
            for ColumnName in distColumnNameList:
                new_profile[ColumnName] = dist_type()
            rdelta = relativedelta(date.today(), new_profile['birthdate'])
            new_profile['age'] = rdelta.years
            new_profile['boolean'] = fake.boolean()
            new_profile['employee_id'] = self.startemployee_id
            self.startemployee_id = self.startemployee_id+1
            del new_profile["current_location"]
            df = df.append(new_profile, ignore_index=True)
            df.index = df.employee_id
        if savecsv == True:
            df.to_csv(filename+'.csv', header=True, index=True)
            return df
        else:
            return df
            
