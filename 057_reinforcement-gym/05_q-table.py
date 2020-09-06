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

# Perform Q-Learning
import numpy as np
# Initialize the q_table with zeros.
q_table = np.zeros([streets.observation_space.n, streets.action_space.n])
print ('\ninitialize q_table:')
print (q_table)

# Setup hyperparameter
learning_rate = 0.1
discount_factor = 0.6
exploration = 0.1
epochs = 10000

print ('\nlearning_rate: ', learning_rate)
print ('discount_factor:', discount_factor)
print('exploration:', exploration)
print ('epochs:', epochs)

for taxi_run in range(epochs):
    state = streets.reset()
    done = False
    
    while not done:
        random_value = random.uniform(0, 1)
        if (random_value < exploration):
            action = streets.action_space.sample() # Explore a random action
        else:
            action = np.argmax(q_table[state]) # Use the action with the highest q-value
            
        next_state, reward, done, info = streets.step(action)
        
        prev_q = q_table[state, action]
        next_max_q = np.max(q_table[next_state])
        new_q = (1 - learning_rate) * prev_q + \
        learning_rate * (reward + discount_factor * next_max_q)

        q_table[state, action] = new_q
        
        state = next_state

print ('\nfinal q_table:')
print (q_table)
print ('\nfinal q_table[initial_state]:')
print (q_table[initial_state])