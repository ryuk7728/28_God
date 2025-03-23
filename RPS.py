import random
import numpy as np

def reward(p1,p2):
    if p1 == 1:
        if p2 == 1:
            return 0
        if p2 == 2:
            return -1
        if p2 == 3:
            return 1  
    if p1 == 2:
        if p2 == 2:
            return 0
        if p2 == 3:
            return -1
        if p2 == 1:
            return 1
    if p1 == 3:
        if p2 == 3:
            return 0
        if p2 == 1:
            return -1
        if p2 == 2:
            return 1

def sample_action(strategy):
    random_no = random.random()
    if random_no<strategy[0]:
        return 1
    elif random_no<(strategy[0]+strategy[1]):
        return 2
    else:
        return 3

def compute_regret(p,rew):
    regret = np.array([0,0,0])
    for i in range(1,4):
        regret[i-1] = reward(i,p)-rew
    return regret


p1_strategy = [1,0,0] #Always play Rock
p2_strategy = [0,1,0] #Always play Paper
p1_regret = np.array([0,0,0])
p2_regret = np.array([0,0,0])

p1_reward = 0
p2_reward = 0

iterations = 10

p1_cum_reward=0


for i in range(iterations):

    p1 = sample_action(p1_strategy)
    p2 = sample_action(p2_strategy)
    print(p1,p2)
    p1_reward = reward(p1,p2)
    p2_reward = -p1_reward
    p1_cum_reward+=p1_reward

    p1_regret+=compute_regret(p2,p1_reward)
    p2_regret+=compute_regret(p1,p2_reward)
    if np.sum(np.maximum(p1_regret,0))>0:
        p1_strategy = np.maximum(p1_regret,0)/np.sum(np.maximum(p1_regret,0))
    if np.sum(np.maximum(p2_regret,0))>0:
        p2_strategy = np.maximum(p2_regret,0)/np.sum(np.maximum(p2_regret,0))
    print(p1_strategy,p2_strategy)

print(p1_strategy,p2_strategy)
# print(p1_cum_reward)