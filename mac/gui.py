import termplotlib as tpl
import numpy as np
import time

from mac.agent import Agent


def collect_info():
    print("Before we start we need to setup the test")
    number_of_agents = int(input("How many agents are we going to have? "))
    agents = []
    for _ in range(number_of_agents):
        agent = Agent()
        agents.append(agent)

    print(f"Ok, we will use {len(agents)} agents 🤖")

    num_of_iterations = int(input("How many iterations do you want to run? "))

    print(f"Ok, we will run for {num_of_iterations} iterations 🕒")

    return agents, num_of_iterations


def show_results(graph_data):
    print("Displaying results... 📈")
    data = graph_data["data"]
    categories = graph_data["categories"]

    fig = tpl.figure()
    fig.barh(data, categories, force_ascii=True)
    fig.show()
