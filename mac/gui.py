from typing import List, Tuple, Union, Dict

import numpy as np
import time
import matplotlib.pyplot as plt
from mplcursors import cursor

from mac.agent import Agent


def collect_info() -> Tuple[List[Agent], int]:
    print("Before we start we need to setup the test")
    number_of_agents = int(input("How many agents are we going to have? "))
    print(f"Ok, we will use {number_of_agents} agents 🤖")
    number_of_cheaters = int(input("How many cheating agents are we going to have? "))
    print(f"Ok, we will have {number_of_agents} cheating agents 😈")

    agents = []

    for created_amount in range(number_of_agents):
        if created_amount < number_of_cheaters:
            agent = Agent(winning_probability=0.6, is_cheater=True)
        else:
            agent = Agent()
        agents.append(agent)

    num_of_iterations = int(input("How many iterations do you want to run? "))

    print(f"Ok, we will run for {num_of_iterations} iterations 🕒")

    return agents, num_of_iterations


def show_results(result: Dict, statistic_data: Dict) -> None:
    print("Presenting suite results... 📈")
    fig, (ax1, ax2) = plt.subplots(1, 2)

    ax1.bar(result["categories"], result["data"])
    ax1.set_title("Simulation results")
    ax1.set_xlabel("Wins")
    ax1.set_ylabel("Number of agents")
    ax2.bar(statistic_data["categories"], statistic_data["data"])
    ax2.set_title("Binomial distribution")
    ax2.set_xlabel("Wins")
    ax2.set_ylabel("Probability")

    plt.show()
