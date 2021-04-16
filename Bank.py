from Agent import Agent

class Bank:
    def __init__(self, factor):
        self.deposit = 0
        self.multiplication_factor = factor
    
    def multiply_deposit(self):
        self.deposit *= self.multiplication_factor
    
    def pay_in(self, agent: Agent):
        self.deposit += agent.contribute()
    
    def pay_out(self, agents):
        for agent in agents:
            agent.recieve(self.deposit/len(agents))
        self.deposit = 0
