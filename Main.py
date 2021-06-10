import random

import matplotlib.pyplot as plt
from Bank import Bank
from Agent import Agent
from Strategies import Greedy, Cooperative, EmotionalStrategy
from pathlib import Path
from PublicGoods import PublicGoods


def binary():
    dir = 'plots/binary_model/'
    Path(dir).mkdir(parents=True, exist_ok=True)

    greedy_strategy = Greedy()
    cooperative_strategy = Cooperative()
    final_sum = []

    def iteration(bank, agents, i):
        iterations.append(i)
        avg_contribution = bank.pay_in(agents)
        avg_contributions.append(avg_contribution)
        bank.multiply_deposit()
        payoff = bank.pay_out(agents)
        payoffs.append(payoff)

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

        agent_balance = [(x.name, x.money) for x in agents]
        agent_balance = sorted(agent_balance, key=lambda x: x[1])
        final_sum.append(sum([a.money for a in agents]))

        plt.figure()
        plt.plot(iterations, avg_contributions)
        plt.xlabel('iteration')
        plt.ylabel('average contribution')
        title = f'Average contribution per iteration - {free_riders_num} free-riders - {agents_num} agents'
        plt.title(title)
        plt.savefig(f'{dir}avg_contribution_{free_riders_num}_freeriders.png')
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
        plt.savefig(f'{dir}final_balance_{free_riders_num}_freeriders.png')
        plt.close()

    plt.figure()
    plt.plot(range(agents_num + 1), final_sum)
    plt.xlabel('Number of Freeriders')
    plt.ylabel('Final summary balance')
    title = f'Final summary balance per number of freeriders - {agents_num} agents'
    plt.title(title)
    plt.tight_layout()
    plt.savefig(f'{dir}final_sum_{free_riders_num}_freeriders.png')
    plt.close()


def emotions(greedy_count=0, coop_count=0, admiration=5):
    dir = 'plots/emotions_model/'
    Path(dir).mkdir(parents=True, exist_ok=True)

    predefined_strategies = {
        'responsive': (1, 1),
        'active': (1, 2),
        'distrustful': (1, 3),
        'accepting': (2, 1),
        'impartial': (2, 2),
        'non-accepting': (2, 3),
        'trustful': (3, 1),
        'passive': (3, 2),
        'stubborn': (3, 3)
    }

    emotional_agents = []
    bank = Bank(1.5)
    iterations = 10

    thresholds = [(a, g) for a in range(1, 4) for g in range(1, 4)]
    thresholds.append((2, 2))

    agent_num = 0
    for (anger, gratitude) in thresholds:
        # anger = random.randint(1, 3)
        # gratitude = random.randint(1, 3)
        agent_num += 1
        name = f'Agent{agent_num}(A={anger}, G={gratitude})'
        strategy = EmotionalStrategy(anger_threshold=anger, gratitude_threshold=gratitude,
                                     admiration_threshold=admiration)
        emotional_agents.append(Agent(name, strategy))

    for i in range(greedy_count):
        agent_num += 1
        name = f'Agent{agent_num}(Greedy)'
        strategy = Greedy()
        emotional_agents.append(Agent(name, strategy))

    for i in range(coop_count):
        agent_num += 1
        name = f'Agent{agent_num}(Coop)'
        strategy = Cooperative()
        emotional_agents.append(Agent(name, strategy))

    strategy = EmotionalStrategy(is_smart=True)
    emotional_agents.append(Agent('Smart', strategy))

    for i in range(iterations):
        bank.pay_in(emotional_agents)
        bank.multiply_deposit()
        bank.pay_out(emotional_agents)
        for agent in emotional_agents:
            agent.get_inspired(emotional_agents)

    final_money = list(map(lambda agent: agent.money, emotional_agents))
    labels = list(map(lambda agent: agent.name, emotional_agents))

    x = range(len(labels))  # the label locations
    width = 0.5  # the width of the bars

    fig, ax = plt.subplots()

    ax.bar(x, final_money, width=width)
    ax.set_ylabel('Final deposit')
    ax.set_title('Deposit by agents')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=90)
    fig.tight_layout()

    plt.savefig(f'{dir}deposit_by_emotional_agents_with_others_adm{admiration}.png')

    counts = [0, 0, 0]
    for agent in emotional_agents:
        if isinstance(agent.strategy, Greedy):
            counts[0] += 1
        elif isinstance(agent.strategy, Cooperative):
            counts[1] += 1
        elif isinstance(agent.strategy, EmotionalStrategy):
            counts[2] += 1

    ls = ['Greedy', 'Cooperative', 'Emotional']

    fig, ax = plt.subplots()

    ax.bar(ls, counts, width=width)
    ax.set_ylabel('Count of agents')
    ax.set_title('Final state of strategies count')
    ax.set_xticks(range(3))
    ax.set_xticklabels(ls, rotation=90)
    fig.tight_layout()

    plt.savefig(f'{dir}final_state_of_strats_emotion_and_others.png')


def emotions(greedy_count=0, coop_count=0, admiration=5):
    dir = 'plots/emotions_model/'
    Path(dir).mkdir(parents=True, exist_ok=True)

    predefined_strategies = {
        'responsive': (1, 1),
        'active': (1, 2),
        'distrustful': (1, 3),
        'accepting': (2, 1),
        'impartial': (2, 2),
        'non-accepting': (2, 3),
        'trustful': (3, 1),
        'passive': (3, 2),
        'stubborn': (3, 3)
    }

    emotional_agents = []
    bank = Bank(1.5)
    iterations = 10

    thresholds = [(a, g) for a in range(1, 4) for g in range(1, 4)]
    thresholds.append((2, 2))

    agent_num = 0
    for (anger, gratitude) in thresholds:
        # anger = random.randint(1, 3)
        # gratitude = random.randint(1, 3)
        agent_num += 1
        name = f'Agent{agent_num}(A={anger}, G={gratitude})'
        strategy = EmotionalStrategy(anger_threshold=anger, gratitude_threshold=gratitude,
                                     admiration_threshold=admiration)
        emotional_agents.append(Agent(name, strategy))

    for i in range(greedy_count):
        agent_num += 1
        name = f'Agent{agent_num}(Greedy)'
        strategy = Greedy()
        emotional_agents.append(Agent(name, strategy))

    for i in range(coop_count):
        agent_num += 1
        name = f'Agent{agent_num}(Coop)'
        strategy = Cooperative()
        emotional_agents.append(Agent(name, strategy))

    strategy = EmotionalStrategy(is_smart=True)
    emotional_agents.append(Agent('Smart', strategy))

    for i in range(iterations):
        bank.pay_in(emotional_agents)
        bank.multiply_deposit()
        bank.pay_out(emotional_agents)
        for agent in emotional_agents:
            agent.get_inspired(emotional_agents)

    final_money = list(map(lambda agent: agent.money, emotional_agents))
    labels = list(map(lambda agent: agent.name, emotional_agents))

    x = range(len(labels))  # the label locations
    width = 0.5  # the width of the bars

    fig, ax = plt.subplots()

    ax.bar(x, final_money, width=width)
    ax.set_ylabel('Final deposit')
    ax.set_title('Deposit by agents')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=90)
    fig.tight_layout()

    plt.savefig(f'{dir}deposit_by_emotional_agents_with_others_adm{admiration}.png')

    counts = [0, 0, 0]
    for agent in emotional_agents:
        if isinstance(agent.strategy, Greedy):
            counts[0] += 1
        elif isinstance(agent.strategy, Cooperative):
            counts[1] += 1
        elif isinstance(agent.strategy, EmotionalStrategy):
            counts[2] += 1

    ls = ['Greedy', 'Cooperative', 'Emotional']

    fig, ax = plt.subplots()

    ax.bar(ls, counts, width=width)
    ax.set_ylabel('Count of agents')
    ax.set_title('Final state of strategies count')
    ax.set_xticks(range(3))
    ax.set_xticklabels(ls, rotation=90)
    fig.tight_layout()

    plt.savefig(f'{dir}final_state_of_strats_emotion_and_others.png')


# emotions(3, 3, admiration=10)

pg = PublicGoods()

pg.addLearningAgent(name=f"q-Learning")

thresholds = [(a, g) for a in range(1, 4) for g in range(1, 4)]

for (a, g) in thresholds:
    pg.addEmotionalAgent(anger=a, gratitude=g, name=f"Emot {a, g}")

for i in range(5):
    pg.addEmotionalAgent(anger=random.randint(1, 3), gratitude=random.randint(1, 3), name=f"Emot")

for i in range(1, 4):
    pg.addCooperativeAgent(name=f"Coop {i}")

for i in range(1, 4):
    pg.addGreedyAgent(name=f"Greed {i}")


for i in range(10):
    pg.run()

    final_money = [a.money for a in pg.agents]
    labels = [a.name for a in pg.agents]
    x = range(len(labels))  # the label locations
    width = 0.5  # the width of the bars

    fig, ax = plt.subplots()
    ax.bar(x, final_money, width=width)
    ax.set_ylabel('Final deposit')
    ax.set_title('Deposit by agents')
    ax.set_xticks(x)
    ax.set_xticklabels(labels, rotation=90)
    fig.tight_layout()
    plt.show()
    pg.reset()
