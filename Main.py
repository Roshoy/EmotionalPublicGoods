import random
from Bank import Bank
from Agent import Agent
from Strategies import Greedy, Cooperative


def iteration(bank, agents):
    for agent in agents:
        bank.pay_in(agent)
    bank.multiply_deposit()
    bank.pay_out(agents)
    # for agent in agents:
    #     print(agent)


bank = Bank(1.5)
agents = []

greedy_strategy = Greedy()
cooperative_strategy = Cooperative()

free_riders_num = 10
agents_num = 100

for i in range(0, free_riders_num):
    agents.append(Agent(f'GreedyAgent{i}', greedy_strategy))

for i in range(free_riders_num, agents_num):
    agents.append(Agent(f'CooperativeAgent{i}', cooperative_strategy))

for i in range(0, 10):
    print('Iteration', i)
    iteration(bank, agents)

for agent in agents:
    print(agent)
