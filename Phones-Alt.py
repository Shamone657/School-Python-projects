import csv

import numpy as np

import matplotlib.pyplot as plt

with open("phones.csv", mode="r", newline="") as file:
        
    reader=csv.reader(file)
        
    next(reader)# skips header
        
    brands = []
    
    model = []
    
    storage = []
    
    ram = []
    
    screen = []
    
    bat = []
    
    price = []
        
    for row in reader:
            
        #print(row) #shows csv contents in shell
        
        brands.append(row[0])
        
        model.append(row[1])
        
        storage.append(row[2])
        
        ram.append(row[3])
        
        screen.append(row[4])
        
        battery = int(row[6])
        
        bat.append(battery)
        
        prices = int(row[7])
        
        price.append(prices)
        
Brands = []
for q in brands:
    if q not in Brands:
        Brands.append(q)
    
sortedPrice = sorted(price) #Sorts prices by cost

Ram = [y.replace("GB","") for y in ram] #Removes GB from ram list

for i in range(len(Ram)): #Converts Ram to int
    
    Ram[i] = int(Ram[i])

Storage = [y.replace("GB","") for y in storage] #Removes GB from storage list

for o in range(len(Storage)): #Converts Storage to int 
    
    Storage[o] = int(Storage[o])

def minNum(l):
    print('Minimum number is' ,l[0],'.')

def maxNum(l):
    lsort = sorted(l)
    print('Maximum number is' ,lsort[len(l) - 1] ,'.')
    
def mean(l):
    lsort = sorted(l)
    total = sum(lsort)
    print('Mean is ', total/len(lsort),'.')

def median(l):
    mid = (len(l) // 2)
    
    if mid % 2 == 0:
        median = (l[mid] + l[mid - 1]) / 2
        print('Median is ', median)

    else:
        print('Median is',l[mid])
        
def mode(l):
    names = []
    co = []
    for i in l:
        if i not in names:
            names.append(i)
        
    for j in names:
        total = l.count(j)
        co.append(total)
    
    print("Value | Frequency")
    print("-----------------")
    for i in range(len(names)):
        print(f"{names[i]:<6} | {co[i]}")

Brands = []
for q in brands:
    if q not in Brands:
        Brands.append(q)

brand_price = []

for brand in Brands:
    total = 0
    for m in range(len(brands)):
        if brands[m] == brand:
            total += price[m]

    brand_price.append(total)
    #print(brand,"-", total)
    
mode(brands)

