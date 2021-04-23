import random
import matplotlib.pyplot as plt
from Bank import Bank
from Agent import Agent
from Strategies import Greedy, Cooperative


def iteration(bank, agents, i):
    iterations.append(i)
    avg_contribution = bank.pay_in(agents)
    avg_contributions.append(avg_contribution)
    bank.multiply_deposit()
    payoff = bank.pay_out(agents)
    payoffs.append(payoff)


greedy_strategy = Greedy()
cooperative_strategy = Cooperative()
final_sum = []

for a in range(0, 11):
    avg_contributions, iterations, payoffs = [], [], []
    bank = Bank(1.5)
    agents = []
    free_riders_num = a
    agents_num = 10

    for i in range(0, free_riders_num):
        agents.append(Agent(f'GreedyAgent{i}', greedy_strategy))

    for i in range(free_riders_num, agents_num):
        agents.append(Agent(f'CooperativeAgent{i}', cooperative_strategy))

    for i in range(0, 10):
        # print('Iteration', i)
        iteration(bank, agents, i)

    # for agent in agents:
    #     print(agent)
    # print(avg_contributions)
    # print(payoffs)
    
    agent_balance = [(x.name,x.money) for x in agents]
    agent_balance = sorted(agent_balance,key=lambda x: x[1])
    final_sum.append(sum([a.money for a in agents]))

    plt.figure()
    plt.plot(iterations, avg_contributions)
    plt.xlabel('iteration')
    plt.ylabel('average contribution')
    title = f'Average contribution per iteration - {free_riders_num} free-riders - {agents_num} agents'
    plt.title(title)
    plt.savefig(f'plots/binary_model/avg_contribution_{free_riders_num}_freeriders.png')
    plt.close()
    agent_balance = list(zip(*agent_balance))
    plt.figure()
    plt.plot(agent_balance[0], agent_balance[1])
    plt.xticks(rotation=90)
    plt.xlabel('Greedy/Cooperative')
    plt.ylabel('Final balance')
    title = f'Final balance per greedy cooperative - {free_riders_num} freeriders - {agents_num} agents'
    plt.title(title)
    plt.tight_layout()
    plt.savefig(f'plots/binary_model/final_balance_{free_riders_num}_freeriders.png')
    plt.close()

plt.figure()
plt.plot(range(agents_num+1), final_sum)
plt.xlabel('Number of Freeriders')
plt.ylabel('Final summary balance')
title = f'Final summary balance per number of freeriders - {agents_num} agents'
plt.title(title)
plt.tight_layout()
plt.savefig(f'plots/binary_model/final_sum_{free_riders_num}_freeriders.png')
plt.close()
