import random
import matplotlib.pyplot as plt
import numpy as np

prisoners_100 = list(range(1, 101, 1)) 
boxes_100 = list(range(1, 101, 1)) 
live_or_die = []


# this function models 100 prisoners going in to check 50 (out of 100) boxes 
# starting with the box that matches their prison number
# if they find their prison number within 50 boxes
# they live and the next prisoner does the same until 
# all prisoners have had their turn or until a prisoner does not find their number within 50 boxes
# if all prisoners find their number within 50 boxes, all prisoners live and that is one prison where everyone lives
# if even one prisoner does not find their number within 50 boxes
# no other prisoner will get a chance to check
# and all prisoners will die and that is one prison where everyone dies
# returns one of either: "live" or "die"

def onehundred_prisoners (prisoners):                                   
    boxes = [0]
    boxes = boxes + random.sample (boxes_100, 100)                                                                                              
    live = 0

    for prison_number in prisoners:
        box_count = 0
        number_in_box = boxes [prison_number]                           # index position is same as prison_number
        box_count += 1

        while number_in_box != prison_number and box_count <50:         # while prison number not found in fewer than 50 boxes
            number_in_box = boxes [number_in_box]                       # index position becomes the number in the previous box
            box_count += 1
        if box_count == 50 and number_in_box != prison_number:          # if prison number not found in 50 boxes
            live_or_die.append("die")                                   # add "die" and break from the loop: if one dies, all die
            break
        else:
            live += 1                                                   # if live, add 1
            if live == 100:                                             # if all 100 live    
                live_or_die.append("live")                              # add "live"
            continue 
    
    return live_or_die


# this function simulates the 100 prisoners function 101 times (e.g. 101 prisons)
# it collates 101 "live" or "die"
# and finds a percentage of prisons where everyone lives
# and returns a single percentage

def simulate_prisoners():    
    for i in range (101):                                               # simulate the prisoners function 101 times
        simulation = onehundred_prisoners(prisoners_100)

    live = live_or_die.count("live")                                    # count the number of "live"
    percent_live = round((live/len(live_or_die)*100.00),2)              # % live (should be approx 30%)
    return percent_live                                                 # print(percent_live,"%")


# this loops through the above simulation 120 times (e.g. 120 prisons in each of 101 countries = 12120 prisons)
# it collates 120 percentages from the simulation (percentage of prisons where everyone lives)
# and calculates the mean average percentage
# it prints the mean average
# it plots the percentages in a histogram

percentages_list = []
for i in range (120): 
    mass_simulation = simulate_prisoners()
    percentages_list.append(mass_simulation)

average = round(np.mean(percentages_list),2)

# print("here are the percentages of groups that all lived:\n",percentages_list)
# print ("\nthis is the mean percentage of groups that all lived:",round(average,2))
plt.hist(percentages_list, edgecolor="blue", color="yellow", bins = 10)
plt.title("average percentage of prisons where all 100 prisoners live: {}".format(average))
plt.show()