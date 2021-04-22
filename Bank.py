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
        payoff = self.deposit / len(agents)
        for agent in agents:
            agent.receive(payoff)
        self.deposit = 0
