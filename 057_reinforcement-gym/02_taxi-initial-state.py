# environment setup
import gym
import random

random.seed(1234)
streets = gym.make("Taxi-v3").env #New versions keep getting released; if -v3 doesn't work, try -v2 or -v4
streets.render()

# initial satte
initial_state = streets.encode(2, 3, 2, 0)

streets.s = initial_state
streets.render()
