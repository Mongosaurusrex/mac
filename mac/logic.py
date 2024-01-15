from typing import List, Tuple, Dict, Union

from mac.agent import Agent


def run_suite(agents: List[Agent], num_of_iterations: int) -> Tuple[List[Agent], Dict]:
    data: List[int] = []
    categories: List[str] = []

    print("Running suite... 🏃‍♂️")

    for _ in range(num_of_iterations):
        for agent in agents:
            agent.play()
    for result in range(num_of_iterations):
        agents_with_current_results = list(
            filter(lambda agent: agent.wins == result, agents)
        )
        data.append(len(agents_with_current_results))
        categories.append(f"Wins: {result}")

    graph_data = {
        "data": data,
        "categories": categories,
    }
    print("Done! ✅")
    return (agents, graph_data)
