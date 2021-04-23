import random
import matplotlib.pyplot as plt
from Bank import Bank
from Agent import Agent
from Strategies import Greedy, Cooperative

avg_contributions = []
iterations = []
payoffs = []


def iteration(bank, agents, i):
    iterations.append(i)
    avg_contribution = bank.pay_in(agents)
    avg_contributions.append(avg_contribution)
    bank.multiply_deposit()
    payoff = bank.pay_out(agents)
    payoffs.append(payoff)
    # for agent in agents:
    #     print(agent)


bank = Bank(1.5)
agents = []

greedy_strategy = Greedy()
cooperative_strategy = Cooperative()

free_riders_num = 1
agents_num = 10

for i in range(0, free_riders_num):
    agents.append(Agent(f'GreedyAgent{i}', greedy_strategy))

for i in range(free_riders_num, agents_num):
    agents.append(Agent(f'CooperativeAgent{i}', cooperative_strategy))

for i in range(0, 10):
    print('Iteration', i)
    iteration(bank, agents, i)

for agent in agents:
    print(agent)

print(avg_contributions)
print(payoffs)

plt.plot(iterations, payoffs, iterations, avg_contributions)
plt.ylabel('some numbers')
plt.show()
