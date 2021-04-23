class Bank:
    def __init__(self, factor):
        self.deposit = 0
        self.multiplication_factor = factor

    def multiply_deposit(self):
        self.deposit *= self.multiplication_factor

    def pay_in(self, agents):
        total_contribution = 0.0
        for agent in agents:
            agent_contribution = agent.contribute()
            self.deposit += agent_contribution
            total_contribution += agent_contribution
        return total_contribution / len(agents)  # average contirbution

    def pay_out(self, agents):
        payoff = self.deposit / len(agents)
        for agent in agents:
            agent.receive(payoff)
        self.deposit = 0
        return payoff
