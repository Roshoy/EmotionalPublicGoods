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

for a in range(0, 9):
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

    plt.figure()
    plt.plot(iterations, avg_contributions)
    plt.xlabel('iteration')
    plt.ylabel('average contribution')
    title = f'Average contribution per iteration - {free_riders_num} free-riders'
    plt.title(title)
    plt.savefig(f'plots/binary_model/avg_contribution_{free_riders_num}_freeriders.png')
