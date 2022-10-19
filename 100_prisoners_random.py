import random
import matplotlib.pyplot as plt
import numpy as np

list_100 = list(range(1, 101, 1)) 
prisoners = list_100
live_or_die = []

def onehundred_prisoners_random(prisoners):
    for prisoner in prisoners:
        boxes = [0] 
        boxes = boxes + random.sample(list_100, 50)
        live = 0

        if prisoner not in boxes:
            live_or_die.append("die")
            break

        else:
            live += 1                                                   # if live, add 1

            if live == 100:                                             # if all 100 live    
                live_or_die.append("live")                              # add "live"
            continue

        return live_or_die
    
for i in range (250000):
    simulation = onehundred_prisoners_random(prisoners)
    
simulation
live = live_or_die.count("live")                                    # count the number of "live"
die = live_or_die.count("die")                                      # count the number of "die"
percentage_live = round(live/len(live_or_die)*100,32)
print("percentage of prisons where everyone lived: {}".format(percentage_live))