# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Homework #0

#from numpy import loadtxt only give me access to the comand loadtxt insted of the whole library on numpy
from numpy import loadtxt


def city_elevation(city, elevation):
    
    if isinstance(city, str) and isinstance(elevation,float): #isindex check if the value plugged in is a string, float, integer, etc.
    
        #the first input in the parentesis is the file I want to load, like HoneyRun.txt, and the other ones are, parameters of the function loadtxtx 
        honey_data = loadtxt("HoneyRun.txt",skiprows=1, delimiter=',') #(open file, skip 1st row, eliminate commas)
        #now I have access to HoneyRun.txt data
        
        sm_difference = 99999999999999999.0 #smallest difference that is going to be compared to the actual difference.
        sp = 0 #smallest possition
        c_poss = 0 #current possition , that is where I start
        ans_elev = honey_data[sp][0] #Im calling answer elevation a function that I can call in the return

        for el in honey_data[:,1]:#This for loop saves the values from honeyrun and give it to el
            delta = abs(elevation-el)#this is the equation that makes the diference between the given value and each value in el
            if (delta < sm_difference):#this if compare all the answers for delta and reduce it to the smallest difference in altitude
                sm_difference = delta
                sp = c_poss #the smallest possition is updated to be the current possition
                ans_elev = honey_data[sp][0]
            c_poss += 1 #moves the current possition to the next possition
                
        print("The most close distance for the given elevation is:", ans_elev)
        return ans_elev
    
       
    
    else:
        print("Please provide a string for the City value")

       
city = input("City:")
elevation = float(input("Elevation:"))
city_elevation(city, elevation)    




