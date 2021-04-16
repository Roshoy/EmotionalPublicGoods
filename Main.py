import random
from Bank import Bank
from Agent import Agent

def iteration(bank, agents):
    for agent in agents:
        bank.pay_in(agent)
    bank.multiply_deposit()
    bank.pay_out(agents)
    # for agent in agents:
    #     print(agent)
    
bank = Bank(1.5)
agents = []
for i in range(0,100):
    agents.append(Agent(f'Agent{i}', random.random()))

for i in range(0,100):
    print('Iteration', i)
    iteration(bank, agents)

for agent in agents:
    print(agent)