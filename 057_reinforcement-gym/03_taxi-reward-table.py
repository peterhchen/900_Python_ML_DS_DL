# environment setup
import gym
import random

random.seed(1234)
streets = gym.make("Taxi-v3").env #New versions keep getting released; if -v3 doesn't work, try -v2 or -v4
streets.render()
# print ('streets:')
# print (streets)

# initial state
initial_state = streets.encode(2, 3, 2, 0)

streets.s = initial_state
streets.render()

# Reward Table
streets.P[initial_state]
print ('streets.P[initial_state]:')
for x in streets.P[initial_state]:
    print (streets.P[initial_state][x])