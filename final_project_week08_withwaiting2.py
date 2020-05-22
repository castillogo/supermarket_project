# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 15:31:51 2020

@author: casti
"""

import random
import pandas as pd
import numpy as np
from faker import Faker
import time
import cv2
import matplotlib.pyplot as plt

CHECKOUT = [100, 220, 360, 525]
AISLES = [[200,300], [200,150], [200,780], [200,550], [530,100]]
locations = ["dairy","drinks","fruit","spices","checkout"]
transitionName = [locations, locations, locations, locations, locations]


class Human:
    """This is a Human class, with some attributes and behaviour"""
    aisle = np.random.choice(locations)
    locationList = [aisle]
    prob = 1
    probList = [prob]
    def __init__(self, name, aisle, prob_matrix, locationList):
        self.name = customername
        self.aisle = np.random.choice(locations)
        self.aisleindex = locations.index(self.aisle)
        self.prob_matrix = transitionMatrix[self.aisleindex]
        self.locationList = locationList


    def move(self):
        self.aisle = np.random.choice(locations[0:3])
        self.locationList = [self.aisle]
        self.aisleindex = locations.index(self.aisle)
        self.prob = 1
        self.probList = [self.prob]
        d = locations.index(self.aisle)
        e = AISLES[d]
        coordinateslist.append(e)
        while True:
            self.change = np.random.choice(transitionName[self.aisleindex],replace=True,p=transitionMatrix[self.aisleindex])
            self.locationList.append(self.change)
            self.prob=self.prob * transitionMatrix[locations.index(self.aisle)][locations.index(self.change)]
            self.probList.append(self.prob)
            b = locations.index(self.change)
            c = AISLES[b]
            coordinateslist.append(c)
            if self.change==locations[4]:
                break
            else:
                self.aisle=self.change
                self.aisleindex = locations.index(self.aisle)
                continue
            yield c
        print(f"{self.name} went through the following aisles in the supermarket: {self.locationList}")
        a = self.locationList
        supermarket_path_list.append(a)
        yield c

monday = pd.read_csv('monday.csv', sep=';')
monday = monday.sort_values(by=['customer_no', 'timestamp'])
monday['transition_aisle'] = monday['location'].shift(-1)
monday.loc[monday['location'] == 'checkout', 'transition_aisle'] = 'checkout'
monday.fillna('checkout', inplace=True)

P = pd.crosstab(monday['location'], monday['transition_aisle'], normalize=0)
checkoutdf = P.pop('checkout')
P['checkout']=checkoutdf
target_row = P.ix[[0],:]
P.drop([P.index[0]], axis=0, inplace=True)
P = pd.concat([P, target_row], axis=0)
P2 = P.values

transitionMatrix = P2.tolist()

f = Faker()
humanlist = []
supermarket_path_list = []
summary_usercoordinates = []

print('')
print('How many customers would you like to simulate?')
print('')
userwish = int(input())

print('')
print('This is a list of supermarket customers and where they spent their time:')
print('')

for i in range(userwish):
    name = f.name()
    humanlist.append(name)
for customername in humanlist:
    time.sleep(0.5)
    a=locations[0:3]
    coordinateslist=[]
    customer=Human(customername, np.random.choice(a), transitionMatrix, [np.random.choice(a)])
    customer.move()
    next(customer.move())
    summary_usercoordinates.append(coordinateslist)

customerpathdictionary = dict(zip(humanlist, supermarket_path_list))
customercoordinatesdictionary = dict(zip(humanlist, summary_usercoordinates))
print('')
print('This is a list of the coordinates of the aisles where the customers spent time:')
print('')
print(summary_usercoordinates)
print('')
print(summary_usercoordinates, file=open("aislecoordinates.txt", 'w'))

PL = summary_usercoordinates

class Customer:
    '''
    The class customer is a blueprint for a customer flying around in space
    '''
    def __init__(self, image, starting_position, target_positions, speed=1):

        self.image = image
        self.location = np.array(starting_position)
        self.target_position = target_positions
        self.wp = 0
        self.h = self.image.shape[0]
        self.w = self.image.shape[1]
        self.speed = speed

    def fly(self):
        '''
        The method fly lets the customer fly from A to B
        '''

        # of target_position != location
        y, x = self.location

#        for i in range(1):
        if self.location[0]==self.target_position[self.wp][0] and self.location[1]==self.target_position[self.wp][1]:
            if not (self.location[0]==self.target_position[-1][0] and self.location[1]==self.target_position[-1][1]):
                self.wp+=1
        ty, tx = self.target_position[self.wp]


        #move right or left while waiting to start shopping:
        if ((tx == 630 and ty==600 ) or (tx == 800 and ty == 600)) and y == 600:
            trajectory = tx - x
            if trajectory > 0:
                self.location[1] += self.speed
            if trajectory < 0:
                self.location[1] -= self.speed

        #move left or right to reach checkout nr. 2
        else:
            if ((tx == 240 and ty == 530) and (x != 240 and y == 440)):
                trajectory = tx - x
                if trajectory > 0:
                    self.location[1] += self.speed
                if trajectory < 0:
                    self.location[1] -= self.speed

                #move down to reach checkout nr. 2
            if (x==240 and y == 440):
                trajectory = ty - y
                if trajectory > 0:
                    self.location[0] += self.speed
                if trajectory < 0:
                    self.location[0] -= self.speed

            # go up general
            if ((x != tx and y != 450) and (tx != 240)):
                trajectory = 100 - y
                if trajectory > 0:
                    self.location[0] += self.speed
                elif trajectory < 0:
                    self.location[0] -= self.speed

            # go right or left general
            if ((x != tx and y == 100) or (x != tx and y == 450)):
                trajectory = tx - x
                if trajectory > 0:
                    self.location[1] += self.speed
                if trajectory < 0:
                    self.location[1] -= self.speed

            # go down general
            if ((x == tx and y>=100) and tx!=220):
                trajectory = ty - y
                if trajectory > 0:
                    self.location[0] += self.speed
                if trajectory < 0:
                    self.location[0] -= self.speed

class Simulation:
    '''
    The class simulation coordinates the simulation of flying customers
    '''

    def __init__(self, background, customers, counter):
        self.background = background
        self.customers = customers
        self.frame = background
        self.counter = counter

        #try putting the creation and destruction of the customers here (pop customer from list)
        #for waiting with the creation of customers, make loops where no customer is created

    def draw(self):
        self.frame = self.background.copy()
        for emoji in customers:
            y, x = emoji.location
            self.frame[y:y+emoji.h, x:x+emoji.w] = emoji.image

    def run_one_iteration(self):
        for emoji in customers:
            emoji.fly()




if __name__=='__main__':

    img = plt.imread('./images/market2.jpg')

    customers = []

    for i in range(len(PL)):
        #time.sleep(i)
        CL = PL[i]
        CL = CL[:-1]
        CL2 = CL+[[530, random.choice(CHECKOUT)]]
        if CL2[-1] == [530, 220]:
            CL2[-1] = [440, 340]
            CL2 = CL2 + [[530, 240]]
        CL3 = [[600, 630], [600, 800]]*i
        CL4 = CL3 + CL2

        #CL3 = CL2.insert(1, [500, 630], [500, 800])

        customers.append(Customer(cv2.imread('./images/SE.png'), \
        (600, 800),CL4, speed=((3/len(PL))*i+1)))

    sim = Simulation(img, customers, 1)

    counter=0
    while True:
        frame = img.copy()
        counter += 1
        sim.draw()
        sim.run_one_iteration()
        cv2.imshow('frame', sim.frame)
        if cv2.waitKey(3) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()
