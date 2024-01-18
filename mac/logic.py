from math import factorial, ceil
from typing import List, Tuple, Dict

from mac.agent import Agent


def run_suite(
    agents: List[Agent], num_of_iterations: int
) -> Tuple[List[Agent], Dict, Dict, List[List[Agent]]]:
    agent_distribution: List[List[Agent]] = []
    data: List[int] = []
    categories: List[int] = []

    print("Running suite... 🏃")

    for _ in range(num_of_iterations):
        for agent in agents:
            agent.play()
    for result in range(num_of_iterations + 1):
        agents_with_current_results = list(
            filter(lambda agent: agent.wins == result, agents)
        )
        data.append(len(agents_with_current_results))
        agent_distribution.append(agents_with_current_results)
        categories.append(result)

    graph_data = {
        "data": data,
        "categories": categories,
    }

    statistic_data = {
        "categories": categories,
        "data": binomial_distribution_over_all(num_of_iterations + 1, 0.5),
    }

    print("Done! ✅")
    return (agents, graph_data, statistic_data, agent_distribution)


def binomial_coefficient(n: int, k: int) -> int:
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def binomial_distribution(k: int, n: int, p: float) -> float:
    return binomial_coefficient(n, k) * p**k * (1 - p) ** (n - k)


def binomial_distribution_over_all(total_amount: int, p: float) -> List[float]:
    return [binomial_distribution(k, total_amount, p) for k in range(total_amount)]


def anti_cheat_eval(num_of_iterations: int, agent_list: List[List[Agent]]) -> None:
    accusation_theshold = None
    for i in range(num_of_iterations):
        accused_slices = agent_list[i:]
        non_accused_slices = agent_list[:i]
        non_accused_cheaters: List[Agent] = [
            agent for slice in non_accused_slices if len(slice) > 0 for agent in slice
        ]
        accused_cheaters: List[Agent] = [
            agent for slice in accused_slices if len(slice) > 0 for agent in slice
        ]

        true_positive_cheaters = len(
            list(filter(lambda agent: agent.is_cheater == True, accused_cheaters))
        )
        false_positive_cheaters = len(
            list(filter(lambda agent: agent.is_cheater == False, accused_cheaters))
        )
        true_negative_cheaters = len(
            list(filter(lambda agent: agent.is_cheater == False, non_accused_cheaters))
        )
        false_negative_cheaters = len(
            list(filter(lambda agent: agent.is_cheater == True, non_accused_cheaters))
        )

        total_fair_players = false_positive_cheaters + true_negative_cheaters
        total_cheating_players = true_positive_cheaters + false_negative_cheaters

        try:
            false_accusations = false_positive_cheaters / total_fair_players
        except ZeroDivisionError:
            false_accusations = 0
        try:
            correct_accusations = true_positive_cheaters / total_cheating_players
        except ZeroDivisionError:
            correct_accusations = 0

        if correct_accusations >= 0.8 and false_accusations < 0.05:
            accusation_theshold = i
            break

    if not accusation_theshold:
        print(
            "Chould not find a treshold for a good enough accusation given the success parameters"
        )
    else:
        print(
            f"Given the inputs we should accuse everyone that has more than {accusation_theshold}/{num_of_iterations}"
        )
