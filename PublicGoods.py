from Bank import Bank
from Agent import Agent
from Strategies import Greedy, Cooperative, EmotionalStrategy
import matplotlib.pyplot as plt


class PublicGoods:
    def __init__(self):
        self.bank = Bank(1.5)
        self.iterations = 100
        self.agents = []

    def run(self):
        for i in range(self.iterations):
            self.bank.pay_in(self.agents)
            self.bank.multiply_deposit()
            self.bank.pay_out(self.agents)
            # for agent in self.agents:
            #     agent.get_inspired(self.agents)

        fig, ax = plt.subplots()
        ax.plot(self.agents[0].balances, alpha=0.7, label='smart')
        ax.plot(self.agents[1].balances, alpha=0.6, label='emotional')
        ax.plot(self.agents[20].balances, alpha=0.5, label='greedy')
        ax.legend(loc="upper left")
        plt.show()

    def addEmotionalAgent(self, anger=1, gratitude=1, admiration=1, name=""):
        strategy = EmotionalStrategy(anger, gratitude, admiration)
        self.agents.append(Agent(name, strategy))

    def addLearningAgent(self, name=""):
        strategy = EmotionalStrategy(is_smart=True)
        self.agents.append(Agent(name, strategy))

    def addGreedyAgent(self, name=""):
        strategy = Greedy()
        self.agents.append(Agent(name, strategy))

    def addCooperativeAgent(self, name=""):
        strategy = Cooperative()
        self.agents.append(Agent(name, strategy))

    def reset(self):
        for agent in self.agents:
            agent.reset()
