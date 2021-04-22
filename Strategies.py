class Greedy:
    def __init__(self, greed_level=1.0):
        if greed_level > 1.0 or greed_level < 0.0:
            raise Exception('Greed level must be in range 0.0 - 1.0')
        self.greed_level = greed_level

    def calculate_contribution(self, agent_deposit):
        max_contribution = 0.2 * agent_deposit  # bardzo szczodry chciwy agent
        contribution = max_contribution * (1.0 - self.greed_level)
        return contribution

    def calculate_contribution_with_last_payoff(self, agent_deposit, last_payoff):
        # TODO: implement in future
        pass

    def __str__(self):
        return 'GREEDY strategy'


class Cooperative:
    def __init__(self, cooperation_level=1.0):
        if cooperation_level > 1.0 or cooperation_level < 0.0:
            raise Exception('Cooperation level must be in range 0.0 - 1.0')
        self.cooperation_level = cooperation_level

    def calculate_contribution(self, agent_deposit):
        max_contribution = agent_deposit
        min_contribution = 0.8 * max_contribution
        contribution = min_contribution + ((max_contribution - min_contribution) * self.cooperation_level)
        return contribution

    def calculate_contribution_with_last_payoff(self, agent_deposit, last_payoff):
        # TODO: implement in future
        pass

    def __str__(self):
        return 'COOPERATIVE strategy'
