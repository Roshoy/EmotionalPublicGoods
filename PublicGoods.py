from Bank import Bank
from Agent import Agent
from Strategies import Greedy, Cooperative, EmotionalStrategy


class PublicGoods:
    def __init__(self):
        self.bank = Bank(1.5)
        self.iterations = 10
        self.agents = []

    def run(self):
        for i in range(self.iterations):
            self.bank.pay_in(self.agents)
            self.bank.multiply_deposit()
            self.bank.pay_out(self.agents)
            for agent in self.agents:
                agent.get_inspired(self.agents)
    
    def addEmotionalAgent(self,anger = 1, gratitude = 1, admiration = 1, name=""):
        strategy = EmotionalStrategy(anger,gratitude,admiration)
        self.agents.append(Agent(name, strategy))
    
    def addLearningAgent(self,name=""):
        strategy = EmotionalStrategy(is_smart = True)
        self.agents.append(Agent(name, strategy))

    def addGreedyAgent(self,name=""):
        strategy = Greedy()
        self.agents.append(Agent(name, strategy))

    def addCooperativeAgent(self,name=""):
        strategy = Cooperative()
        self.agents.append(Agent(name, strategy))

    def reset(self):
        for agent in self.agents:
            agent.reset()