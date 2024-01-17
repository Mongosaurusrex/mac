from math import factorial
from typing import List, Tuple, Dict, Union

from mac.agent import Agent


def run_suite(
    agents: List[Agent], num_of_iterations: int
) -> Tuple[List[Agent], Dict, Dict]:
    data: List[int] = []
    categories: List[int] = []

    print("Running suite... 🏃")

    for _ in range(num_of_iterations):
        for agent in agents:
            agent.play()
    for result in range(num_of_iterations):
        agents_with_current_results = list(
            filter(lambda agent: agent.wins == result, agents)
        )
        data.append(len(agents_with_current_results))
        categories.append(result)

    graph_data = {
        "data": data,
        "categories": categories,
    }

    statistic_data = {
        "categories": categories,
        "data": binomial_distribution_over_all(num_of_iterations, 0.5),
    }

    print("Done! ✅")
    return (agents, graph_data, statistic_data)


def binomial_coefficient(n: int, k: int) -> int:
    return int(factorial(n) / (factorial(k) * factorial(n - k)))


def binomial_distribution(k: int, n: int, p: float) -> float:
    return binomial_coefficient(n, k) * p**k * (1 - p) ** (n - k)


def binomial_distribution_over_all(total_amount: int, p: float) -> List[float]:
    return [binomial_distribution(k, total_amount, p) for k in range(total_amount)]
