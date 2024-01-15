from dataclasses import dataclass
import random
from typing import List


@dataclass
class AgentHistory:
    win: bool
    outcome: float


class Agent:
    def __init__(self, winning_probability: float = 0.5):
        self.winning_probability = winning_probability
        self.loosing_probability = 1 - winning_probability
        self.history: List[AgentHistory] = []
        self.wins = 0

    def play(self) -> None:
        random_number = random.random()

        if random_number >= self.winning_probability:
            self.history.append(AgentHistory(win=True, outcome=random_number))
            self.wins += 1
        else:
            self.history.append(AgentHistory(win=False, outcome=random_number))
