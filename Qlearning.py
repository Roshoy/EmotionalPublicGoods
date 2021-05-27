import random

# consts for Bellman equation
epsilon = 0.9
discount_factor = 0.9  # discount factor for future rewards
learning_rate = 0.9  # the rate at which the agent should learn

# initialization
q_values = {}
t = range(0, 3)
states = [(anger, gratitude) for anger in t for gratitude in t]
for state in states:
    q_values[state] = [0, 0]  # [not pay, pay]


def get_next_action(agent_state):
    if random.random() < epsilon:
        return max(q_values[agent_state])
    else:
        return random.randint(0, 1)  # 0 - not pay; 1 - pay


def update_q_table(previous_state, current_state, action, reward):
    # Bellman equation:
    # Q = old_Q + learning_rate * (reward + discount_factor * estimated_optimal future_value - old_Q)
    old_q = q_values[previous_state][action]
    temporal_difference = reward + discount_factor * max(current_state) - old_q
    new_q = old_q + (learning_rate * temporal_difference)
    q_values[previous_state][action] = new_q
